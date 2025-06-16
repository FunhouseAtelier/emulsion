# routes/api/demo/movie/route.py

from fastapi import APIRouter, Request, Query
from server.utils.envars import OMDB_API_KEY
import httpx

async def get_movie_data(request: Request):
    search = request.query_params.get("search", "").strip() or "inception"
    if not OMDB_API_KEY:
        return {"error": "OMDb API key not configured on server."}

    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={search}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        return {"error": "Failed to contact OMDb API."}

    data = response.json()

    if data.get("Response") == "False":
        return {"error": data.get("Error", "No results found.")}

    results = data.get("Search", [])[:10]  # Top 10 results

    # Clean up each result
    return {
        "results": [
            {
                "title": movie.get("Title"),
                "year": movie.get("Year"),
                "type": movie.get("Type"),
                "imdb_id": movie.get("imdbID"),
                "poster": movie.get("Poster"),
            }
            for movie in results
        ]
    }
