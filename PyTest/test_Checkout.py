import pytest



def tc_setup():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close Browser")