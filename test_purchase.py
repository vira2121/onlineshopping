import pytest
@pytest.fixture()
def setUp():
    print("setup started")
    yield
    print("exited")

def test_AddItemtoCart(setUp):
    print("added successfully")

def test_RemoveItemfromCart(setUp):
    print("remove successfully")



