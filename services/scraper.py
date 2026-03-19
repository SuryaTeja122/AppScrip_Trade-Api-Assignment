import requests

def get_market_data(sector: str):
    try:
        url = f"https://api.duckduckgo.com/?q={sector}+India+market&format=json"
        response = requests.get(url)
        return response.json()
    except:
        return {"data": f"No live data found for {sector}"}