Feature: Web Browserの操作
    Scenario Outline: ブラウザでGoogleを開いてみるテスト
        When ページを開く:
            http://google.com
        And スクリーンショットを撮る:
            google
        Then titleを検証

    Scenario Outline: ブラウザでアイフルのホームページを開いてみるテスト
        When ページを開く:
            https://www.aiful.co.jp/
        And スクリーンショットを撮る:
            aiful
