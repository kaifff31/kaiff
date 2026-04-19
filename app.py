import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ---------------- PAGE CONFIG ----------------
=======
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ================ PAGE CONFIG ================
st.set_page_config(
    page_title="Analytics Pro Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('[fonts.googleapis.com](https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap)');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Container */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Gradient Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
=======
# ================ PROFESSIONAL CSS ================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        font-family: 'Inter', sans-serif;
        st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
}
</style>
""", unsafe_allow_html=True)
    }
    
    /* ===== HEADER SECTION ===== */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 3rem 2.5rem;
        border-radius: 24px;
        margin-bottom: 2.5rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 500px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 50%;

    }
    
    .main-header h1 {
        color: white;

        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fc 100%);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.8);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    .metric-icon {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Glass Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        margin-bottom: 1.5rem;
    }
    
    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Custom Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #f1f5f9;
        padding: 8px;
        border-radius: 16px;
=======
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        font-family: 'Poppins', sans-serif;
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.95);
        font-size: 1.15rem;
        margin-top: 0.75rem;
        font-weight: 300;
        position: relative;
        z-index: 1;
    }
    
    /* ===== METRIC CARDS ===== */
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.8);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    .metric-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
    }
    
    .metric-icon {
        width: 60px;
        height: 60px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin-bottom: 1.2rem;
        font-weight: 600;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e293b;
        line-height: 1.2;
        font-family: 'Poppins', sans-serif;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #64748b;
        margin-top: 0.75rem;
        font-weight: 500;
        letter-spacing: 0.3px;
    }
    
    .metric-change {
        font-size: 0.85rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #e2e8f0;
        color: #10b981;
        font-weight: 600;
    }
    
    /* ===== GLASS CARD ===== */
    .glass-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 2rem;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-family: 'Poppins', sans-serif;
    }
    
    .card-title::before {
        content: '';
        display: inline-block;
        width: 4px;
        height: 24px;
        background: linear-gradient(180deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        padding: 12px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;

    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;

        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 500;
        color: #64748b;
    }
    
    .stTabs [aria-selected="true"] {
        background: white !important;
        color: #667eea !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* File Uploader */
    .stFileUploader {
        background: linear-gradient(145deg, #f8fafc 0%, #f1f5f9 100%);
        border: 2px dashed #cbd5e1;
        border-radius: 16px;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: #667eea;
        background: linear-gradient(145deg, #f0f4ff 0%, #e8edff 100%);
    }
    
    /* Buttons */
=======
        border-radius: 14px;
        padding: 14px 28px;
        font-weight: 600;
        color: #64748b;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
        border: 2px solid rgba(102, 126, 234, 0.5);
    }
    
    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;

        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
    }
    
    /* Select boxes */
=======
        padding: 0.85rem 2.2rem;
        font-weight: 700;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 32px rgba(102, 126, 234, 0.5);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.85rem 2.2rem;
        font-weight: 700;
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.4);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* ===== SELECT BOXES & INPUTS ===== */

    .stSelectbox > div > div {
        background: white;
        border-radius: 12px;
        border: 2px solid #e2e8f0;

    }
    
    /* Dataframe */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        padding: 2rem 1rem;
=======
        padding: 12px 14px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #667eea;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.15);
    }
    
    .stSlider > div {
        padding: 1.5rem 0;
    }
    
    .stSlider [role="slider"] {
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        border-right: 2px solid rgba(102, 126, 234, 0.2);

    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: rgba(255,255,255,0.8) !important;
    }
    
    /* Success/Info Messages */
    .stSuccess {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-radius: 12px;
        border-left: 4px solid #10b981;
=======
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-family: 'Poppins', sans-serif;
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: rgba(255, 255, 255, 0.85) !important;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] .stCheckbox label {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    
    /* ===== ALERTS ===== */
    .stSuccess {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-radius: 14px;
        border-left: 5px solid #10b981;
    }
    
    .stError {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-radius: 14px;
        border-left: 5px solid #ef4444;

    }
    
    .stInfo {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);

        border-radius: 12px;
        border-left: 4px solid #3b82f6;
    }
    
    /* Metrics in Streamlit */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #1a1a2e;
    }
    
    [data-testid="stMetricLabel"] {
        font-weight: 500;
        color: #64748b;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
=======
        border-radius: 14px;
        border-left: 5px solid #3b82f6;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-radius: 14px;
        border-left: 5px solid #f59e0b;
    }
    
    /* ===== DATAFRAME ===== */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }
    
    /* ===== METRICS ===== */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 800;
        color: #1e293b;
        font-family: 'Poppins', sans-serif;
    }
    
    [data-testid="stMetricLabel"] {
        font-weight: 600;
        color: #64748b;
    }
    
    /* ===== ANIMATIONS ===== */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }

    }
    
    .animate-fade {
        animation: fadeIn 0.6s ease-out forwards;
    }
    

    /* Plotly Charts Container */
    .chart-container {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h2 style="color: white; font-size: 1.5rem; margin-bottom: 0.5rem;">⚡ Control Panel</h2>
=======
    .animate-slide {
        animation: slideIn 0.6s ease-out forwards;
    }
    
    /* ===== CHART CONTAINER ===== */
    .chart-container {
        background: white;
        border-radius: 18px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.8);
        margin-bottom: 1.5rem;
    }
    
    /* ===== DIVIDER ===== */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
    
    /* ===== EMPTY STATE ===== */
    .empty-state {
        text-align: center;
        padding: 5rem 2rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
    }
    
    .empty-state-icon {
        font-size: 6rem;
        margin-bottom: 1.5rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    /* ===== INFO BOX ===== */
    .info-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        padding: 1.5rem;
        border-radius: 14px;
        border-left: 5px solid #f59e0b;
        box-shadow: 0 4px 16px rgba(245, 158, 11, 0.2);
    }
    
    .info-box h4 {
        color: #92400e;
        margin: 0 0 0.5rem 0;
        font-weight: 700;
        font-family: 'Poppins', sans-serif;
    }
    
    .info-box p {
        color: #78350f;
        margin: 0;
        font-size: 0.95rem;
    }
    
    /* ===== STAT BOX ===== */
    .stat-box {
        background: white;
        padding: 1.5rem;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    
    .stat-label {
        color: #64748b;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .stat-value {
        color: #667eea;
        font-size: 1.8rem;
        font-weight: 800;
        font-family: 'Poppins', sans-serif;
    }
    
    /* ===== HIDE STREAMLIT UI ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# ================ SIDEBAR ================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <h2 style="color: white; font-size: 1.8rem; margin-bottom: 0.5rem; font-family: 'Poppins', sans-serif; font-weight: 800;">⚡ Control Panel</h2>

        <p style="color: rgba(255,255,255,0.6); font-size: 0.9rem;">Configure your analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<p style="color: rgba(255,255,255,0.8); font-weight: 500; margin-bottom: 0.5rem;">📊 Chart Type</p>', unsafe_allow_html=True)
    chart_type = st.selectbox("Select Chart", ["Scatter", "Histogram", "Box", "Line", "Area"], label_visibility="collapsed")
    
    st.markdown("---")
    
    st.markdown('<p style="color: rgba(255,255,255,0.8); font-weight: 500; margin-bottom: 0.5rem;">🎨 Chart Theme</p>', unsafe_allow_html=True)
    chart_theme = st.selectbox("Theme", ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn"], label_visibility="collapsed")
    
    st.markdown("---")
    
    st.markdown('<p style="color: rgba(255,255,255,0.8); font-weight: 500; margin-bottom: 0.5rem;">📈 Show Trendline</p>', unsafe_allow_html=True)
    show_trendline = st.checkbox("Enable Trendline", value=False)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: rgba(255,255,255,0.5); font-size: 0.8rem;">
        <p>Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MAIN HEADER ----------------
st.markdown("""
<div class="main-header">
    <h1>📊 Analytics Pro Dashboard</h1>
    <p>Upload your data and unlock powerful insights with AI-driven analysis</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD SECTION ----------------
