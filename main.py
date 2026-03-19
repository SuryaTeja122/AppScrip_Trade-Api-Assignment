from fastapi import FastAPI
from routes.analyze import router
from slowapi.middleware import SlowAPIMiddleware

# ✅ ADD THIS IMPORT
from core.rate_limiter import limiter
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

# ✅ VERY IMPORTANT
app.state.limiter = limiter

# ✅ Exception handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )

app.add_middleware(SlowAPIMiddleware)

app.include_router(router)