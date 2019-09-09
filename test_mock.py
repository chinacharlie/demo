import requests
import unittest
from unittest import mock

#自定义异常
class myException(Exception):
    pass

#判断python.org是否是python网站，用到来requests.get
def is_python_site():
    try:
        r  = requests.get('http://python.org')
    except IOError:
        pass
    else:
        if r.status_code == 200:
            return 'Python' in r.content
    raise myException('error happened')


#mock来模拟一个http返回
def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code = status_code
    m.content = content

    def fake_get(url):
        return m
    
    return fake_get

class TestPython(unittest.TestCase):
    #构造一个mock，代替requests.get的返回
    @mock.patch('requests.get', get_fake_get(200, 'Python is language'))
    def test_python(self):
        self.assertTrue(is_python_site())

    #构造一个mock，代替requests.get的返回，这次假设返回404
    @mock.patch('requests.get', get_fake_get(404, ''))
    def test_404(self):
        self.assertRaises(myException, is_python_site)


t = TestPython()
t.test_python()
t.test_404()