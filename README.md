# 🎬 Movie Search API (FastAPI + Docker)

本專案提供一個快速且簡單的電影查詢API，基於 FastAPI 框架開發，並支援 Docker 部署。

---

## 🚀 專案簡介

- 使用 [The Movie Database (TMDB)](https://www.themoviedb.org/) 公開API
- 快速取得現正上映電影資訊（片名、上映日期、簡介、海報）
- 支援跨來源請求（CORS），可直接串接前端網站
- 已部署於 [Render](https://render.com)

---

## 📚 技術棧

- Python 3.9
- FastAPI
- Docker
- Render 雲端部署

---

## 🛠 專案架構

```plaintext
├── app.py                 # FastAPI 主程式
├── requirements.txt       # 依賴套件
├── Dockerfile              # Docker 建置設定
└── README.md               # 專案說明文件
```

## 📦 快速啟動 (本地開發)

1. 安裝依賴套件
```bash
pip install -r requirements.txt
```
2. 啟動伺服器
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
3. 打開瀏覽器
API根目錄：http://localhost:8000/
取得電影資料：http://localhost:8000/movies

## 🐳 Docker 啟動方式
1. 建立 Docker Image
```bash
docker build -t movie-api .
```
2. 啟動 Docker Container
```bash
docker run -d -p 8000:8000 movie-api
```
## 🌐 已部署版本
API Endpoint: https://movie-backend-wlvm.onrender.com/movies

✨ 特別感謝
本專案使用了 TMDB 公開API，特此致謝。
本專案僅作為個人學習與展示用途，不用於任何商業行為。