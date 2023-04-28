from pytest_bdd import given, parsers, scenarios, then, when

scenarios("features/browser.feature")


@then("titleを検証")
def check_title(browser):
    assert browser.title == "Google"