=======
    st.markdown("""
    <div style="height: 2px; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent); margin: 1.5rem 0;"></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p style="color: rgba(255,255,255,0.8); font-weight: 600; margin-bottom: 0.75rem; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">📊 Chart Type</p>', unsafe_allow_html=True)
    chart_type = st.selectbox("Select Chart", ["Scatter", "Histogram", "Box", "Line", "Area", "Violin"], label_visibility="collapsed")
    
    st.markdown("""<div style="height: 1px; background: rgba(255,255,255,0.1); margin: 1.5rem 0;"></div>""", unsafe_allow_html=True)
    
    st.markdown('<p style="color: rgba(255,255,255,0.8); font-weight: 600; margin-bottom: 0.75rem; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">🎨 Chart Theme</p>', unsafe_allow_html=True)
    chart_theme = st.selectbox("Theme", ["plotly_black", "plotly_dark", "plotly", "ggplot2"], label_visibility="collapsed")
    
    st.markdown("""<div style="height: 1px; background: rgba(255,255,255,0.1); margin: 1.5rem 0;"></div>""", unsafe_allow_html=True)
    
    st.markdown('<p style="color: rgba(255,255,255,0.8); font-weight: 600; margin-bottom: 0.75rem; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.5px;">📈 Options</p>', unsafe_allow_html=True)
    show_trendline = st.checkbox("Enable Trendline", value=False)
    show_stats = st.checkbox("Show Statistics", value=True)
    
    st.markdown("""<div style="height: 2px; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent); margin: 2rem 0;"></div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0; color: rgba(255,255,255,0.4); font-size: 0.8rem;">
        <p style="margin: 0;">📊 Analytics Pro v2.0</p>
        <p style="margin: 0.5rem 0 0 0;">Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# ================ MAIN HEADER ================
st.markdown("""
<div class="main-header">
    <h1>📊 Analytics Pro Dashboard</h1>
    <p>Transform Your Data Into Actionable Insights with Advanced Analytics & AI</p>
</div>
""", unsafe_allow_html=True)

# ================ FILE UPLOAD SECTION ================

st.markdown("""
<div class="glass-card">
    <div class="card-title">📁 Data Upload</div>
</div>
""", unsafe_allow_html=True)

col_upload, col_info = st.columns([2, 1])
=======
col_upload, col_info = st.columns([2.5, 1.5])


with col_upload:
    file = st.file_uploader("Drag and drop your CSV file here", type=["csv"], label_visibility="collapsed")

with col_info:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #f59e0b;">
        <p style="margin: 0; color: #92400e; font-weight: 500;">💡 Tip</p>
        <p style="margin: 0.5rem 0 0 0; color: #78350f; font-size: 0.9rem;">Upload a CSV file to start exploring your data with interactive visualizations and AI predictions.</p>
=======
    <div class="info-box">
        <h4>💡 Pro Tip</h4>
        <p>Upload a clean CSV file to unlock powerful visualizations, statistical analysis, and ML-powered predictions.</p>

    </div>
    """, unsafe_allow_html=True)

if file:
    df = pd.read_csv(file)

    # ---------------- DATA CLEANING ----------------
=======
    # ================ DATA CLEANING ================

    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)


    # ---------------- METRICS SECTION ----------------
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
=======
    # ================ METRICS SECTION ================
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4, gap="medium")

    
    with col1:
        st.markdown(f"""
        <div class="metric-card">

            <div class="metric-icon" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
=======
            <div class="metric-icon" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">

                📊
            </div>
            <div class="metric-value">{df.shape[0]:,}</div>
            <div class="metric-label">Total Rows</div>

=======
            <div class="metric-change">↑ Complete Dataset</div>
 
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">

            <div class="metric-icon" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
=======
            <div class="metric-icon" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white;">
 
                📋
            </div>
            <div class="metric-value">{df.shape[1]}</div>
            <div class="metric-label">Total Columns</div>

=======
            <div class="metric-change">↑ Features Available</div>
 
        </div>
        """, unsafe_allow_html=True)
    
    with col3:

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
                🔢
            </div>
            <div class="metric-value">{len(df.select_dtypes(include=np.number).columns)}</div>
            <div class="metric-label">Numeric Columns</div>
=======
        numeric_count = len(df.select_dtypes(include=np.number).columns)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white;">
                🔢
            </div>
            <div class="metric-value">{numeric_count}</div>
            <div class="metric-label">Numeric Columns</div>
            <div class="metric-change">↑ For Analysis</div>
 
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        missing = df.isnull().sum().sum()

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
=======
        missing_pct = (missing / (df.shape[0] * df.shape[1])) * 100
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white;">
 
                ⚠️
            </div>
            <div class="metric-value">{missing}</div>
            <div class="metric-label">Missing Values</div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- TABS ----------------
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Data Preview", "📊 Visualization", "🤖 AI Prediction", "📈 Statistics"])

    # ---------------- DATA TAB ----------------
=======
            <div class="metric-change">↓ {missing_pct:.1f}% Data</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)

    # ================ TABS ================
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Data Preview", "📊 Visualization", "🤖 AI Prediction", "📈 Statistics"])

    # ============ DATA TAB ============
 
    with tab1:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">🔍 Dataset Overview</div>
        </div>
        """, unsafe_allow_html=True)
        

        col_data1, col_data2 = st.columns([3, 1])
        
        with col_data1:
