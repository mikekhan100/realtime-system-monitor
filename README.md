# Real-Time System Monitor 🚀

A high-performance hardware monitoring dashboard that streams live CPU and RAM metrics from a Python backend to a web-based frontend using WebSockets.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI
* **Real-time Engine:** WebSockets (Uvicorn Standard)
* **System Metrics:** `psutil`
* **Frontend:** HTML5, JavaScript, Chart.js

## ✨ Key Features
* **Bi-directional Communication:** Uses WebSockets instead of traditional HTTP polling for low-latency updates.
* **Live Visualisation:** Dynamic line charts that update every second without page refreshes.
* **Concurrency:** Built using Python's `asyncio` to handle multiple client connections efficiently.

## 🚀 How to Run
1. Clone the repo: `git clone <your-repo-link>`
2. Create a virtual environment: `python -m venv venv`
3. Activate venv: `.\venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Start the server: `uvicorn main:app --reload`
6. Visit `http://127.0.0.1:8000` in your browser.