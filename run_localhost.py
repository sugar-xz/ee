#!/usr/bin/env python3
import os
import sys
import yaml
from yaml import full_load
from tavern.core import run

from api_tests import TEST_BASE_DIR

# assert 'API_TEST_SERVER' in os.environ, 'Require environment `API_TEST_SERVER`'


def case_file(config_path):
    with open(config_path, encoding='utf-8') as file_obj:
        cont = file_obj.read()
        data = yaml.full_load(cont)
        return data


def file_name(cases):
    test_file = []
    file_dir = os.path.join(TEST_BASE_DIR, 'API_list')
    for case_name in cases:
        for root, dirs, files in os.walk(file_dir):
            # print('root_dir:', root)  # 当前目录路径
            # print('sub_dirs:', dirs)  # 当前路径下所有子目录
            # print('files:', files)  # 当前路径下所有非目录子文件
            if case_name in dirs:
                case_path = os.path.join(root, case_name)
                if cases[case_name] == 'default':
                    file_path = os.path.join(case_path, 'test_default.tavern.yaml')
                else:
                    file_path = os.path.join(case_path, ('test_' + str(cases[case_name]) + '.tavern.yaml'))
                test_file.append(file_path)
    print(test_file)
    return test_file

if __name__ == '__main__':
    # if len(sys.argv)<2:
    #     print('Error: need config file!\nExit')
    #     exit(1)
    # print(sys.argv)
    # config_path = sys.argv[1]
    #
    # data = case_file(config_path)
    data = case_file('config.yml')
    versions = data['db_version']
    file = data['api_case']

    test_files = file_name(file)
    # os.system('rm report.log')
    # sys.stdout = open('report.log', 'w')
    # rst = []
    # for test_file in test_files:
    #     et = run(test_file, tavern_global_cfg={"tavern-beta-new-traceback": True}, pytest_args=['-v', '--tb=short', '--disable-warnings', '--capture=sys'])
    #     rst.append(int(et))
    #     #rst.append(os.system(f'tavern-ci {test_file} -v --disable-warnings >> report.log'))
    # print(rst)
    # exit(max(rst))


    import datetime
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(nowTime)
    rst = []
    errors = []
    for test_file in test_files:
        et = run(test_file, tavern_global_cfg={"tavern-beta-new-traceback": True},
                 pytest_args=['-v', '--tb=short', '--disable-warnings', '--capture=sys'])
        print("eeeeeeeeeeeeet:==================",et)
        rst.append(et)
        if int(et) != 0:
            errors.append(test_file)
        # rst.append(os.system(f'tavern-ci {test_file} -v --disable-warnings >> report.log'))
    if len(errors) != 0:
        print('\n' + 'errors:%s' % errors + '\n')
    print(rst)

    nowTime1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(nowTime1)
