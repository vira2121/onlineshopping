import pytest
@pytest.fixture()
def setUp():
    print("open amazon app")
    print("User logged in")
    yield
    print("logged out")
    print("closed amazon app")



def test_checkout(setUp):
    print("payment successful")
