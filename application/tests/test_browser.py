from pathlib import Path

from pytest_bdd import given, scenarios, then, when

scenarios("features/browser.feature")


@given("Googleのurlを設定", target_fixture="url")
def google_url():
    return "http://google.com"


@given("アイフルのurlを設定", target_fixture="url")
def aiful_url():
    return "https://www.aiful.co.jp/cashing/ld2/?aff=11052631&utm_source=google&utm_medium=cpc&utm_campaign=LS_A&dclid=CL6S9_CEhfECFfzDFgUd_PEJdA&&&&&B23982656.303468037;dc_trk_aid=495914084;dc_trk_cid=130809203;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=&gad=1&gclid=CjwKCAjwuqiiBhBtEiwATgvixA4vLZzSS2TxlnaiaHT8yZCYBfrwqseCujJ79aLEBsxOzQSeJzP-axoC-u4QAvD_BwE&gclsrc=aw.ds"


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
