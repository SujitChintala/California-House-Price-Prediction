# Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SujitChintala/YouTube-Video-Recommendation-System.git
cd youtube-recommendation-system
```

### 2. Create Virtual Environment (Optional)

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Merge Data Files

Ensure CSV files (`CAvideos.csv`, `GBvideos.csv`, `INvideos.csv`, `USvideos.csv`) are in the `data/` directory, then run:

```bash
python merge_data.py
```

## Running the Application

### Web Application

```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000`

### Jupyter Notebook

```bash
jupyter notebook
```

Open `youtube_analysis.ipynb` in the browser.

### Python Script

```python
from recommendation_system import YouTubeRecommendationSystem

recommender = YouTubeRecommendationSystem()
recommendations = recommender.get_recommendations(video_id='2Vv-BfVoq4g', n_recommendations=10)
```

## Troubleshooting

**Module not found:**
```bash
pip install --upgrade -r requirements.txt
```

**Port already in use (Windows):**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Port already in use (macOS/Linux):**
```bash
lsof -ti:5000 | xargs kill -9
```
