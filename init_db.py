import os
import sys
import yaml

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Error: need config file!')
        print('Usage: \n /path/to/config.yml')
        exit(1)
    config_path = sys.argv[1]
    if not os.path.exists(config_path):
        print('config file not exist')
        exit(1)

    data=yaml.load(open(config_path).read())
    db_type = data['db_version']

    sql_dir = os.path.join('/data/tavern/api_tests/sql_init/', db_type)
    sql_files = os.listdir(sql_dir)
    sql_files.sort()
    for fname in sql_files:
        sql_path = os.path.join(sql_dir, fname)
        os.system(f'PGPASSWORD=123456 psql -h websitedb -p 5432 -U postgres -f {sql_path}')

