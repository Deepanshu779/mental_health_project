import streamlit as st
import pandas as pd
from datetime import datetime

# Import custom modules
from utils.styles import apply_custom_styles, render_sidebar
from utils.data_store import load_mood_logs, append_mood_log

# Try importing Plotly Express
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Page Configuration
st.set_page_config(
    page_title="Mood Tracker & Analytics - Virtual Wellness Companion",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global premium styles
apply_custom_styles()

# Render unified sidebar settings
render_sidebar()

# Page Title
st.markdown('<h1 class="gradient-text" style="font-size: 2.8rem; margin-bottom:0;">📊 Mood Journey & Analytics</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size:1.15rem; color:#9ca3af; margin-top:5px; margin-bottom:20px;">Reflect on your emotional trends and identify lifestyle correlations.</p>', unsafe_allow_html=True)

col_logger, col_stats = st.columns([1, 2], gap="large")

with col_logger:
    st.markdown('<h3 style="color:#14b8a6; margin-top:0;">📝 Log Current State</h3>', unsafe_allow_html=True)
    st.write("Take a mindful pause to record how you are feeling in this moment.")
    
    # Log Form
    with st.form("mood_logger_form", clear_on_submit=True):
        input_score = st.slider(
            "Emotional Wellness Rating (1-10):",
            min_value=1.0,
            max_value=10.0,
            value=5.0,
            step=0.5,
            help="1 = Deep distress/distracted, 5 = Balanced/Neutral, 10 = Radiantly peaceful and happy."
        )
        
        input_mood = st.selectbox(
            "Primary Emotional Tone:",
            ["neutral", "happy", "sad", "anxious", "angry", "breakup", "lonely", "tired"]
        )
        
        input_influencers = st.multiselect(
            "What factors contributed to this feeling?",
            ["💤 Sleep/Rest", "💼 Work/Study", "👥 Relationships", "🏃 Exercise/Sport", "🌡️ Health", "🍏 Diet/Nutrition", "🧘 Mindfulness", "🎭 Hobbies/Play"]
        )
        
        input_notes = st.text_area(
            "Add a brief reflection (optional):",
            placeholder="What is causing this state? What did you do about it?"
        )
        
        submit_log = st.form_submit_button("Save Reflection to Dashboard", use_container_width=True)
        
        if submit_log:
            # Format factors list nicely by removing emojis
            clean_factors = [f.split(" ")[-1] for f in input_influencers]
            success = append_mood_log(
                score=input_score,
                mood=input_mood,
                influencers=clean_factors,
                notes=input_notes
            )
            if success:
                st.success("Your reflection has been securely logged!")
                st.rerun()
                
with col_stats:
    st.markdown('<h3 style="color:#a78bfa; margin-top:0;">📈 Wellness Insights</h3>', unsafe_allow_html=True)
    
    # Load the CSV log
    df_logs = load_mood_logs()
    
    if len(df_logs) <= 1:
        st.info("💡 Log a few more mood entries in the logger panel, or chat with EmpathyBot to generate dynamic dashboard graphs!")
    else:
        # 1. Trend Line/Area Chart using Plotly
        if PLOTLY_AVAILABLE:
            st.markdown('<p style="font-weight:600; margin-bottom:5px;">Emotional Wellness Trend (Over Time)</p>', unsafe_allow_html=True)
            
            # Beautiful area trend plot
            fig_trend = px.area(
                df_logs, 
                x="timestamp", 
                y="score",
                hover_data=["mood", "influencers", "notes"],
                color_discrete_sequence=["#14b8a6"]
            )
            # Layout Customization
            fig_trend.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Time"),
                yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Wellness Score", range=[0.5, 10.5]),
                margin=dict(l=10, r=10, t=10, b=10),
                height=280
            )
            fig_trend.update_traces(
                fill='tozeroy',
                fillcolor='rgba(20, 184, 166, 0.1)',
                line=dict(width=3, color='#14b8a6')
            )
            
            st.plotly_chart(fig_trend, use_container_width=True)
            
            # Split charts inside columns
            col_chart_l, col_chart_r = st.columns(2)
            
            with col_chart_l:
                st.markdown('<p style="font-weight:600; margin-bottom:5px;">Emotional Distribution</p>', unsafe_allow_html=True)
                # Donut chart
                mood_counts = df_logs["mood"].value_counts().reset_index()
                mood_counts.columns = ["mood", "count"]
                
                fig_donut = px.pie(
                    mood_counts,
                    values="count",
                    names="mood",
                    hole=0.4,
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                fig_donut.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin=dict(l=10, r=10, t=10, b=10),
                    height=220,
                    showlegend=True
                )
                st.plotly_chart(fig_donut, use_container_width=True)
                
            with col_chart_r:
                st.markdown('<p style="font-weight:600; margin-bottom:5px;">Average Wellness by Influencer</p>', unsafe_allow_html=True)
                
                # Explode/extract multiple comma-separated influencers to calculate average wellness score
                influencer_rows = []
                for idx, row in df_logs.iterrows():
                    infl_str = row["influencers"]
                    if infl_str and infl_str != "Baseline" and infl_str != "Chat Sentiment Analysis":
                        items = [i.strip() for i in infl_str.split(",")]
                        for item in items:
                            if item:
                                influencer_rows.append({"factor": item, "score": row["score"]})
                                
                if influencer_rows:
                    df_factors = pd.DataFrame(influencer_rows)
                    df_avg = df_factors.groupby("factor")["score"].mean().reset_index()
                    df_avg = df_avg.sort_values(by="score", ascending=True)
                    
                    fig_factors = px.bar(
                        df_avg,
                        x="score",
                        y="factor",
                        orientation='h',
                        color="score",
                        color_continuous_scale=[[0, '#8b5cf6'], [1, '#14b8a6']]
                    )
                    fig_factors.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Average Wellness Score"),
                        yaxis=dict(title="Factor"),
                        coloraxis_showscale=False,
                        margin=dict(l=10, r=10, t=10, b=10),
                        height=220
                    )
                    st.plotly_chart(fig_factors, use_container_width=True)
                else:
                    st.caption("Log mood entries with multiple lifestyle factors (Sleep, Exercise, Diet) to generate correlation metrics.")
                    
        else:
            # Basic standard matplotlib plot fallback in case plotly fails
            st.line_chart(df_logs, x="timestamp", y="score")
