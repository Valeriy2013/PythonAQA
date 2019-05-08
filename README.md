# PythonAQA

Master branch:
[![CircleCI](https://circleci.com/gh/Valeriy2013/PythonAQA/tree/master.svg?style=svg)](https://circleci.com/gh/Valeriy2013/PythonAQA/tree/master)


Prerequisites:
pip install flake8 pytest pytest-cov requests
pip freeze > requirements.txt
autopep8 -a -i filename.py
flake8 --max-line-length 150 --statistics
pytest -v --cov

pip install allure-pytest
py.test --alluredir=allure-results 
path_to_allure serve allure-results

Tags:
- ui
- api
