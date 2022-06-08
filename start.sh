#!/bin/sh
python init_db.py ./config.yml
python run_api_test.py ./config.yml http://apiserver:8080
