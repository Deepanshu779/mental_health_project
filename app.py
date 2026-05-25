import streamlit as st
import os

# Import custom modules
from utils.styles import apply_custom_styles, render_sidebar
from utils.data_store import init_data_store

# Initialize page configuration
st.set_page_config(
    page_title="EmpathyBot 2.0 - Safe Space",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global custom styles & data store
apply_custom_styles()
init_data_store()

# Initialize session state objects
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello. I am your emotional companion. How are you feeling today? I am here to listen without judgment."}
    ]
if 'last_significant_mood' not in st.session_state:
    st.session_state.last_significant_mood = None
if 'crisis_detected' not in st.session_state:
    st.session_state.crisis_detected = False
if 'selected_persona' not in st.session_state:
    st.session_state.selected_persona = "🌿 Serene"
if 'gemini_api_key' not in st.session_state:
    st.session_state.gemini_api_key = ""

# Render unified sidebar settings
render_sidebar()

# ==========================================
# --- Simple, Elegant Landing Page ---
# ==========================================

# Minimalist Centered Header
st.write("##")
st.markdown('<div style="text-align: center;"><h1 class="gradient-text" style="font-size: 3.5rem; margin-bottom:0;">Welcome to EmpathyBot</h1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p style="font-size:1.3rem; color:#9ca3af; margin-top:5px; margin-bottom:40px;">A peaceful, secure space to reflect, converse, and track emotional wellness.</p></div>', unsafe_allow_html=True)

# Single elegant greeting banner
st.markdown(
    '<div class="glass-card" style="padding: 30px; text-align: center; border-color: rgba(20,184,166,0.15); max-width: 800px; margin: 0 auto;">'
    '  <h3 style="color:#ffffff; margin-top:0; font-weight:600; font-size: 1.5rem;">Take a Deep Breath 🌿</h3>'
    '  <p style="font-size:1.05rem; color:#d1d5db; line-height:1.7; margin-bottom:20px;">'
    '    This is your private emotional sanctuary. EmpathyBot is here to support you '
    '    without judgment. Share how you feel, record your emotional trends, and access support resources anytime.'
    '  </p>'
    '  <p style="color:#a78bfa; font-weight:600; font-size:1.05rem; margin-bottom:0;">'
    '    👈 Select a companion page in the sidebar menu to begin.'
    '  </p>'
    '</div>',
    unsafe_allow_html=True
)

st.write("##")
st.write("##")

# Three simple visual column cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        '<div class="glass-card" style="text-align: center; padding: 25px; height:100%;">'
        '  <span style="font-size: 2.5rem;">💬</span>'
        '  <h4 style="color:#14b8a6; font-weight:600; margin-top:15px; margin-bottom:10px;">Companion Chat</h4>'
        '  <p style="font-size:0.9rem; color:#9ca3af; line-height:1.5; margin-bottom:0;">'
        '    Talk through your day with calming, uplifting, or reflective personas.'
        '  </p>'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="glass-card" style="text-align: center; padding: 25px; height:100%;">'
        '  <span style="font-size: 2.5rem;">📊</span>'
        '  <h4 style="color:#8b5cf6; font-weight:600; margin-top:15px; margin-bottom:10px;">Mood Tracking</h4>'
        '  <p style="font-size:0.9rem; color:#9ca3af; line-height:1.5; margin-bottom:0;">'
        '    Record emotional wellness scores and identify lifestyle correlations.'
        '  </p>'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="glass-card" style="text-align: center; padding: 25px; height:100%;">'
        '  <span style="font-size: 2.5rem;">🚨</span>'
        '  <h4 style="color:#f43f5e; font-weight:600; margin-top:15px; margin-bottom:10px;">Helpline Directory</h4>'
        '  <p style="font-size:0.9rem; color:#9ca3af; line-height:1.5; margin-bottom:0;">'
        '    Quickly access free, 24/7 confidential crisis and support lines.'
        '  </p>'
        '</div>',
        unsafe_allow_html=True
    )