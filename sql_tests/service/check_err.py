from sql_tests.config import config


class CheckError:
    @classmethod
    def sql_error(cls, sql, error_type=""):

        err_sql = {'sql': sql, 'error_type': error_type}

        if error_type == "sql_repeat":
            err_sql['error_info'] = config.sql_repeat
        elif error_type == "sql_redundant":
            err_sql = {'prefix': sql, 'error_type': error_type, 'error_info': config.sql_redundant}
        elif error_type == "sql_black":
            err_sql['error_info'] = config.sql_black
        elif error_type == "sql_much":
            err_sql = {'error_type': error_type, 'error_info': config.sql_much}
        elif error_type == "sql_update_range":
            err_sql['error_info'] = config.sql_update_range
        elif error_type == "sql_delete_range":
            err_sql['error_info'] = config.sql_delete_range
        else:
            err_sql['error_info'] = ""

        return err_sql