=======
        col_data1, col_data2 = st.columns([2.5, 1.5], gap="large")
        
        with col_data1:
            st.markdown('<p style="color: #64748b; font-weight: 600; margin-bottom: 1rem;">First 10 Rows</p>', unsafe_allow_html=True)
 
            st.dataframe(df.head(10), use_container_width=True, height=400)
        
        with col_data2:
            st.markdown("""

            <div style="background: white; padding: 1.5rem; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
                <h4 style="color: #1a1a2e; margin-bottom: 1rem;">📊 Column Types</h4>
            </div>
            """, unsafe_allow_html=True)
            
            for col in df.columns[:8]:
                dtype = str(df[col].dtype)
                color = "#667eea" if "int" in dtype or "float" in dtype else "#f59e0b"
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #e2e8f0;">
                    <span style="color: #374151; font-size: 0.85rem;">{col[:15]}...</span>
                    <span style="color: {color}; font-weight: 500; font-size: 0.85rem;">{dtype}</span>
                </div>
                """, unsafe_allow_html=True)

    # ---------------- VISUALIZATION TAB ----------------
=======
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 16px; color: white;">
                <h4 style="margin: 0 0 1.5rem 0; font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 1.1rem;">📊 Data Types</h4>
            </div>
            """, unsafe_allow_html=True)
            
            for col in df.columns[:10]:
                dtype = str(df[col].dtype)
                icon = "🔢" if "int" in dtype or "float" in dtype else "📝"
                color = "#667eea" if "int" in dtype or "float" in dtype else "#f59e0b"
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem; background: white; margin-bottom: 0.5rem; border-radius: 10px; border-left: 4px solid {color};">
                    <div>
                        <div style="color: #1e293b; font-weight: 600; font-size: 0.9rem;">{icon} {col[:20]}</div>
                        <div style="color: #94a3b8; font-size: 0.8rem;">{df[col].nunique()} unique</div>
                    </div>
                    <span style="background: {color}15; color: {color}; padding: 0.4rem 0.8rem; border-radius: 8px; font-weight: 600; font-size: 0.75rem;">{dtype.upper()}</span>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
        
        # Missing data visualization
        col_info1, col_info2 = st.columns(2)
        
        with col_info1:
            st.markdown("""
            <div class="glass-card">
                <div class="card-title">Missing Data Analysis</div>
            </div>
            """, unsafe_allow_html=True)
            
            missing_data = df.isnull().sum()
            missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
            
            if len(missing_data) > 0:
                fig_missing = px.bar(missing_data, orientation='h', template=chart_theme, 
                                    labels={'value': 'Count', 'index': 'Column'},
                                    title="Missing Values per Column",
                                    color=missing_data.values,
                                    color_continuous_scale='Reds')
                fig_missing.update_layout(height=300, showlegend=False)
                st.plotly_chart(fig_missing, use_container_width=True)
            else:
                st.success("✅ No missing values detected!")
        
        with col_info2:
            st.markdown("""
            <div class="glass-card">
                <div class="card-title">Data Quality Score</div>
            </div>
            """, unsafe_allow_html=True)
            
            quality_score = ((df.shape[0] * df.shape[1] - df.isnull().sum().sum()) / (df.shape[0] * df.shape[1])) * 100
            
            col_q1, col_q2 = st.columns(2)
            
            with col_q1:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-label">Quality Score</div>
                    <div class="stat-value">{quality_score:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_q2:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-label">Completeness</div>
                    <div class="stat-value">{100 - (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100):.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

    # ============ VISUALIZATION TAB ============
 
    with tab2:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">🎨 Interactive Visualization</div>
        </div>
        """, unsafe_allow_html=True)

        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

        if len(numeric_cols) > 0:

            col_viz1, col_viz2, col_viz3 = st.columns(3)
=======
            col_viz1, col_viz2, col_viz3 = st.columns(3, gap="medium")
 
            
            with col_viz1:
                x_col = st.selectbox("📍 X-Axis", numeric_cols, key="x_axis")
            
            with col_viz2:
                y_col = st.selectbox("📍 Y-Axis", numeric_cols, key="y_axis", index=min(1, len(numeric_cols)-1))
            
            with col_viz3:
                if categorical_cols:
                    color_col = st.selectbox("🎨 Color By", ["None"] + categorical_cols, key="color")
                else:
                    color_col = "None"


            # Create chart based on selection
            color_param = None if color_col == "None" else color_col
            
=======
            color_param = None if color_col == "None" else color_col
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Create chart
            if chart_type == "Scatter":
                if show_trendline:
                    fig = px.scatter(df, x=x_col, y=y_col, color=color_param, 
                                    trendline="ols", template=chart_theme,

                                    title=f"{y_col} vs {x_col}")
                else:
                    fig = px.scatter(df, x=x_col, y=y_col, color=color_param, 
                                    template=chart_theme, title=f"{y_col} vs {x_col}")
                    
            elif chart_type == "Histogram":
                fig = px.histogram(df, x=x_col, color=color_param, 
                                  template=chart_theme, title=f"Distribution of {x_col}",
                                  marginal="box")
                
            elif chart_type == "Box":
                fig = px.box(df, x=color_param, y=x_col, 
                            template=chart_theme, title=f"Box Plot of {x_col}")
                
            elif chart_type == "Line":
                fig = px.line(df, x=x_col, y=y_col, color=color_param,
                             template=chart_theme, title=f"{y_col} over {x_col}")
                
            elif chart_type == "Area":
                fig = px.area(df, x=x_col, y=y_col, color=color_param,
                             template=chart_theme, title=f"{y_col} over {x_col}")

            fig.update_layout(
                font_family="Inter",
                title_font_size=20,
                title_font_color="#1a1a2e",
                legend_title_font_color="#1a1a2e",
                height=500,
                margin=dict(l=20, r=20, t=60, b=20)
=======
                                    title=f"<b>{y_col} vs {x_col}</b>",
                                    hover_data=numeric_cols[:5])
                else:
                    fig = px.scatter(df, x=x_col, y=y_col, color=color_param, 
                                    template=chart_theme, title=f"<b>{y_col} vs {x_col}</b>",
                                    hover_data=numeric_cols[:5])
                    
            elif chart_type == "Histogram":
                fig = px.histogram(df, x=x_col, color=color_param, 
                                  template=chart_theme, title=f"<b>Distribution of {x_col}</b>",
                                  marginal="box", nbins=50)
                
            elif chart_type == "Box":
                fig = px.box(df, x=color_param, y=x_col, 
                            template=chart_theme, title=f"<b>Box Plot of {x_col}</b>")
                
            elif chart_type == "Line":
                fig = px.line(df, x=x_col, y=y_col, color=color_param,
                             template=chart_theme, title=f"<b>{y_col} over {x_col}</b>",
                             markers=True)
                
            elif chart_type == "Area":
                fig = px.area(df, x=x_col, y=y_col, color=color_param,
                             template=chart_theme, title=f"<b>{y_col} over {x_col}</b>")
            
            elif chart_type == "Violin":
                fig = px.violin(df, x=color_param, y=x_col,
                               template=chart_theme, title=f"<b>Violin Plot of {x_col}</b>",
                               box=True, points="outliers")

            fig.update_layout(
                font_family="Inter",
                title_font_size=22,
                title_font_color="#1e293b",
                title_font=dict(family="Poppins"),
                legend_title_font_color="#1e293b",
                height=550,
                margin=dict(l=20, r=20, t=80, b=20),
                hoverlabel=dict(bgcolor="white", font_size=12, font_family="Inter")
 
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Correlation heatmap

            st.markdown("<br>", unsafe_allow_html=True)
=======
            st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
            
 
            st.markdown("""
            <div class="glass-card">
                <div class="card-title">🔥 Correlation Heatmap</div>
            </div>
            """, unsafe_allow_html=True)
            
            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()
                fig_corr = px.imshow(corr_matrix, 

                                     text_auto=True, 
                                     aspect="auto",
                                     color_continuous_scale="RdBu_r",
                                     template=chart_theme)
                fig_corr.update_layout(height=400)
                st.plotly_chart(fig_corr, use_container_width=True)

    # ---------------- PREDICTION TAB ----------------
=======
                                     text_auto='.2f',
                                     aspect="auto",
                                     color_continuous_scale="RdBu_r",
                                     template=chart_theme,
                                     title="<b>Feature Correlation Matrix</b>")
                fig_corr.update_layout(
                    height=500,
                    title_font_size=20,
                    title_font_color="#1e293b",
                    font=dict(family="Inter")
                )
                st.plotly_chart(fig_corr, use_container_width=True)

    # ============ PREDICTION TAB ============
 
    with tab3:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">🤖 Machine Learning Prediction</div>
        </div>
        """, unsafe_allow_html=True)


        col_pred1, col_pred2 = st.columns([1, 2])
        
        with col_pred1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 16px; color: white;">
                <h4 style="margin: 0 0 1rem 0;">⚙️ Model Configuration</h4>
                <p style="font-size: 0.9rem; opacity: 0.9;">Configure your Random Forest model parameters below.</p>
=======
        col_pred1, col_pred2 = st.columns([1.2, 2.8], gap="large")
        
        with col_pred1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 16px; color: white;">
                <h4 style="margin: 0 0 1.5rem 0; font-family: 'Poppins', sans-serif; font-weight: 700; font-size: 1.1rem;">⚙️ Config</h4>
                <p style="font-size: 0.9rem; opacity: 0.9; margin: 0;">Random Forest Regressor</p>
 
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            

            target = st.selectbox("🎯 Select Target Variable", numeric_cols)
            
            n_estimators = st.slider("🌲 Number of Trees", 10, 200, 100)
            test_size = st.slider("📊 Test Size (%)", 10, 40, 20) / 100
=======
            target = st.selectbox("🎯 Target Variable", numeric_cols, key="target_var")
            
            st.markdown('<p style="color: #1e293b; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem;">Number of Trees</p>', unsafe_allow_html=True)
            n_estimators = st.slider("", 10, 200, 100, step=10, label_visibility="collapsed")
            
            st.markdown('<p style="color: #1e293b; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem;">Test Size</p>', unsafe_allow_html=True)
            test_size = st.slider("", 10, 40, 20, step=5, label_visibility="collapsed") / 100
            
            st.markdown("<br>", unsafe_allow_html=True)
 
            
            run_model = st.button("🚀 Train Model", use_container_width=True)
        
        with col_pred2:
            if run_model:
                with st.spinner("Training model..."):
                    df_encoded = pd.get_dummies(df)
                    
                    if target in df_encoded.columns:
                        X = df_encoded.drop(target, axis=1)
                        y = df_encoded[target]
                        
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
                        
                        model = RandomForestRegressor(n_estimators=n_estimators, random_state=42)
                        model.fit(X_train, y_train)
                        
                        pred = model.predict(X_test)
                        
                        r2 = r2_score(y_test, pred)
                        mae = mean_absolute_error(y_test, pred)
                        rmse = np.sqrt(mean_squared_error(y_test, pred))
                        
                        st.success("✅ Model trained successfully!")
                        
                        # Metrics display
                        met1, met2, met3 = st.columns(3)
                        
                        with met1:
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 1.5rem; border-radius: 16px; text-align: center; color: white;">
                                <div style="font-size: 2rem; font-weight: 700;">{r2:.3f}</div>
                                <div style="font-size: 0.9rem; opacity: 0.9;">R² Score</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with met2:
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 1.5rem; border-radius: 16px; text-align: center; color: white;">
                                <div style="font-size: 2rem; font-weight: 700;">{mae:.2f}</div>
                                <div style="font-size: 0.9rem; opacity: 0.9;">MAE</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with met3:
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); padding: 1.5rem; border-radius: 16px; text-align: center; color: white;">
                                <div style="font-size: 2rem; font-weight: 700;">{rmse:.2f}</div>
                                <div style="font-size: 0.9rem; opacity: 0.9;">RMSE</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.markdown("<br>", unsafe_allow_html=True)
                        
                        # Feature importance
                        importance_df = pd.DataFrame({
                            'Feature': X.columns,
                            'Importance': model.feature_importances_
                        }).sort_values('Importance', ascending=True).tail(10)
                        
                        fig_importance = px.bar(importance_df, x='Importance', y='Feature',
                                               orientation='h', template=chart_theme,
                                               title="🎯 Top 10 Feature Importance",
                                               color='Importance',
                                               color_continuous_scale='Viridis')
                        fig_importance.update_layout(height=400)
                        st.plotly_chart(fig_importance, use_container_width=True)
                        
                        # Actual vs Predicted
                        fig_pred = px.scatter(x=y_test, y=pred, template=chart_theme,
                                             labels={'x': 'Actual', 'y': 'Predicted'},
                                             title="📊 Actual vs Predicted Values")
                        fig_pred.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], 
                                                      y=[y_test.min(), y_test.max()],
                                                      mode='lines', name='Perfect Prediction',
                                                      line=dict(dash='dash', color='red')))
                        st.plotly_chart(fig_pred, use_container_width=True)

    # ---------------- STATISTICS TAB ----------------
