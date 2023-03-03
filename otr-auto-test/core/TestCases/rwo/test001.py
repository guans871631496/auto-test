# ./conftest.py

import pytest

data = [
    {"url": "https://www.baidu.com", "http": "get"},
    {"url": "https://www.google.com", "http": "post"}
]

ids = ['get_baidu', 'post_google']


@pytest.fixture(scope='function', params=data, ids=ids)
def f_function(request):
    print("fixture部分-url:{}".format(request.param['url']))
    print("fixture部分-http:{}".format(request.param['http']))
    return request.param


# ./test_case/test_func.py
import pytest


def test_add_by_func_aaa(f_function):
    print("测试用例-url：{}".format(f_function['url']))
    print("测试用例-http：{}".format(f_function['http']))


# ./run_test.py
import pytest

if __name__ == '__main__':
    pytest.main(['-v', '-s'])

'''
============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-5.3.4, py-1.8.1, pluggy-0.13.1 -- D:\Python3.7\python.exe
cachedir: .pytest_cache
rootdir: D:\Python3.7\project\pytest, inifile: pytest.ini
plugins: allure-pytest-2.8.9, rerunfailures-8.0
collecting ... collected 2 items

test_case/test_func.py::test_add_by_func_aaa[get_baidu] fixture部分-url:https://www.baidu.com
fixture部分-http:get
测试用例-url：https://www.baidu.com
测试用例-http：get
PASSED
test_case/test_func.py::test_add_by_func_aaa[post_google] fixture部分-url:https://www.google.com
fixture部分-http:post
测试用例-url：https://www.google.com
测试用例-http：post
PASSED

============================== 2 passed in 0.04s ==============================
[Finished in 1.5s]
'''


