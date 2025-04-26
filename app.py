from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 加上CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Movie Search API running!"}

@app.get("/movies")
def get_movies():
    # 你的電影資料
    return [
        {"title": "電影1", "release_date": "2025-04-26", "info": "描述...", "poster_path": "/abcd.jpg"},
        {"title": "電影2", "release_date": "2025-04-28", "info": "描述...", "poster_path": "/efgh.jpg"},
    ]

# backend/app.py
from fastapi import FastAPI
import requests
from typing import List

app = FastAPI()

API_KEY = "dd805c7ad21f99a62cbcc7a446b16be5"  

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
                "release_date": movie.get("release_date", ""),
                "info": movie.get("overview", ""),
                "poster_path": movie.get("poster_path")  # << 加這行
            })

        return movies
    
    except Exception as e:
        print(f"❗ 錯誤發生：{e}")
        return []

