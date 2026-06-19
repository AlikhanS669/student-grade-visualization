"""
Streamlit Interactive Dashboard for Student Grade Prediction
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Student Grade Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Grade Prediction - Interactive Dashboard")
st.markdown("---")

@st.cache_data
def load_data():
    df = pd.read_csv('data/raw/student-grades.csv')
    return df

df = load_data()

st.sidebar.title("🖥️ Navigation")
page = st.sidebar.radio(
    "Select Page:",
    ["📈 Overview", "📊 Analysis", "🔍 Exploration", "📋 About"]
)

if page == "📈 Overview":
    st.header("Dataset Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        st.metric("Total Features", df.shape[1])
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
    with col4:
        st.metric("Duplicates", df.duplicated().sum())
    
    st.subheader("Dataset Head")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe(), use_container_width=True)

elif page == "📊 Analysis":
    st.header("Statistical Analysis")
    st.subheader("Final Grade Distribution (G3)")
    
    fig = go.Figure(data=[go.Histogram(x=df['G3'], nbinsx=30)])
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Grades by Gender")
    fig = px.box(df, x='sex', y='G3')
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Grades by Study Time")
    fig = px.box(df, x='studytime', y='G3')
    st.plotly_chart(fig, use_container_width=True)

elif page == "🔍 Exploration":
    st.header("Interactive Exploration")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns))
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        feature_x = st.selectbox("Select X-axis feature:", numeric_cols)
    with col2:
        feature_y = st.selectbox("Select Y-axis feature:", numeric_cols, index=1)
    
    fig = px.scatter(df, x=feature_x, y=feature_y, color='G3')
    st.plotly_chart(fig, use_container_width=True)

else:
    st.header("About This Dashboard")
    st.markdown("""
    ### Student Grade Prediction - Data Visualization Project
    
    **Dataset:** Kaggle - Student Grade Prediction  
    **Records:** 395 students  
    **Features:** 30+ attributes
    
    **Technologies:** Python, Pandas, Plotly, Streamlit
    """)
