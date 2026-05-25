import streamlit as st
from utils.styles import apply_custom_styles, render_sidebar
from utils.data_store import append_mood_log
from utils.bot_logic import (
    check_crisis,
    detect_mood,
    get_offline_response,
    generate_ai_response,
    EMERGENCY_RESPONSE
)

# Safe baseline scores for auto-logging chat moods
MOOD_SCORES_MAP = {
    'happy': 8.5,
    'neutral': 5.0,
    'anxious': 3.5,
    'sad': 2.5,
    'angry': 2.0,
    'breakup': 1.5,
    'lonely': 2.0,
    'tired': 3.5,
    'crisis': 1.0
}

# Page Setup
st.set_page_config(
    page_title="Empathy Chatbot - Virtual Wellness Companion",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global premium custom styles
apply_custom_styles()

# Initialize session states if they were bypassed by loading this page directly
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

# Fetch active configurations
active_persona = st.session_state.selected_persona
gemini_key = st.session_state.gemini_api_key

# Page Title
st.markdown('<h1 class="gradient-text" style="font-size: 2.8rem; margin-bottom:0;">💬 Companion Chat</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:1.15rem; color:#9ca3af; margin-top:5px; margin-bottom:20px;">Conversing with <strong>{active_persona}</strong></p>', unsafe_allow_html=True)

# Safety/Crisis Disclaimer Banner
st.markdown(
    '<div class="glass-card" style="padding: 12px 18px; margin-bottom:15px; border-left: 4px solid #ef4444; font-size:0.85rem;">'
    '⚠️ <strong>Safety Disclaimer:</strong> EmpathyBot is a supportive demonstration chatbot and does not substitute for '
    'clinical healthcare or professional therapy. If you are experiencing a crisis, please navigate to the <strong>Emergency Helpline</strong> '
    'page in the sidebar immediately.'
    '</div>',
    unsafe_allow_html=True
)

# Display crisis override if detected in session
if st.session_state.crisis_detected:
    st.markdown(
        f'<div class="crisis-card">'
        f'<h3 style="color:#ef4444; margin-top:0;">🛑 Crisis Support Triggered</h3>'
        f'<p>{EMERGENCY_RESPONSE}</p>'
        f'</div>',
        unsafe_allow_html=True
    )
    if st.button("I feel safer now. Restart Chat.", type="primary", use_container_width=True):
        st.session_state.crisis_detected = False
        st.session_state.chat_history = [
            {"role": "assistant", "content": "Welcome back. Let's take things slow. How can I support you right now?"}
        ]
        st.rerun()
        
else:
    # Chat Message Container
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # User input box
    user_input = st.chat_input("Type a message to your companion...")
    
    if user_input:
        # 1. Append User Input
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        # 2. Crisis check (Highest Priority)
        if check_crisis(user_input):
            st.session_state.crisis_detected = True
            # Log a background crisis event
            append_mood_log(
                score=MOOD_SCORES_MAP['crisis'],
                mood='crisis',
                influencers='Crisis Triggered',
                notes=f"Crisis trigger detected in message: '{user_input[:40]}...'"
            )
            st.session_state.chat_history.append({"role": "assistant", "content": "I detected that you may be in crisis. Please consult the emergency resources shown immediately."})
            st.rerun()
            
        # 3. Standard Chat Processing
        else:
            detected_mood = detect_mood(user_input)
            
            # Auto-log mood score in background if a clean mood was detected!
            if detected_mood != 'neutral':
                st.session_state.last_significant_mood = detected_mood
                score = MOOD_SCORES_MAP.get(detected_mood, 5.0)
                append_mood_log(
                    score=score,
                    mood=detected_mood,
                    influencers="Chat Sentiment Analysis",
                    notes=f"Auto-logged from chat: '{user_input[:40]}...'"
                )
            
            # Generate Bot response
            with st.spinner("Your companion is typing..."):
                if gemini_key:
                    bot_reply_msg = generate_ai_response(
                        prompt=user_input,
                        api_key=gemini_key,
                        persona_name=active_persona,
                        chat_history=st.session_state.chat_history[:-1] # Exclude the user input we just added
                    )
                else:
                    is_followup = (detected_mood == 'neutral' and st.session_state.last_significant_mood is not None)
                    mood_state = detected_mood if detected_mood != 'neutral' else st.session_state.last_significant_mood
                    if mood_state is None:
                        mood_state = 'neutral'
                    bot_reply_msg = get_offline_response(active_persona, mood_state, is_followup=is_followup)
            
            # Append assistant reply
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply_msg})
            with st.chat_message("assistant"):
                st.markdown(bot_reply_msg)
                
            # Auto-scroll or reload page to show charts updated in other tabs
            st.rerun()
