from fastapi import APIRouter, HTTPException, Depends, Request
from services.scraper import get_market_data
from services.ai_service import analyze_data
from services.report import generate_markdown
from core.auth import verify_api_key
from core.rate_limiter import limiter

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,   # ✅ ADD THIS
    sector: str,
    api_key: str = Depends(verify_api_key)
):
    try:
        data = get_market_data(sector)
        analysis = analyze_data(sector, data)
        report = generate_markdown(sector, analysis)

        return {"report": report}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))