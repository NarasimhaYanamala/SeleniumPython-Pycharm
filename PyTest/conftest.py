# import pytest
# import smtplib
#
#
# @pytest.fixture()
# def tc_setup(browser):
#     if browser == "chrome":
#         print("Launch Chrome")
#     elif browser == 'edge':
#         print("Launch Edge")
#     else:
#         print("Launch valid Browser")
#     print("Login")
#     print("Browse Products")
#     yield
#     print("Logoff")
#     print("Close Browser")
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store")
#
# ## This will return the Browser value to setup method
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
