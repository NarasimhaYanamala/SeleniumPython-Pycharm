import pytest


# @pytest.fixture()
# def setup():
#     print("Once before every method")
#
# def testMethod(setup):
#     print("this is test method1")
#
# def testMethod2():
#     print("this is test method2")


@pytest.fixture()
## it will execute each and every method BEFORE and AFTER
def setup():
    print("Once before every method")
    yield
    print("--once after every method--")

def testMethod11(setup):
    print("this is test method1")

def testMethod21(setup):
    print("this is test method2")