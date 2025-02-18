import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records")

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def fake_data():
    a = str(fake.random_int(min=1, max=100))
    b = str(fake.random_int(min=1, max=100))
    operation = fake.random_element(elements=['add', 'subtract', 'multiply', 'divide'])
    return a, b, operation
