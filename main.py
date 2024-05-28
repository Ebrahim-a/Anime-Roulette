from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()


anime = Scraper()


@app.get("/{cat}")
async def read_item(cat):
    return anime.scrapedata(cat)

