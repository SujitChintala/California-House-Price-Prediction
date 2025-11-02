# 🎬 YouTube Video Recommendation System

A comprehensive video recommendation system that analyzes YouTube trending videos from multiple countries (CA, GB, IN, US) and provides intelligent content-based recommendations using machine learning.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Data Analysis](#data-analysis)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project provides a complete pipeline for YouTube video analysis and recommendations:

1. **Data Collection**: Merges YouTube trending video datasets from 4 countries
2. **Data Analysis**: Comprehensive exploratory data analysis with visualizations
3. **Recommendation Engine**: Content-based filtering using TF-IDF and cosine similarity
4. **Web Interface**: Clean, intuitive frontend for searching and discovering videos
5. **REST API**: Flask-based backend for serving recommendations

## ✨ Features

### 🔍 Recommendation System
- **Content-Based Filtering**: Analyzes video titles, tags, descriptions, and channels
- **Similarity Scoring**: Uses TF-IDF vectorization and cosine similarity
- **Multiple Search Options**: Search by video ID, title, or keywords
- **Popularity Ranking**: Considers views, likes, and engagement metrics

### 📊 Data Analysis & Visualization
- **Comprehensive Statistics**: Total views, likes, comments across all countries
- **Visual Insights**: 
  - View distribution analysis
  - Engagement metrics comparison
  - Country-wise performance charts
  - Category analysis
  - Publishing time patterns
  - Correlation heatmaps
  - Word clouds from titles
- **Interactive Notebook**: Jupyter notebook with all analyses and visualizations

### 🌐 Web Application
- **Clean UI**: Simple, modern interface with gradient design
- **Three Main Sections**:
  - Search & Recommendations
  - Trending Videos
  - Statistics Dashboard
- **Real-time Search**: Instant video search with autocomplete
- **Responsive Design**: Works on desktop and mobile devices

### 🚀 REST API
- **GET** `/api/recommendations/<video_id>` - Get similar videos
- **GET** `/api/trending` - Get trending videos (filterable by country)
- **GET** `/api/search` - Search videos by query
- **GET** `/api/video/<video_id>` - Get video details
- **GET** `/api/stats` - Get dataset statistics

## 📁 Project Structure

```
YouTube-Recommendation-System/
│
├── data/                          # Data directory
│   ├── CAvideos.csv              # Canada videos
│   ├── GBvideos.csv              # Great Britain videos
│   ├── INvideos.csv              # India videos
│   ├── USvideos.csv              # United States videos
│   └── merged_youtube_data.csv   # Merged dataset
│
├── frontend/                      # Frontend application
│   └── index.html                # Main web interface
│
├── app.py                        # Flask backend server
├── recommendation_system.py      # Recommendation engine
├── merge_data.py                 # Data merging script
├── youtube_analysis.ipynb        # Analysis notebook
├── requirements.txt              # Python dependencies
├── README.md                     # Main documentation
└── SETUP.md                      # Setup instructions
```

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for REST API
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning library
  - TfidfVectorizer for text analysis
  - Cosine similarity for recommendations

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with gradients and animations
- **JavaScript**: Interactivity and API calls
- **Responsive Design**: Mobile-friendly layout

### Data Analysis
- **Jupyter Notebook**: Interactive analysis environment
- **Matplotlib**: Statistical visualizations
- **Seaborn**: Advanced statistical graphics
- **WordCloud**: Text visualization

## 💻 Installation

See [SETUP.md](SETUP.md) for detailed installation instructions.

Quick start:

```bash
# Clone the repository
git clone https://github.com/yourusername/youtube-recommendation-system.git
cd youtube-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Merge data files
python merge_data.py

# Start the server
python app.py
```

## 🎮 Usage

### 1. Start the Backend Server

```bash
python app.py
```

The server will start at `http://localhost:5000`

### 2. Open the Web Interface

Open your browser and navigate to:
```
http://localhost:5000
```

### 3. Use the Application

**Search for Videos:**
1. Enter keywords in the search box
2. Click "Search" to find matching videos
3. Select a video from the dropdown
4. Click "Get Recommendations" to see similar videos

**Browse Trending:**
1. Switch to the "Trending" tab
2. Optionally filter by country
3. Click "Load Trending" to see popular videos

**View Statistics:**
1. Switch to the "Statistics" tab
2. View total videos, views, likes, and comments

### 4. Run the Analysis Notebook

```bash
jupyter notebook youtube_analysis.ipynb
```

The notebook contains:
- Data loading and merging
- Exploratory data analysis
- Comprehensive visualizations
- Recommendation system implementation
- Interactive widgets

## 📚 API Documentation

### Get Recommendations

```http
GET /api/recommendations/<video_id>?n=10
```

**Parameters:**
- `video_id` (path): YouTube video ID
- `n` (query, optional): Number of recommendations (default: 10)

**Response:**
```json
{
  "success": true,
  "recommendations": [
    {
      "video_id": "abc123",
      "title": "Video Title",
      "channel_title": "Channel Name",
      "views": 1000000,
      "likes": 50000,
      "dislikes": 500,
      "comment_count": 10000,
      "category_id": 10,
      "country": "US",
      "thumbnail": "https://...",
      "similarity_score": 0.85
    }
  ]
}
```

### Get Trending Videos

```http
GET /api/trending?country=US&n=20
```

**Parameters:**
- `country` (query, optional): Country code (CA, GB, IN, US)
- `n` (query, optional): Number of videos (default: 20)

### Search Videos

```http
GET /api/search?q=music&n=20
```

**Parameters:**
- `q` (query, required): Search query
- `n` (query, optional): Number of results (default: 20)

### Get Video Details

```http
GET /api/video/<video_id>
```

Returns complete details for a specific video.

### Get Statistics

```http
GET /api/stats
```

Returns dataset statistics including total videos, views, likes, and country distribution.

## 📊 Data Analysis

The project includes comprehensive data analysis covering:

### Dataset Overview
- **Total Videos**: 158,098 unique videos
- **Countries**: CA, GB, IN, US
- **Time Period**: 2017-2018 trending data
- **Features**: 17 columns including views, likes, comments, tags, descriptions

### Key Insights
1. **View Distribution**: Highly skewed with few viral videos
2. **Engagement Patterns**: Strong correlation between likes and views
3. **Category Performance**: Music and Entertainment dominate
4. **Publishing Patterns**: Peak activity during specific hours
5. **Country Differences**: Varying content preferences across regions

### Visualizations Include
- Distribution plots for views, likes, and engagement
- Scatter plots showing metric correlations
- Bar charts for country and category comparisons
- Time-series analysis of publishing patterns
- Heatmaps for correlation analysis
- Word clouds from video titles and tags

## 🔬 How It Works

### Recommendation Algorithm

The system uses **Content-Based Filtering** with the following steps:

1. **Feature Extraction**:
   - Combines title, tags, channel name, and description
   - Creates a text corpus for each video

2. **TF-IDF Vectorization**:
   - Converts text to numerical vectors
   - Uses bi-grams (1-2 word combinations)
   - Removes common English stop words
   - Limits to top 5000 features

3. **Similarity Calculation**:
   - Computes cosine similarity between vectors
   - Finds videos with similar content profiles
   - Ranks by similarity score

4. **Ranking & Filtering**:
   - Considers popularity scores
   - Excludes the source video
   - Returns top N recommendations

### Engagement Score

```python
engagement_score = (likes + comments × 2 - dislikes) / (views + 1)
```

### Popularity Score

```python
popularity_score = log(views) × 0.4 + log(likes) × 0.3 + log(comments) × 0.3
```

## 📸 Screenshots

### Main Interface
The clean, gradient-styled interface with tabs for different features.

### Search & Recommendations
Search for videos and get intelligent recommendations based on content similarity.

### Trending Videos
Browse trending videos filtered by country.

### Statistics Dashboard
View comprehensive statistics about the dataset.

### Jupyter Notebook Analysis
Interactive data analysis with beautiful visualizations.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Add more recommendation algorithms (collaborative filtering, hybrid)
- Improve frontend UI/UX
- Add video player integration
- Implement user preferences and history
- Add more data visualization options
- Optimize performance for larger datasets

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- YouTube trending data from [Kaggle](https://www.kaggle.com/)
- Icons from various open-source libraries
- Inspired by modern recommendation systems

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ for data science and machine learning enthusiasts**