=======
                with st.spinner("🔄 Training model... This may take a moment."):
                    try:
                        df_encoded = pd.get_dummies(df)
                        
                        if target in df_encoded.columns:
                            X = df_encoded.drop(target, axis=1)
                            y = df_encoded[target]
                            
                            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
                            
                            model = RandomForestRegressor(n_estimators=n_estimators, random_state=42, n_jobs=-1)
                            model.fit(X_train, y_train)
                            
                            pred = model.predict(X_test)
                            
                            r2 = r2_score(y_test, pred)
                            mae = mean_absolute_error(y_test, pred)
                            rmse = np.sqrt(mean_squared_error(y_test, pred))
                            
                            st.success("✅ Model trained successfully!")
                            
                            st.markdown("<br>", unsafe_allow_html=True)
                            
                            # Metrics display
                            met1, met2, met3 = st.columns(3, gap="medium")
                            
                            with met1:
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 2rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);">
                                    <div style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 0.5rem; font-family: 'Poppins';">R² Score</div>
                                    <div style="font-size: 2.5rem; font-weight: 800; font-family: 'Poppins';">{r2:.3f}</div>
                                    <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.5rem;">Model Accuracy</div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            with met2:
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); padding: 2rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3);">
                                    <div style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 0.5rem; font-family: 'Poppins';">MAE</div>
                                    <div style="font-size: 2.5rem; font-weight: 800; font-family: 'Poppins';">{mae:.2f}</div>
                                    <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.5rem;">Mean Error</div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            with met3:
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); padding: 2rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 8px 24px rgba(139, 92, 246, 0.3);">
                                    <div style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 0.5rem; font-family: 'Poppins';">RMSE</div>
                                    <div style="font-size: 2.5rem; font-weight: 800; font-family: 'Poppins';">{rmse:.2f}</div>
                                    <div style="font-size: 0.8rem; opacity: 0.8; margin-top: 0.5rem;">Root Error</div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
                            
                            # Feature importance
                            st.markdown("""
                            <div class="glass-card">
                                <div class="card-title">🎯 Feature Importance</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            importance_df = pd.DataFrame({
                                'Feature': X.columns,
                                'Importance': model.feature_importances_
                            }).sort_values('Importance', ascending=True).tail(12)
                            
                            fig_importance = px.bar(importance_df, x='Importance', y='Feature',
                                                   orientation='h', template=chart_theme,
                                                   title="<b>Top 12 Most Important Features</b>",
                                                   color='Importance',
                                                   color_continuous_scale='Blues')
                            fig_importance.update_layout(
                                height=400,
                                showlegend=False,
                                font=dict(family="Inter"),
                                title_font_size=18
                            )
                            st.plotly_chart(fig_importance, use_container_width=True)
                            
                            st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
                            
                            # Actual vs Predicted
                            st.markdown("""
                            <div class="glass-card">
                                <div class="card-title">📊 Prediction Accuracy</div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            fig_pred = px.scatter(x=y_test, y=pred, template=chart_theme,
                                                 labels={'x': 'Actual Values', 'y': 'Predicted Values'},
                                                 title="<b>Actual vs Predicted Values</b>",
                                                 opacity=0.6)
                            
                            fig_pred.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], 
                                                          y=[y_test.min(), y_test.max()],
                                                          mode='lines', name='Perfect Prediction',
                                                          line=dict(dash='dash', color='red', width=3)))
                            
                            fig_pred.update_layout(
                                height=450,
                                font=dict(family="Inter"),
                                title_font_size=18
                            )
                            st.plotly_chart(fig_pred, use_container_width=True)
                        else:
                            st.error("❌ Target variable not found in dataset!")
                    except Exception as e:
                        st.error(f"❌ Error during model training: {str(e)}")

    # ============ STATISTICS TAB ============
 
    with tab4:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">📈 Statistical Summary</div>
        </div>
        """, unsafe_allow_html=True)
        

        st.dataframe(df.describe().T.style.background_gradient(cmap='Blues'), 
                    use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Distribution plots for numeric columns
=======
        stats_df = df.describe().T
        st.dataframe(stats_df.style.background_gradient(cmap='Blues', axis=0).format("{:.2f}"), 
                    use_container_width=True)
        
        st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
        
        # Distribution plots
 
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">📊 Distribution Analysis</div>
        </div>
        """, unsafe_allow_html=True)
        

        selected_col = st.selectbox("Select column for detailed analysis", numeric_cols)
        
        col_stat1, col_stat2 = st.columns(2)
        
        with col_stat1:
            fig_hist = px.histogram(df, x=selected_col, template=chart_theme,
                                   title=f"Distribution of {selected_col}",
                                   marginal="violin")
