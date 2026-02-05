from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI(title="AI Voice Detection API")

API_KEY = "123456"

class VoiceRequest(BaseModel):
    language: str
    audio_format: str
    audio_base64: str

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/detect")
async def detect_voice(
    request: VoiceRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    try:
        audio_bytes = base64.b64decode(request.audio_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid audio")

    result = {
        "language": request.language,
        "audio_format": request.audio_format,
        "audio_size": len(audio_bytes),
        "prediction": "Human voice",
        "confidence": 0.90
    }

    return result




