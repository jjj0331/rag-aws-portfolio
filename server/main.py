# server/main.py

from fastapi import FastAPI
# POSTからの送信のバリデーション検証のメソッドをインポート
from pydantic import BaseModel

# CROSチェックのメソットをインポート
from fastapi.middleware.cors import CORSMiddleware # 1. CORSミドルウェアをimport

app = FastAPI()

# 2. CORSミドルウェアを追加する (ここが最重要)
origins = [
    "http://localhost:3000", # あなたのReact(Next.js)が動いている住所
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # この「オリジン（住所）」からの通信を許可する
    allow_credentials=True,
    allow_methods=["*"], # すべてのメソッド (GET, POST, OPTIONSなど) を許可
    allow_headers=["*"], # すべてのヘッダーを許可
)


# --- (以下はDay 4で書いたコード) ---

class QueryRequest(BaseModel):
    query_text: str

@app.post("/api/v1/query")
async def post_query(request: QueryRequest):
    
    return {
        "answer": f"「{request.query_text}」へのダミー回答です", 
        "sources": [
            {"document_name": "dummy.pdf", "page": 1}
        ],
        "annotations": [
            {"word": "ダミー", "definition": "ハリボテのことです"}
        ]
    }