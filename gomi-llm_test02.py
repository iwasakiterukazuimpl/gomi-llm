from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

# 1. JSONファイルからテキストデータを読み込み
with open("text.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 2. Embeddingモデルの読み込みと変換
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(data["docs"])  # → (3, 384)のベクトル

# 3. FAISSインデックスの作成と保存
dimension = embeddings.shape[1]  # ベクトルの次元数（384）
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 4. 検索用のクエリを入力
query = "プラスチックゴミの出し方は？"
query_vec = model.encode([query])

# 5. FAISSでベクトル検索（最も近い1件を取得）
distances, indices = index.search(query_vec, k=1)  # k=1は上位1件

# 6. 結果を表示
print("🔍 クエリ:", query)
print("🧠 一番近い文:", data["docs"][indices[0][0]])
print("📏 距離スコア:", distances[0][0])