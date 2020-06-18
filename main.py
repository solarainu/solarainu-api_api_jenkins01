import pytest
import allure

pytest.main(['-s','-v',r'./test_case/test_postman_api.py','--alluredir=./allure-results'])
