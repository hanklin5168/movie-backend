# backend/app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import List
from dotenv import load_dotenv
import os

# ⚡️ 1. 創建app
app = FastAPI()

# ⚡️ 2. 在創建app之後立刻加CORS（一定要順序正確）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全部來源都允許（開發版）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚡️ 3. API邏輯
load_dotenv()  # 讀取.env檔案

API_KEY = os.getenv("TMDB_API_KEY")  # 你的TMDB金鑰

@app.get("/")
def root():
    return {"message": "Movie Search API running!"}

@app.get("/movies", response_model=List[dict])
def get_movies():
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=zh-TW&page=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        movies = []
        for movie in data.get("results", []):
            movies.append({
                "title": movie.get("title", ""),
                "original_title": movie.get("original_title", ""),
                "release_date": movie.get("release_date", ""),
                "overview": movie.get("overview", ""),
                "poster_path": movie.get("poster_path"),
                "vote_average": movie.get("vote_average", 0),
                "genre_ids": movie.get("genre_ids", [])
            })

        return movies

    except Exception as e:
        print(f"❗ 錯誤發生：{e}")
        return []
