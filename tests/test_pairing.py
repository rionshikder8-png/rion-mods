import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../server')))
from rion_server.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "1.0.0"}

def test_pairing_flow():
    # Create
    res = client.post("/pair/create", json={"device_name": "TestDevice"})
    assert res.status_code == 200
    code = res.json()["pairing_code"]
    
    # Approve
    res2 = client.post(f"/pair/approve?code={code}")
    assert res2.status_code == 200
    token = res2.json()["session_token"]
    
    # Check sessions
    res3 = client.get("/sessions")
    assert token in res3.json()["sessions"]
    
    # Start prank
    res4 = client.post(f"/session/{token}/prank", json={"duration_seconds": 10})
    assert res4.status_code == 200
    assert res4.json()["status"] == "prank_started"

    # Restore
    res5 = client.post(f"/session/{token}/restore")
    assert res5.status_code == 200
    assert res5.json()["status"] == "restored"
