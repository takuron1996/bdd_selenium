import pytest
from pytest_bdd import given


@pytest.fixture(scope="session")
def splinter_webdriver():
    """Override splinter webdriver name."""
    return "remote"


@pytest.fixture(scope="session")
@given("remoteのurlを指定", target_fixture="splinter_remote_url")
def splinter_remote_url():
    return "http://selenium:4444/wd/hub"
