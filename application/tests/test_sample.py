"""サンプルのテストコード"""

import pytest
from pytest_bdd import given, scenario, then, when

from bdd_selenium.sample import Sample


@scenario("features/sample.feature", "サンプルコードのテスト")
def test_sample():
    pass


@pytest.fixture
@given("「HelloWorld」で初期化")
def sample():
    return Sample("HelloWorld")


@pytest.fixture
@when("run関数を実行")
def run(sample):
    return sample.get_text()


@then("「HelloWorld」が返ってくる")
def check_result(run):
    assert run == "HelloWorld"
