// client/app/page.tsx
// 1. Next.jsに、このファイルが「ブラウザ側で動く」ことを教えます
"use client"; 

// 2. Reactの 'useState' をimportします（ボタンクリックの検知などに使えます）
import { useState } from 'react';

export default function Home() {

  // APIからの応答を保存するための「状態（State）」
  const [apiResponse, setApiResponse] = useState("");

  // 3. APIを「叩く」ための関数を定義します
  const handleApiCall = async () => {
    try {
      console.log("APIを呼び出します...");
      setApiResponse("ローディング中...");

      const response = await fetch(
        // ▼▼▼ 【重要】あなたのAPI（Backend）のURL ▼▼▼
        'http://127.0.0.1:8000/api/v1/query', 
        {
          method: 'POST', // Day 2の設計書通り、POSTメソッド
          headers: {
            'Content-Type': 'application/json',
          },
          // Day 2の設計書通りのJSONデータを送る
          body: JSON.stringify({
            query_text: "G検定について教えて" 
          }),
        }
      );

      const data = await response.json();
      console.log("APIからの応答:", data);
      
      // 成功したら、ダミー回答を画面に表示
      setApiResponse(data.answer); 

    } catch (error) {
      console.error("API呼び出しエラー:", error);
      // ▼▼▼ おそらく、ここに来ます ▼▼▼
      setApiResponse("エラーが発生しました。コンソールを確認してください。");
    }
  };

  return (
    <main style={{ padding: '2rem' }}>
      <h1>G検定 学習アプリ (RAG)</h1>
      
      {/* 4. このボタンがAPIを「叩く」引き金（トリガー）です */}
      <button onClick={handleApiCall}>
        APIを叩く (テスト)
      </button>

      {/* 5. APIからの応答をここに表示します */}
      <div>
        <h2>APIの回答:</h2>
        <p>{apiResponse}</p>
      </div>
    </main>
  );
}