from pathlib import Path

import pytest
from pytest_bdd import given, parsers, scenarios, then, when


@pytest.fixture(scope="session")
def splinter_webdriver():
    """Override splinter webdriver name."""
    return "remote"


@pytest.fixture(scope="session")
@given("remoteのurlを指定", target_fixture="splinter_remote_url")
def splinter_remote_url():
    return "http://selenium:4444/wd/hub"


@pytest.fixture
def path():
    return Path.cwd() / "tests" / "screenshot"


@given(parsers.parse("urlを設定:\n{url}"), target_fixture="url")
def url(url):
    return url


@when("ページを開く")
def open_browser(browser, url):
    browser.visit(url)


@when(parsers.parse("スクリーンショットを撮る:\n{file_name}"))
def screenshot(browser, path, file_name):
    browser.screenshot(str(path / file_name), full=True)
