from pathlib import Path

from pytest_bdd import given, parsers, scenarios, then, when

scenarios("features/browser.feature")


@given("Googleのurlを設定", target_fixture="url")
def google_url():
    return "http://google.com"


@given("アイフルのurlを設定", target_fixture="url")
def aiful_url():
    return "https://www.aiful.co.jp/"


@when("ページを開く")
def open_browser(browser, url):
    browser.visit(url)


@when("グーグルのスクリーンショットの保存場所を設定", target_fixture="path")
def google_path():
    return str(Path.cwd() / "google.png")


@when("アイフルのスクリーンショットの保存場所を設定", target_fixture="path")
def aiful_path():
    return str(Path.cwd() / "aiful.png")


@when("スクリーンショットを撮る")
def screenshot(browser, path):
    browser.screenshot(path, full=True)


@then("titleを検証")
def check_title(browser):
    assert browser.title == "Google"
