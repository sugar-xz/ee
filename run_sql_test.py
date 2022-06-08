#!/usr/bin/env python3
import sys
from sql_tests.service.check_sql import CheckSQL
from sql_tests.utils.josn_util import PathLog


def test(interface_sqls):
    try:
        # Get SQL log
        sql_log = PathLog.read_log(interface_sqls)

        # Parse SQL
        result, errors = CheckSQL().sql_check(sql_log)
    except Exception as e:
        result = 1
        errors = repr(e)
        print("SQL check error:", repr(e))
    return result, errors


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Error: need tavern SQL log file！！')
        print('Usage: \n /path/to/data.log')
        exit(1)
    interface_sql = sys.argv[1]

    test(interface_sql)
