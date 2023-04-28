Feature: Web Browserの操作
    Scenario Outline: ブラウザでGoogleを開いてみるテスト
        Given Googleのurlを設定
        When ページを開く
        And グーグルのスクリーンショットの保存場所を設定
        And スクリーンショットを撮る
        Then titleを検証

    Scenario Outline: ブラウザでアイフルのホームページを開いてみるテスト
        Given アイフルのurlを設定
        When ページを開く
        And アイフルのスクリーンショットの保存場所を設定
        And スクリーンショットを撮る
