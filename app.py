import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ---------------- PAGE CONFIG ----------------
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
st.markdown("""
<div class="glass-card">
    <div class="card-title">📁 Data Upload</div>
</div>
""", unsafe_allow_html=True)

col_upload, col_info = st.columns([2, 1])

with col_upload:
    file = st.file_uploader("Drag and drop your CSV file here", type=["csv"], label_visibility="collapsed")

with col_info:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #f59e0b;">
        <p style="margin: 0; color: #92400e; font-weight: 500;">💡 Tip</p>
        <p style="margin: 0.5rem 0 0 0; color: #78350f; font-size: 0.9rem;">Upload a CSV file to start exploring your data with interactive visualizations and AI predictions.</p>
    </div>
    """, unsafe_allow_html=True)

if file:
    df = pd.read_csv(file)

    # ---------------- DATA CLEANING ----------------
    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)

    # ---------------- METRICS SECTION ----------------
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                📊
            </div>
            <div class="metric-value">{df.shape[0]:,}</div>
            <div class="metric-label">Total Rows</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
                📋
            </div>
            <div class="metric-value">{df.shape[1]}</div>
            <div class="metric-label">Total Columns</div>
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
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        missing = df.isnull().sum().sum()
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-icon" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
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
    with tab1:
        st.markdown("""
        <div class="glass-card">
            <div class="card-title">🔍 Dataset Overview</div>
        </div>
        """, unsafe_allow_html=True)
        
        col_data1, col_data2 = st.columns([3, 1])
        
        with col_data1:
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
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Correlation heatmap
            st.markdown("<br>", unsafe_allow_html=True)
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
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            target = st.selectbox("🎯 Select Target Variable", numeric_cols)
            
            n_estimators = st.slider("🌲 Number of Trees", 10, 200, 100)
            test_size = st.slider("📊 Test Size (%)", 10, 40, 20) / 100
            
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
    </div>
    """, unsafe_allow_html=True)
