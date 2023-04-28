Feature: Web Browserの操作
    Scenario Outline: ブラウザでGoogleを開いてみるテスト
        Given urlを設定:
            http://google.com
        When ページを開く
        And スクリーンショットを撮る:
            google
        Then titleを検証

    Scenario Outline: ブラウザでアイフルのホームページを開いてみるテスト
        Given urlを設定:
            https://www.aiful.co.jp/
        When ページを開く
        And スクリーンショットを撮る:
            aiful
