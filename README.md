# PythonAQA

pip install flake8 pytest pytest-cov requests
pip freeze > requirements.txt
autopep8 -a -i filename.py
flake8 --max-line-length 150 --statistics
pytest -v --cov

pip install allure-pytest
py.test --alluredir=allure-results 
D:\Tools\allure\2.8.1\bin\allure serve allure-results