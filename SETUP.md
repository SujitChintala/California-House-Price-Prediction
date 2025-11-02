# 🚀 Setup Guide - YouTube Video Recommendation System

This guide will walk you through setting up and running the YouTube Video Recommendation System on your local machine.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
  - Download from [python.org](https://www.python.org/downloads/)
  - Verify installation: `python --version`

- **pip** (Python package manager)
  - Usually comes with Python
  - Verify installation: `pip --version`

- **Git** (optional, for cloning)
  - Download from [git-scm.com](https://git-scm.com/)

- **Web Browser**
  - Chrome, Firefox, Edge, or Safari (latest version)

## 📥 Installation Steps

### Step 1: Get the Project Files

**Option A: Clone with Git**
```bash
git clone https://github.com/yourusername/youtube-recommendation-system.git
cd youtube-recommendation-system
```

**Option B: Download ZIP**
1. Download the project as ZIP
2. Extract to your desired location
3. Open terminal/command prompt in that directory

### Step 2: Create a Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt after activation.

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (cross-origin support)
- pandas (data manipulation)
- numpy (numerical operations)
- scikit-learn (machine learning)
- matplotlib (plotting)
- seaborn (statistical visualizations)
- wordcloud (text visualization)
- jupyter (notebook environment)
- ipywidgets (interactive widgets)

**Installation time**: 2-5 minutes depending on your internet speed.

### Step 4: Verify Data Files

Make sure you have the following CSV files in the `data/` directory:
- `CAvideos.csv`
- `GBvideos.csv`
- `INvideos.csv`
- `USvideos.csv`

### Step 5: Merge the Data Files

```bash
python merge_data.py
```

**Expected output:**
```
Reading CSV files...
Merging datasets...
Merged data saved to data/merged_youtube_data.csv
Total rows: 158,098
Total columns: 17

Dataset breakdown:
CA videos: 40,881
GB videos: 38,916
IN videos: 37,352
US videos: 40,949
```

This creates `data/merged_youtube_data.csv` which will be used by the recommendation system.

## 🎮 Running the Application

### Method 1: Web Application (Recommended)

1. **Start the Flask server:**

```bash
python app.py
```

**Expected output:**
```
Initializing recommendation system...
Loading data...
Preprocessing data...
Building recommendation model...
Model built with 158098 videos
Recommendation system ready!
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

2. **Open your web browser and navigate to:**
```
http://localhost:5000
```

3. **Use the application:**
   - Search for videos by keywords
   - Get recommendations for similar videos
   - Browse trending videos by country
   - View dataset statistics

4. **Stop the server:**
   - Press `Ctrl + C` in the terminal

### Method 2: Jupyter Notebook

1. **Start Jupyter Notebook:**

```bash
jupyter notebook
```

This will open Jupyter in your default browser.

2. **Open the analysis notebook:**
   - Click on `youtube_analysis.ipynb`

3. **Run the notebook:**
   - Click "Cell" → "Run All" to execute all cells
   - Or run cells individually with `Shift + Enter`

4. **Explore the analysis:**
   - View data statistics
   - See visualizations
   - Test the recommendation system
   - Use interactive widgets

### Method 3: Python Script

You can also use the recommendation system directly in Python:

```python
from recommendation_system import YouTubeRecommendationSystem

# Initialize the system
recommender = YouTubeRecommendationSystem()

# Get recommendations for a video
recommendations = recommender.get_recommendations(
    video_id='2Vv-BfVoq4g',  # Example: Ed Sheeran - Perfect
    n_recommendations=10
)

# Get trending videos
trending = recommender.get_trending_videos(country='US', n_videos=20)

# Search for videos
results = recommender.search_videos('music', n_results=10)
```

## 🔧 Configuration

### Changing the Port

By default, the Flask server runs on port 5000. To change it:

**Edit `app.py`:**
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)  # Change 5000 to your preferred port
```

**Update frontend:**
Edit `frontend/index.html` and change:
```javascript
const API_URL = 'http://localhost:8080/api';  // Match your port
```

### Adjusting Recommendation Parameters

**Edit `recommendation_system.py`:**

```python
# Change number of TF-IDF features
self.tfidf = TfidfVectorizer(
    max_features=5000,  # Increase for more features (slower but potentially better)
    stop_words='english',
    ngram_range=(1, 2),  # Change to (1, 3) for trigrams
    min_df=2
)

# Modify popularity score weights
self.df['popularity_score'] = (
    np.log1p(self.df['views']) * 0.4 +      # Adjust weights
    np.log1p(self.df['likes']) * 0.3 +
    np.log1p(self.df['comment_count']) * 0.3
)
```

## 📊 Dataset Information

### Data Schema

Each video record contains:
- `video_id`: Unique YouTube video identifier
- `trending_date`: Date when video was trending
- `title`: Video title
- `channel_title`: Channel name
- `category_id`: Category identifier
- `publish_time`: Publication timestamp
- `tags`: Video tags (pipe-separated)
- `views`: View count
- `likes`: Like count
- `dislikes`: Dislike count
- `comment_count`: Comment count
- `thumbnail_link`: Thumbnail URL
- `comments_disabled`: Boolean flag
- `ratings_disabled`: Boolean flag
- `video_error_or_removed`: Boolean flag
- `description`: Video description
- `country`: Country code (added during merge)

### Data Size

- **Total Videos**: ~158,000 unique videos
- **File Size**: ~50-60 MB merged
- **Memory Usage**: ~300-400 MB when loaded
- **Processing Time**: 10-30 seconds for initial load

## 🐛 Troubleshooting

### Common Issues

#### 1. "Module not found" Error

**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

Make sure your virtual environment is activated.

#### 2. "Port already in use" Error

**Solution:**
- Kill the process using port 5000, or
- Change the port in `app.py` (see Configuration section)

**Windows:**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
lsof -ti:5000 | xargs kill -9
```

#### 3. Frontend Can't Connect to Backend

**Check:**
1. Is the Flask server running?
2. Is the correct URL in `frontend/index.html`?
3. Are there CORS errors? (Should be handled by Flask-CORS)

**Solution:**
- Restart the Flask server
- Clear browser cache
- Check browser console for errors (F12)

#### 4. "File not found" Error for CSV Files

**Solution:**
- Ensure all 4 CSV files are in the `data/` directory
- Run `merge_data.py` to create the merged file
- Check file paths are correct

#### 5. Memory Error with Large Dataset

**Solution:**
- Close other applications
- Use a machine with more RAM
- Reduce `max_features` in TF-IDF vectorizer
- Process data in chunks

#### 6. Jupyter Notebook Won't Start

**Solution:**
```bash
pip install --upgrade jupyter notebook
jupyter notebook --generate-config
```

### Performance Optimization

For faster recommendations:

1. **Reduce TF-IDF features:**
```python
max_features=3000  # Instead of 5000
```

2. **Limit dataset size:**
```python
# In recommendation_system.py, after loading data:
self.df = self.df.sample(n=50000, random_state=42)  # Use 50K samples
```

3. **Pre-compute similarity matrix:**
```python
# Warning: High memory usage
self.similarity_matrix = cosine_similarity(self.tfidf_matrix)
```

## 🔒 Security Notes

- This is a local development setup
- Do not expose to the internet without proper security
- API has no authentication (add if deploying)
- CORS is enabled for all origins (restrict for production)

## 📱 Browser Compatibility

Tested and working on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Edge 90+
- ✅ Safari 14+

## 💡 Tips

1. **First Run**: The initial load takes 10-30 seconds to build the recommendation model
2. **Search Tips**: Use specific keywords for better search results
3. **Recommendations**: More popular videos tend to have better recommendations
4. **Notebook**: Run cells in order for best results
5. **Visualizations**: Some plots may take a few seconds to render

## 📚 Next Steps

After setup:

1. **Explore the notebook** to understand the data
2. **Try the web interface** for recommendations
3. **Experiment with parameters** in the code
4. **Add your own features** and improvements
5. **Read the API documentation** in README.md

## 🆘 Getting Help

If you encounter issues:

1. Check this SETUP.md file
2. Review error messages carefully
3. Check the README.md for API documentation
4. Open an issue on GitHub with:
   - Error message
   - Steps to reproduce
   - Your Python version
   - Your operating system

## 🎉 Success!

If everything is working:
- ✅ Flask server is running
- ✅ Web interface loads
- ✅ Can search for videos
- ✅ Recommendations are displayed
- ✅ Jupyter notebook runs

**You're ready to explore YouTube video recommendations!**

---

**Need help?** Open an issue on GitHub or check the README.md for more information.
