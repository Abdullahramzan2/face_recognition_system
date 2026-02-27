# 🎭 Face Recognition System

Face Recognition Using Python, OpenCV, and DeepFace.

---

## 📁 Project Structure

```
face_recognition_system/
├── app.py            # Main entry point
├── config.py         # Settings
├── register.py       # Register users via webcam
├── recognize.py      # Real-time recognition
├── utils.py          # Logging
├── requirements.txt
├── database/faces/   # Auto-created — stores face images
└── logs/app.log      # Auto-created — activity logs
```

---

## 🚀 Setup

### 1. Clone & Navigate
```bash
git clone https://github.com/Abdullahramzan2/face_recognition_system.git
cd face_recognition_system
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### 3. Activate Virtual Environment
```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```
> You'll see `(venv)` in your terminal when active.

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run
```bash
python app.py
```

---

## 🧑‍💻 Usage

| Option | Action |
|---|---|
| `1` | Register a user — press `S` to save photos, `Q` when done |
| `2` | Start recognition — green box = known, red = unknown |
| `3` | Exit |

> 💡 Save 8–10 photos per user from different angles for best accuracy.

---

## ⚙️ Configuration

Edit `config.py` to change behaviour:

| Setting | Default | Description |
|---|---|---|
| `MODEL_NAME` | `Facenet` | Recognition model |
| `DETECTOR_BACKEND` | `opencv` | Face detector |
| `DISTANCE_THRESHOLD` | `0.6` | Match strictness |
| `MAX_PHOTOS_PER_USER` | `10` | Max photos per user |

---

## 🛑 Deactivate Environment

```bash
deactivate
```

---

## 🐛 Common Issues

- **Camera not opening** — close other apps using the webcam
- **Slow recognition** — use `MODEL_NAME = "Facenet"` and `DETECTOR_BACKEND = "opencv"`
- **Too many unknowns** — register more photos or raise `DISTANCE_THRESHOLD` slightly
- **ModuleNotFoundError** — make sure `(venv)` is active, then re-run `pip install -r requirements.txt`
