from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import secrets
import logging
from typing import Dict, Optional

# Basic logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("RionModsServer")

app = FastAPI(title="RION MODS Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for local dev
active_sessions: Dict[str, dict] = {}
pairing_codes: Dict[str, dict] = {}

class PairRequest(BaseModel):
    device_name: str

class PrankRequest(BaseModel):
    duration_seconds: int = 15

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "1.0.0"}

@app.post("/pair/create")
def create_pairing(req: PairRequest):
    code = secrets.token_hex(4).upper()
    pairing_codes[code] = {"device_name": req.device_name, "status": "pending"}
    logger.info(f"Created pairing code for {req.device_name}")
    return {"pairing_code": code, "expires_in": 300}

@app.post("/pair/approve")
def approve_pairing(code: str):
    if code not in pairing_codes:
        raise HTTPException(status_code=404, detail="Invalid or expired code")
    session_token = secrets.token_urlsafe(32)
    device = pairing_codes.pop(code)
    active_sessions[session_token] = {"device_name": device["device_name"], "status": "active", "prank_active": False}
    logger.info(f"Approved pairing for {device['device_name']}")
    return {"session_token": session_token, "status": "approved"}

@app.get("/sessions")
def get_sessions():
    return {"sessions": active_sessions}

@app.post("/session/{token}/prank")
def start_prank(token: str, req: PrankRequest):
    if token not in active_sessions:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if req.duration_seconds > 60:
        raise HTTPException(status_code=400, detail="Duration too long")
    
    active_sessions[token]["prank_active"] = True
    active_sessions[token]["prank_duration"] = req.duration_seconds
    logger.info(f"Started prank on session {token} for {req.duration_seconds}s")
    return {"status": "prank_started", "duration": req.duration_seconds}

@app.post("/session/{token}/restore")
def restore_prank(token: str):
    if token not in active_sessions:
        raise HTTPException(status_code=401, detail="Unauthorized")
    active_sessions[token]["prank_active"] = False
    logger.info(f"Restored session {token}")
    return {"status": "restored"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
