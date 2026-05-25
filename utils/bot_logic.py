import streamlit as st
from utils.bot_engine import (
    check_crisis,
    detect_mood,
    get_offline_response,
    generate_ai_response,
    EMERGENCY_RESPONSE
)

# Export core response and check mechanisms for easy inclusion in subpages
__all__ = [
    'check_crisis',
    'detect_mood',
    'get_offline_response',
    'generate_ai_response',
    'EMERGENCY_RESPONSE'
]

def bot_reply(msg):
    """
    Simple compatibility helper matching the notebook's early prototype signature.
    Routes to the offline/engine responses.
    """
    mood = detect_mood(msg)
    # Basic routing
    if check_crisis(msg):
        return EMERGENCY_RESPONSE
    
    return get_offline_response("🌿 Serene", mood)
