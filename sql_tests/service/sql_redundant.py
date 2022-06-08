from sql_tests.config import config


class SQLRedundant:

    @classmethod
    def update_redundant(cls, sql_node, prefixes):
        tables = sql_node.relation
        table = None
        keys = []
        for stmt in sql_node:
            if stmt.parent_attribute == "relation":
                table = tables.relname.value
            # More key
            if stmt.parent_attribute == "targetList":
                for item in stmt:
                    if item.val.node_tag == "A_Const":
                        key = item.name.value
                        keys.append(key)
                    # Set_keyParam include "case \n when than  \n else end"
                    if item.val.node_tag == "CaseExpr":
                        for result in item.val:
                            if result.parent_attribute == "defresult":
                                for field in result.fields:
                                    key = field.string_value
                                    keys.append(key)
        prefix = "update" + " " + table + " " + str(keys)

        white_list = config.sql_whitelist["sql_redundant"]["update"]
        if prefix not in white_list and prefix is not None:
            prefixes.append(prefix)

    @classmethod
    def sql_redundant(cls, sql_node, way, prefixes):
        tables = sql_node.relation
        prefix = None
        if sql_node.relation.node_tag == "RangeVar":
            table = tables.relname.value
            prefix = way + " " + table

        white_list = config.sql_whitelist["sql_redundant"][way]
        if prefix not in white_list and prefix is not None:
            prefixes.append(prefix)

    @classmethod
    def select_redundant(cls, items, prefixes):
        target = False
        select_from_tables = []
        where_condition = []
        targetList = items.targetList
        fromClause = items.fromClause       # Tables
        whereClause = items.whereClause     # Where
        limitCount = items.limitCount       # Limit
        sortClause = items.sortClause       # Group by
        limitOffset = items.limitOffset     # Offset
        lockingClause = items.lockingClause     # For update

        if targetList:
            for tar in targetList:
                if tar.name:
                    if tar.name.value == "__count":
                        target = True

        for tables in fromClause:
            SQLRedundant._select_from_table(tables, select_from_tables)

        if whereClause:
            SQLRedundant._select_where(whereClause, where_condition)

        if sortClause:
            for sorts in sortClause:
                SQLRedundant._select_sort(sorts, where_condition)

        if limitCount:
            if limitCount.node_tag == "A_Const":
                limit = "limit:" + str(limitCount.val.ival.value)
                where_condition.append(limit)

        if limitOffset:
            if limitOffset.node_tag == "A_Const":
                offset = "offset:" + str(limitOffset.val.ival.value)
                where_condition.append(offset)

        if lockingClause:
            where_condition.append("locking")

        if len(select_from_tables) == 0:
            return

        table = select_from_tables[0]
        select_from_tables.pop(0)

        if table not in config.table_whitelist:
            if target:
                prefix = "select * " + table + " " + str(select_from_tables) + " " + str(where_condition)
            else:
                prefix = "select " + table + " " + str(select_from_tables) + " " + str(where_condition)

            # new_str = prefix.split(" ", 2)      #   get 'select' table  others
            white_list = config.sql_whitelist["sql_redundant"]["select"]
            if prefix not in white_list:
                prefixes.append(prefix)

    @classmethod
    def _select_from_table(cls, data, tables):
        if data.node_tag == "RangeVar":
            # From table name
            from_table = data.relname.value
            tables.append(from_table)
        if data.node_tag == "RangeSubselect":   # 目前只取了as的值
            from_table = data.alias.aliasname.value
            tables.append(from_table)
        if data.node_tag == "JoinExpr":
            SQLRedundant._select_from_join(data.parse_tree, tables)

    @classmethod
    def _select_from_join(cls, data, from_join_table):
        # After the SQL parsing, multiple layers are embedded and loop check is required
        for k, v in data.items():
            if k == "relname":
                from_join_table.append(v)
            if k == "jointype" and int(v) == 0:
                if "RangeVar" in data["larg"].keys():
                    join_table1 = data["larg"]["RangeVar"]["relname"]
                    from_join_table.append(join_table1)
                if "JoinExpr" in data["larg"].keys() and "jointype" in data["larg"]["JoinExpr"]["larg"]:
                    join_table1 = data["larg"]["JoinExpr"]["larg"]["RangeVar"]["relname"]
                    from_join_table.append(join_table1)

            if k == "larg" and "JoinExpr" in v.keys():
                SQLRedundant._select_from_join(v["JoinExpr"], from_join_table)

            if k == "rarg":
                join_table2 = v["RangeVar"]["relname"]
                from_join_table.append(join_table2)

    @classmethod
    def _select_where(cls, whereClause, where_condition):
        where_or = []
        if whereClause.node_tag == "A_Expr":
            SQLRedundant._select_where_expr(whereClause, where_condition)

        if whereClause.node_tag == "BoolExpr":
            if whereClause.boolop.value == 0:
                SQLRedundant._select_where_bool(whereClause, where_condition)
            if whereClause.boolop.value == 1:
                SQLRedundant._select_where_bool(whereClause, where_or)
                where_condition.append(where_or)

    @classmethod
    def _select_where_bool(cls, whereClause, where):
        where_or = []
        for item in whereClause.args:
            if item.node_tag == "A_Expr":
                SQLRedundant._select_where_expr(item, where)
            if item.node_tag == "BoolExpr":
                if item.boolop.value == int(1):
                    SQLRedundant._select_where_bool(item, where_or)
                    where.append(where_or)
                    where_or = []

    @classmethod
    def _select_where_expr(cls, item, where):
        k_v = []

        # Key.vlaue
        for k in item.lexpr.fields:
            for v in k:
                k_v.append(v.value)

        # Where key.vlaue condition
        for name in item.name:
            for v in name:
                k_v.append(v.value)

        key_value = ".".join(k_v)
        where.append(key_value) \

    @classmethod
    def _select_sort(cls, item, where):
        k_v = []

        # key.vlaue
        for k in item.node.fields:
            for v in k:
                k_v.append(v.value)

        key_value = ".".join(k_v)
        sort = "sort:" + key_value
        where.append(sort)
