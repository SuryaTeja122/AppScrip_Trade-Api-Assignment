import requests

def analyze_data(sector, data):
    API_KEY = "AIzaSyCn7bNZatp3a6ZG1wDXg17NaP4dO4kA3QU"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    prompt = f"""
    Analyze the {sector} sector in India and return response in this format:

    ## Market Trends
    - ...

    ## Opportunities
    - ...

    ## Risks
    - ...
    """

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        result = response.json()
        print(result)  # debug

        text = result["candidates"][0]["content"]["parts"][0]["text"]

        return {"raw": text}

    except Exception as e:
        print("ERROR:", e)
        return {"raw": f"Fallback analysis for {sector} sector"}