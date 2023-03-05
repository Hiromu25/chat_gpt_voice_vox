# このプロジェクトについて

このプロジェクトでは、ChatGPTとVOICEVOXを用いてずんだもんと会話ができます。

あなたが入力した内容に応じて、ChatGPTが返答を作成し、VOICEVOXが読み上げます。

※音声再生までタイムラグがあるためご了承ください。

# 準備

[ ] [poetry](https://python-poetry.org/)のインストール

[ ] [OpenAI API Key](https://platform.openai.com/docs/introduction/overview)の取得　　

[ ] [VOICEVOX](https://voicevox.hiroshiba.jp/)のダウンロード　　

[ ] .envファイルの作成（.env_exampleを参照）　　

# 実行方法

0. VOICEVOXの起動
1. poetry install
2. poetry run python src/main.py
