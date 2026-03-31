import asyncio
import psutil
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def get():
    # This serves the HTML file when you visit http://localhost:8000
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 1. Collect the data
            cpu = psutil.cpu_percent(interval=None)
            ram = psutil.virtual_memory().percent
            
            # 2. Package it as JSON
            data = {"cpu": cpu, "ram": ram}
            
            # 3. Push it to the browser
            await websocket.send_json(data)
            
            # 4. Wait 1 second before the next update
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Connection closed: {e}")