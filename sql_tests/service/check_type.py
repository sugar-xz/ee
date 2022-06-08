from sql_tests.config import config
from sql_tests.service.check_err import CheckError
from sql_tests.service.sql_redundant import SQLRedundant
from pglast import Node, parse_sql, prettify


class CheckType:

    @classmethod
    def each_parse(cls, data):
        i = 0
        sql_errors = []
        sql_warning = []
        prefixes = []
        for sql in data:
            # Beautify the SQL
            # print("Check sql : ", prettify(sql))
            print("Check sql : %s" % sql)

            # SQL node
            sql_node = Node(parse_sql(sql))
            check_err = CheckType._sql_check(sql, sql_node, prefixes)

            if len(check_err) != 0:
                sql_errors.extend(check_err)

        for item in prefixes:
            if prefixes.count(item) > 1:
                redundant_err = CheckError.sql_error(item, error_type="sql_redundant")
                redundant_err["sql_redundant"] = prefixes.count(item)
                if redundant_err not in sql_warning:    # 新增sql_warning 显示 sql_redundant
                    sql_warning.append(redundant_err)

            i += 1
        return sql_errors, i, sql_warning

    @classmethod
    def _sql_check(cls, sql, sql_node, prefixes):
        sql_err = []
        # sql_syntax = sql_node[0].stmt.node_tag
        for param in sql_node:
            for stmt in param:
                sql_syntax = stmt.node_tag

                if sql_syntax == "SelectStmt":
                    sql_err = CheckType._sql_select_range(sql, stmt)
                    SQLRedundant.select_redundant(stmt, prefixes)

                elif sql_syntax == "UpdateStmt":  # need set check
                    sql_err = CheckType._sql_update_delete_range(sql, stmt, "sql_update_range")
                    SQLRedundant.update_redundant(stmt, prefixes)

                elif sql_syntax == "InsertStmt":
                    SQLRedundant.sql_redundant(stmt, "insert", prefixes)

                elif sql_syntax == "DeleteStmt":
                    sql_err = CheckType._sql_update_delete_range(sql, stmt, "sql_delete_range")
                    SQLRedundant.sql_redundant(stmt, "delete", prefixes)

                else:
                    print("The unknown SQL!!!")

        return sql_err

    @classmethod
    def sql_num_check(cls, url, request_type, number, sql_data):
        # SQL too much
        sql_err = []
        sql_max_number = int(config.sql_max_number)
        sql_white = config.sql_whitelist["sql_much"]["endpoint"]
        for point in sql_white:
            if " " in point:
                port_type = point.split(" ")[0]
                port_url = point.split(" ")[1]

                if url == port_url and request_type == port_type:
                    sql_max_number = config.sql_whitelist["sql_much"]["sql_max_number"]

            if number >= sql_max_number:
                err = CheckError.sql_error(sql_data, error_type="sql_much")
                err["sql_number"] = number
                sql_err.append(err)
        return sql_err

    @classmethod
    def _sql_select_range(cls, sql, sql_node):
        sql_err = []
        fromClause = sql_node.fromClause
        whereClause = sql_node.whereClause
        limitCount = sql_node.limitCount
        if not whereClause and not limitCount:  # limit value check ?
            for fromSub in fromClause:
                if fromSub.node_tag == "RangeVar":
                    # From table name
                    sql_from_table = fromSub.relname.value

                    sql_table_black = config.table_blacklist
                    sql_white = config.sql_whitelist["sql_range"]["select"]

                    if sql_from_table in sql_table_black and sql not in sql_white:
                        err = CheckError.sql_error(sql, error_type="sql_black")
                        sql_err.append(err)

                if fromSub.node_tag == "RangeSubselect":
                    # 暂不处理复杂sql
                    pass
        return sql_err

    @classmethod
    def _sql_update_delete_range(cls, sql, sql_node, error_type):
        sql_err = []
        whereClause = sql_node.whereClause
        if not whereClause:
            errors = CheckError.sql_error(sql, error_type=error_type)
            sql_err.append(errors)
        return sql_err

    @classmethod
    def sql_repeat(cls, data, set_data):
        # Get the de-duplicated SQL
        sql_err = []
        for item in set_data:
            if data.count(item) > 1:
                if item not in config.sql_whitelist["sql_repeat"]["select"]:
                    # print("sql_count: %s  sql: %s" % (data.count(item), item))  # sql: number
                    err = CheckError.sql_error(item, error_type="sql_repeat")
                    err["repeat_number"] = data.count(item)
                    sql_err.append(err)
        return sql_err
