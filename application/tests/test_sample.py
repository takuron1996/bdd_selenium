"""サンプルのテストコード"""

import pytest
from pytest_bdd import given, parsers, scenario, then, when

from bdd_selenium.sample import Sample


@scenario("features/sample.feature", "サンプルコードのテスト")
def test_sample():
    pass


@given(parsers.parse("{text} で初期化"), target_fixture="sample")
def sample(text):
    return Sample(text)


@pytest.fixture
@when("run関数を実行")
def run(sample):
    return sample.get_text()


@then(parsers.parse("{text} が返ってくる"))
def check_result(run, text):
    assert run == text
