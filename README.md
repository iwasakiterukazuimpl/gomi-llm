# 📦 gomi-llm_local
このプロジェクトは、text.jsonファイルからテキスト情報を読み取り、ローカルで動作する大規模言語モデル「Ollama」を用いてゴミ分別に関する質問応答を行うPythonアプリケーションです。仮想環境で動作確認済みです。

---

## 🔧 主な機能
text.jsonからデータを読み込み

OllamaローカルLLMとの対話

ゴミの種類や出し方に関する自然言語応答

コマンドラインから簡単に実行可能

---

## 📁 ディレクトリ構成
```bash
.
├── gomi-llm_local.py      # メインスクリプト
├── text.json              # ゴミ分別情報（例：札幌市のデータ）
├── README.md              # このファイル
└── requirements.text      # Python仮想環境（推奨）
```

---

## 🛠️ セットアップ手順
仮想環境の作成と有効化（例：venv使用）

```bash
python3 -m venv venv
source venv/bin/activate

# Windowsの場合は venv\Scripts\activate
```

依存ライブラリのインストール

```bash
pip install -r requirements.txt
```

Ollamaのインストールとモデルの準備

```bash
# Ollamaのインストール（詳細は https://ollama.com/ を参照）
brew install ollama

ollama run mistral
```

スクリプトの実行

```bash
python gomi-llm_local.py
```

---

## 📘 使用例
```bash
ユーザー: 牛乳パックは何ごみ？
AI: それは「紙パックごみ」です。洗ってから資源ごみの日に出してください。
```

---

## 📝 text.jsonの例
```json
[
  {
    "name": "牛乳パック",
    "category": "紙パック",
    "note": "洗って資源ごみとして出す"
  }
]
```
（※実際の形式に合わせて調整可能です）

--

## 🧠 使用しているLLM
Ollama（例：LLaMA3、Mistralなど）

完全ローカル環境で動作

プライバシー重視 & 高速応答

--

## 🗒 補足事項
モデルのカスタマイズやtext.jsonの拡張により、他の地域のゴミ出し情報にも対応可能です。

--

## 📄 ライセンス
MIT License（変更可能）