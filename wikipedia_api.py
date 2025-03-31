from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/outline")
def get_wikipedia_outline(country: str = Query(..., description="Country name to fetch Wikipedia outline")):
    wiki_url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    
    try:
        response = requests.get(wiki_url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return JSONResponse(status_code=404, content={"error": "Wikipedia page not found"})

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract all headings (h1 to h6)
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    
    if not headings:
        return JSONResponse(status_code=404, content={"error": "No headings found"})

    # Generate Markdown Outline
    markdown_outline = "## Contents\n\n"
    
    for heading in headings:
        level = int(heading.name[1])  # h1 -> 1, h2 -> 2, ...
        markdown_outline += f"{'#' * level} {heading.text.strip()}\n\n"

    return {"country": country, "outline": markdown_outline.strip()}

