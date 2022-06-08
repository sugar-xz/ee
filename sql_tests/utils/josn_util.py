import json
import os


class JsonUtil:
    # json affirm
    @classmethod
    def is_json(cls, json_data):
        try:
            new_json_data = JsonUtil.json_code(json_data)
            if new_json_data is None:
                print("File data not is json.")
            else:
                json.loads(new_json_data, encoding='utf-8')
        except ValueError:
            return False
        return True

    @classmethod
    def json_code(cls, json_data):
        try:
            data = json.dumps(json_data)
            return data
        except TypeError:
            return repr(TypeError)


class PathLog:

    @classmethod
    def read_log(cls, path=None):
        if path is None:
            path = PathLog._log_path()
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return data
        elif os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        else:
            print("Path is not exist!!")

    @classmethod
    def write_log(cls, data, path=None):
        try:
            if path is None:
                path = PathLog._log_path()
                if os.path.exists(path):
                    os.remove(path)
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False)
        except ValueError:
            print("Log writing fail!")
            print("The wrong reason is : ", ValueError)

    @classmethod
    def _log_path(cls):
        BASE_DIR = os.path.dirname(__file__)
        dir1 = "sql_tests"
        log_path = BASE_DIR[:BASE_DIR.index(dir1)] + "log/sql/sql_err.json"
        return log_path