=======
        selected_col = st.selectbox("Select column for detailed analysis", numeric_cols, key="dist_col")
        
        col_stat1, col_stat2 = st.columns(2, gap="large")
        
        with col_stat1:
            fig_hist = px.histogram(df, x=selected_col, template=chart_theme,
                                   title=f"<b>Distribution of {selected_col}</b>",
                                   marginal="box",
                                   nbins=40)
            fig_hist.update_layout(height=450, title_font_size=18, font=dict(family="Inter"))
 
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col_stat2:
            fig_box = px.box(df, y=selected_col, template=chart_theme,

                            title=f"Box Plot of {selected_col}",
                            points="outliers")
            st.plotly_chart(fig_box, use_container_width=True)

    # ---------------- DOWNLOAD SECTION ----------------
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_dl1, col_dl2, col_dl3 = st.columns([1, 1, 1])
    
    with col_dl2:
        st.download_button(
            "⬇️ Download Cleaned Dataset",
            df.to_csv(index=False),
            "cleaned_data.csv",
=======
                            title=f"<b>Statistical Boxplot of {selected_col}</b>",
                            points="outliers")
            fig_box.update_layout(height=450, title_font_size=18, font=dict(family="Inter"))
            st.plotly_chart(fig_box, use_container_width=True)
        
        st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
        
        # Summary statistics
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">🔢 Detailed Statistics</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)
        
        with col_s1:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-label">Mean</div>
                <div class="stat-value">{df[selected_col].mean():.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_s2:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-label">Median</div>
                <div class="stat-value">{df[selected_col].median():.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_s3:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-label">Std Dev</div>
                <div class="stat-value">{df[selected_col].std():.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_s4:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-label">Min</div>
                <div class="stat-value">{df[selected_col].min():.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_s5:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-label">Max</div>
                <div class="stat-value">{df[selected_col].max():.2f}</div>
            </div>
            """, unsafe_allow_html=True)

    # ================ DOWNLOAD SECTION ================
    st.markdown("""<div class="divider"></div>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">💾 Export Data</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_dl1, col_dl2, col_dl3 = st.columns(3, gap="medium")
    
    with col_dl1:
        st.download_button(
            "⬇️ CSV Format",
            df.to_csv(index=False),
            f"analytics_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "text/csv",
            use_container_width=True
        )
    
    with col_dl2:
        st.download_button(
            "⬇️ Excel Format",
            df.to_excel(index=False) if 'openpyxl' in __import__('sys').modules else b'',
            f"analytics_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    
    with col_dl3:
        st.download_button(
            "⬇️ Statistics Report",
            df.describe().T.to_csv(),
            f"statistics_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
 
            "text/csv",
            use_container_width=True
        )

else:

    # Empty state
    st.markdown("""
    <div style="text-align: center; padding: 4rem 2rem;">
        <div style="font-size: 5rem; margin-bottom: 1rem;">📊</div>
        <h2 style="color: #1a1a2e; margin-bottom: 1rem;">No Data Uploaded Yet</h2>
        <p style="color: #64748b; font-size: 1.1rem; max-width: 500px; margin: 0 auto;">
            Upload a CSV file to unlock powerful data analysis, interactive visualizations, 
            and AI-driven predictions.
        </p>
=======
    # ================ EMPTY STATE ================
    st.markdown("""
    <div class="empty-state">
        <div class="empty-state-icon">📊</div>
        <h2 style="color: #1e293b; margin-bottom: 1rem; font-family: 'Poppins', sans-serif; font-weight: 700;">No Data Uploaded Yet</h2>
        <p style="color: #64748b; font-size: 1.1rem; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Get started by uploading your CSV file. Our advanced analytics engine will help you discover insights, 
            visualize trends, and make data-driven decisions with confidence.
        </p>
        <div style="margin-top: 2rem; display: flex; gap: 1rem; justify-content: center;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1rem 1.5rem; border-radius: 12px; font-weight: 600;">
                ✨ Interactive Charts
            </div>
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 1rem 1.5rem; border-radius: 12px; font-weight: 600;">
                🤖 AI Predictions
            </div>
            <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); color: white; padding: 1rem 1.5rem; border-radius: 12px; font-weight: 600;">
                📈 Statistics
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)
