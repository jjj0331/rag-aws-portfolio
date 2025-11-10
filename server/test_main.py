
# server/test_main.py
from fastapi.testclient import TestClient

# 1. main.pyから 'app' をimportしようと試みる
# (まだ 'app' は存在しないので、これがエラーの原因になる)
from server.main import app

# 2. テスト用のクライアントを作成
client = TestClient(app)

def test_post_query_success():
    """
    POST /api/v1/query が設計書通りに成功するかテストする
    """

    # 3. Day 2で設計した通りのリクエストを投げる
    response = client.post("/api/v1/query", 
                       json={"query_text": "テスト質問"})

    data = response.json()

    # 4. Day 2で設計した通りのレスポンスを期待する (アサーション)
    assert response.status_code == 200
    assert "answer" in data
    assert "sources" in data
    assert "annotations" in data