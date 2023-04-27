# featureファイルのサンプル

Feature: Sample
    Scenario Outline: サンプルコードのテスト
        Given <text> で初期化
        When run関数を実行
        Then <text> が返ってくる
    
    Examples:
        | text |
        | HelloWorld |
        | 111 |
