# LambdaでメッセージをSlackに送信

LambdaのSlack通知関連を自分なりに調べていたので、簡単なものをメモとして。

  - Cloudwatchと連携させて何かをトリガーに通知することを前提としています。
  - 以下の行を修正してください。

    ・SlackのWebHook
    SLACK_POST_URL = 'WEB HOOK URLを記載'
    ・メッセージタイトル
    SLACK_MESSAGE_TITLE = 'Something happened'
    ・最下部 message関数のresult
    result = "Something occurred. Please escalate to the information system team."
