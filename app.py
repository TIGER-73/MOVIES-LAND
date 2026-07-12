import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="TopCinema", page_icon="🎬", layout="wide")

# 2. Advanced CSS to replicate the Dark Premium Grid UI
st.markdown(
    """
    <style>
    /* Global Background and Fonts */
    .stApp {
        background-color: #0b0c10;
        color: #ffffff;
    }
    
    /* Top Header Navbar Branding */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        border-bottom: 2px solid #1f2833;
        margin-bottom: 25px;
    }
    .logo-text {
        color: #ff3333;
        font-size: 2.2rem;
        font-weight: 900;
        font-family: 'Arial Black', sans-serif;
        letter-spacing: -1px;
    }
    .logo-text span {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: normal;
        margin-left: 5px;
    }
    
    /* Section Headers */
    .section-header {
        border-left: 4px solid #ff3333;
        padding-left: 10px;
        font-size: 1.4rem;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 15px;
        color: #ffffff;
    }
    
    /* Custom style for Streamlit buttons to look like clickable movie cards */
    div.stButton > button {
        background-color: #15161e !important;
        color: #ffffff !important;
        border: 1px solid #222531 !important;
        width: 100%;
        text-align: center;
        padding: 10px !important;
        font-size: 0.9rem !important;
        font-weight: bold !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        border-radius: 0px 0px 8px 8px !important;
    }
    div.stButton > button:hover {
        border: 1px solid #ff3333 !important;
        color: #ff3333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Top Navigation Bar Implementation
st.markdown(
    """
    <div class="nav-container">
        <div class="logo-text">TopCinema<span>توب سينما</span></div>
        <div style="color: #888888; font-size: 0.9rem;">Welcome to TopCinema - Premium Free Movie Streaming Platform</div>
    </div>
    """, 
    unsafe_allow_html=True
)

# 4. Movie Data Setup (Only Movies, Numbered Structure)
if 'video_db' not in st.session_state:
    st.session_state.video_db = [
        {"id": "m1", "title": "Movie 1", "category": "Featured", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+1", "url": "https://archive.org/download/sample_video_file/video1.mp4"},
        {"id": "m2", "title": "Movie 2", "category": "Featured", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+2", "url": "https://archive.org/download/sample_video_file/video2.mp4"},
        {"id": "m3", "title": "Movie 3", "category": "Featured", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+3", "url": "https://archive.org/download/sample_video_file/video3.mp4"},
        {"id": "m4", "title": "Movie 4", "category": "Featured", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+4", "url": "https://archive.org/download/sample_video_file/video1.mp4"},
        {"id": "m5", "title": "Movie 5", "category": "Featured", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+5", "url": "https://archive.org/download/sample_video_file/video2.mp4"},
        
        {"id": "m6", "title": "Movie 6", "category": "Latest", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+6", "url": "https://archive.org/download/sample_video_file/video3.mp4"},
        {"id": "m7", "title": "Movie 7", "category": "Latest", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+7", "url": "https://archive.org/download/sample_video_file/video1.mp4"},
        {"id": "m8", "title": "Movie 8", "category": "Latest", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+8", "url": "https://archive.org/download/sample_video_file/video2.mp4"},
        {"id": "m9", "title": "Movie 9", "category": "Latest", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+9", "url": "https://archive.org/download/sample_video_file/video3.mp4"},
        {"id": "m10", "title": "Movie 10", "category": "Latest", "poster": "https://placehold.co/300x450/15161e/ffffff?text=Movie+10", "url": "https://archive.org/download/sample_video_file/video1.mp4"}
    ]

if 'active_video' not in st.session_state:
    st.session_state.active_video = st.session_state.video_db[0]

# 5. Media Player Layout
player_col1, player_col2 = st.columns([3, 1])

with player_col1:
    st.video(st.session_state.active_video["url"])
with player_col2:
    st.subheader(st.session_state.active_video["title"])
    st.info("Streaming source verified: Archive.org High Speed Cluster.")

st.markdown("---")

# 6. ROW 1: Premium Featured Movies (Horizontal 5-Column Grid Layout)
st.markdown('<div class="section-header">🔥 FEATURED MOVIES (المضاف حديثاً)</div>', unsafe_allow_html=True)
featured_items = [v for v in st.session_state.video_db if v["category"] == "Featured"]
feat_cols = st.columns(5)

for idx, movie in enumerate(featured_items):
    with feat_cols[idx]:
        st.image(movie["poster"], use_container_width=True)
        if st.button(movie["title"], key=f"feat_{movie['id']}"):
            st.session_state.active_video = movie
            st.rerun()

# 7. ROW 2: Latest Movies (Horizontal 5-Column Grid Layout)
st.markdown('<div class="section-header">🎬 LATEST ADDED MOVIES (أحدث الأفلام)</div>', unsafe_allow_html=True)
latest_items = [v for v in st.session_state.video_db if v["category"] == "Latest"]
lat_cols = st.columns(5)

for idx, movie in enumerate(latest_items):
    with lat_cols[idx]:
        st.image(movie["poster"], use_container_width=True)
        if st.button(movie["title"], key=f"lat_{movie['id']}"):
            st.session_state.active_video = movie
            st.rerun()