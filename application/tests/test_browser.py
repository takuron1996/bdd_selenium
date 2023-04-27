import pytest
from pytest_bdd import given, scenarios, then, when

# scenarios("features/browser.feature")


# @given("chromeブラウザを開く")
# def open_browser(browser):
#     browser.visit("http://google.com")


# @then("titleを検証")
# def title(browser):
#     assert browser.title == "Example Domain"


@pytest.fixture(scope="session")
def splinter_webdriver():
    """Override splinter webdriver name."""
    return "remote"


@pytest.fixture(scope="session")
def splinter_remote_url():
    return "http://selenium:4444/wd/hub"


def test_browser(browser):
    browser.visit("http://google.com")
    assert browser.title == "Google"
