from sql_tests.config import config
from sql_tests.service.check_type import CheckType


class CheckSQL:

    def __init__(self):
        self.err_data = []
        self.data_url = ""
        self.data_request_type = ""

    def sql_check(self, data_json):  # 每个sql校验是否会出问题
        # Each interface is handled separately
        for data in data_json:
            self.data_url = data['url']
            self.data_request_type = data['request_type']

            if self.data_url in config.interface_whitelist[self.data_request_type]:
                continue

            print('------------------------------start------------------------------')

            sql_data = data['sql']
            if len(sql_data) == 0:
                print("No sql!! Interface exception test data.  ", data)
                continue
            else:
                set_data = set(sql_data)

                # SQL check：sql repeat
                repeat_errors = CheckType.sql_repeat(sql_data, set_data)
                # SQL check：sql much and range and redundant
                check_errors, sql_num, sql_warning = CheckType.each_parse(set_data)
                # SQL check：sql max mumber
                num_check_errors = CheckType.sql_num_check(self.data_url, self.data_request_type, sql_num, sql_data)

                if len(repeat_errors) != 0:
                    check_errors.extend(repeat_errors)

                if len(num_check_errors) != 0:
                    check_errors.extend(num_check_errors)

            self._sql_all_err(sql_data, check_errors, sql_warning)

        # All sql error log
        print('\n----------------------------All error----------------------------')
        print("SQL check error: \n", self.err_data)

        for item in self.err_data:
            if "errors" in item.keys():
                return 1, self.err_data

        return 0, self.err_data

        # if len(self.err_data) == 0:
        #     return 0
        # else:
        #     return 1

    def _sql_all_err(self, all_sql, errors, warning):
        if len(errors) == 0 and len(warning) == 0:
            return self.err_data

        err_sql = {'url': self.data_url, 'type': self.data_request_type, 'all_sql': all_sql}
        if len(errors) != 0:
            err_sql["errors"] = errors
        if len(warning) != 0:
            err_sql["warning"] = warning

        if err_sql in self.err_data:    # Repeat
            return self.err_data

        for error in self.err_data:     # Repeat (Except for the sql)
            if self.data_url == error["url"] and self.data_request_type == error["type"]:
                if "warning" in error.keys() and "errors" in error.keys():
                    if errors == error["errors"] and warning == error["warning"]:
                        return self.err_data
                elif "warning" in error.keys() and "errors" not in error.keys():
                    if warning == error["warning"]:
                        return self.err_data
                elif "warning" not in error.keys() and "errors" in error.keys():
                    if errors == error["errors"]:
                        return self.err_data

        # Error interface information is returned
        self.err_data.append(err_sql)
        print("error-info : %s" % self.err_data)
