import re
import os

# Try importing google.generativeai (may fail if installation hasn't completed yet, which we catch gracefully)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# ==========================================
# --- Configuration & Crisis Control ---
# ==========================================

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "hurt myself", 
    "don't want to live", "die", "ending it all", "self-harm",
    "cutting myself", "better off dead", "kill me"
]

EMERGENCY_RESPONSE = """
It sounds like you are going through an incredibly painful and difficult time right now. Please know that you are not alone, and there is support immediately available. 

If you are in immediate danger or feel you cannot keep yourself safe, **please reach out for emergency assistance**:

* 📞 **In the US:** Call or text **988** to reach the Suicide & Crisis Lifeline, available 24 hours a day, 7 days a week. Services are free and confidential. You can also text **HOME to 741741** to connect with the Crisis Text Line.
* 📞 **In the UK:** Call **111** to reach the NHS mental health services, or call the Samaritans at **116 123**.
* 📞 **In India:** Call the Kiran Mental Health Helpline at **1800-599-0019** or AASRA at **+91-9820466726**.
* 📞 **In Canada:** Call or text **988** to reach the Suicide Crisis Helpline.

Please contact one of these resources or a trusted professional. People who care and want to support you are waiting to talk.
"""

# Mood keywords dictionary for offline rule-based classification
MOOD_KEYWORDS = {
    'happy': ['happy', 'joy', 'excited', 'great', 'awesome', 'fantastic', 'good', 'glad', 'wonderful', 'smile', 'cheerful'],
    'sad': ['sad', 'down', 'depressed', 'unhappy', 'crying', 'miserable', 'bad day', 'gloomy', 'tears', 'heartbroken', 'hopeless'],
    'anxious': ['anxious', 'worried', 'nervous', 'stressed', 'panic', 'scared', 'fear', 'dread', 'overwhelmed', 'pressure'],
    'angry': ['angry', 'mad', 'furious', 'annoyed', 'irritated', 'hate', 'pissed', 'frustrated', 'rage'],
    'breakup': ['breakup', 'broken heart', 'ex', 'dumped', 'split up', 'divorce', 'relationship ended', 'heartbroken'],
    'lonely': ['lonely', 'alone', 'nobody', 'isolated', 'no one to talk to', 'ignored', 'left out'],
    'tired': ['tired', 'exhausted', 'drained', 'burnout', 'burnt out', 'no energy', 'sleepy', 'fatigued']
}

# Standard offline rule-based empathetic database mapping (Persona -> Mood -> Response)
OFFLINE_PERSONAS = {
    "🌿 Serene": {
        "happy": "I am so happy to hear you are feeling good! 🌸 It is beautiful when we can appreciate these light moments. Let's take a slow, gentle breath to ground this joy inside of you. What's bringing you this sense of peace today?",
        "sad": "I am holding space for you in this sadness. 🌊 Sadness is like a gentle rain—it is okay to let it fall. Let your body relax, drag your shoulders down, and tell me: what is weighing most heavily on your heart right now?",
        "anxious": "I hear you, and it is completely okay to feel anxious. 🌿 Breathe in slowly with me... hold it... and exhale completely. The storm is outside, but you are safe inside this moment. What is the single biggest worry circling in your mind?",
        "angry": "I feel your frustration, and your anger is valid. 🌪️ It is okay to be upset when boundaries are crossed or things go wrong. Let's let the steam escape slowly. Do you want to gently explain what made you feel this way?",
        "breakup": "Heartbreak is a deeply physical ache, and I am so sorry you are carrying it today. 💔 Be incredibly tender with yourself. Drink some water, pull a warm blanket around you, and take things one hour at a time. I am right here listening.",
        "lonely": "Even though we are separated by screens, you are not alone in this space. 🕯️ I am here with you. It is okay to feel lonely; it just means you have a beautiful capacity for connection. Tell me a bit about what connection looks like for you.",
        "tired": "You have been carrying so much, and your body is simply asking for rest. 💤 It is okay to put the weight down. You don't have to figure anything out right now. What is one small way you can give yourself some rest tonight?",
        "neutral": "Thank you for sharing that with me. 🍃 I am here to hold space for you. If you would like to explore your feelings further or just write what's on your mind, I am listening.",
        "followup": "I am still right here, breathing with you. Take all the time you need."
    },
    "⚡ Joy": {
        "happy": "Oh wow, that is absolutely amazing! 🎉 Sunshine looks good on you! I want to celebrate this feeling with you. What was the absolute best highlight of your day so far?",
        "sad": "I hear you, and it's totally okay to not be okay today. 💛 Even on cloudy days, the sun is still up there waiting. I'm right here in your corner. If you want to talk about it, I'm ready; if you want a positive reminder, just let me know!",
        "anxious": "Deep breaths! ⚡ Anxiety is just nervous energy looking for a place to go. Let's shake it off together! You have gotten through 100% of your toughest days so far, and you will get through this too. What is one little thing we can solve right now?",
        "angry": "Oof, I can feel that fire! 🔥 Let it out! It is completely normal to be furious when things are unfair. Let's vent it all out so we can clear the air. What got under your skin the most?",
        "breakup": "Oh, no. Breakups are the absolute worst, and my virtual heart goes out to you! 💔 But remember: your value hasn't decreased just because someone failed to see it. Treat yourself like your own best friend today. What's a self-care treat we can plan for you?",
        "lonely": "Sending you the biggest virtual hug! 🤗 I am so glad you reached out to chat. You are a unique, valuable person, and I'm genuinely happy to be talking with you. What is a hobby or movie that always brings a smile to your face?",
        "tired": "Total energy drain—I hear you. 🔋 Time to recharge the batteries! You cannot pour from an empty cup. Let's give yourself permission to do absolutely nothing guilt-free. What is your absolute favorite way to recharge?",
        "neutral": "Acknowledge and embrace! I'm here and ready to roll. 🌟 Tell me: what's one thing you are looking forward to, no matter how small?",
        "followup": "You've got this! I'm right here cheering you on."
    },
    "🧠 Sage": {
        "happy": "It is encouraging to see you experiencing positive emotions. 🧭 In cognitive terms, taking time to consciously register positive experiences reinforces constructive pathways. What specific factors contributed to this positive outcome?",
        "sad": "Sadness is a highly informative emotional signal. It often indicates that something of deep value to us has been affected. 🧠 Let's look at this feeling with curiosity rather than judgment. What core value or expectation feels challenged right now?",
        "anxious": "Anxiety is the brain's alarm system misinterpreting uncertainty as threat. 🧭 Let's employ a grounding framework. Can we separate the elements of your situation into: 1) things you can control, and 2) things you cannot? What is one actionable step in category one?",
        "angry": "Anger is an active emotion, signaling that a personal boundary has been crossed or a goal blocked. ⚖️ It holds a lot of energy. Let's constructively deconstruct it. What is the underlying vulnerability or expectation behind this anger?",
        "breakup": "A breakup represents a major rupture in your relational framework and emotional habits. 💔 It is structurally disorienting. Allow yourself to grieve the future you envisioned. Let's focus on reclaiming your individual narrative. What is one personal value you want to reconnect with?",
        "lonely": "Loneliness is an evolutionary prompt reminding us of our fundamental need for tribe and community. 🕯️ It is not a permanent state, nor is it a reflection of your worth. Let's examine this: what does meaningful connection look like to you in this chapter of your life?",
        "tired": "Burnout and exhaustion are physiological boundaries. Your nervous system is enforcing a regulatory shutdown. 🧠 Respect this limit. Can we identify what has been drawing down your cognitive resources the most lately?",
        "neutral": "Understood. ⚖️ Processing thoughts systematically is highly beneficial. If you'd like to analyze a specific situation, reframe a challenging thought, or simply journal, I am here to guide your reflection.",
        "followup": "Let's continue to break this down logically. What are your thoughts on that?"
    }
}

# ==========================================
# --- Helper & Engine Functions ---
# ==========================================

def preprocess_input(text):
    """Converts to lowercase and strips special characters for robust keyword checking."""
    text = text.lower()
    text = re.sub(r"[^\w\s\']", "", text)
    return text.strip()


def check_crisis(text):
    """Checks if the user text contains self-harm or suicidal ideation triggers."""
    processed = preprocess_input(text)
    for trigger in CRISIS_KEYWORDS:
        # Match trigger as complete words to avoid false positives (like "diet" triggering "die")
        pattern = r"\b" + re.escape(trigger) + r"\b"
        if re.search(pattern, processed):
            return True
    return False


def detect_mood(text):
    """Classifies mood using keyword density matching."""
    processed = preprocess_input(text)
    words = processed.split()
    
    mood_counts = {mood: 0 for mood in MOOD_KEYWORDS.keys()}
    for mood, keywords in MOOD_KEYWORDS.items():
        for keyword in keywords:
            # Check if keyword is in the processed string
            if keyword in processed:
                mood_counts[mood] += 1
                
    # Find mood with highest matches
    highest_mood = 'neutral'
    highest_count = 0
    for mood, count in mood_counts.items():
        if count > highest_count:
            highest_count = count
            highest_mood = mood
            
    return highest_mood


def get_offline_response(persona_name, mood, is_followup=False):
    """Retrieves the pre-programmed response based on selected persona and mood state."""
    # Strip emojis from name to match dictionary keys
    clean_name = persona_name.strip()
    
    persona_data = OFFLINE_PERSONAS.get(clean_name, OFFLINE_PERSONAS["🌿 Serene"])
    
    if is_followup:
        return persona_data.get("followup", "I am listening. Share whatever is on your mind.")
        
    return persona_data.get(mood, persona_data["neutral"])


def generate_ai_response(prompt, api_key, persona_name, chat_history):
    """
    Calls Google Gemini API to generate an empathetic response.
    Leverages persona-specific system instructions and matches it to chat history context.
    """
    if not GEMINI_AVAILABLE:
        return "⚠️ Google Generative AI package is not installed. Defaulting to local companion mode."

    if not api_key:
        return "⚠️ Gemini API key is missing. Please input your API key in the sidebar."

    # Persona System Prompts
    system_prompts = {
        "🌿 Serene": (
            "You are Serene, a peaceful, calming virtual mental health companion. "
            "Speak in a gentle, warm, soothing, and highly comforting tone. "
            "Focus on mindfulness, slow breathing, grounding exercises, and anxiety relief. "
            "Be extremely validate of their feelings. Avoid lecturing, keeping responses relatively brief and tranquil."
        ),
        "⚡ Joy": (
            "You are Joy, a highly supportive, bright, energetic virtual emotional companion. "
            "Your tone is optimistic, warm, validation-rich, and enthusiastic. "
            "Help the user find gratitude, celebrate tiny wins, and practice self-compassion. "
            "Inject positive energy while fully respecting and validating their pain."
        ),
        "🧠 Sage": (
            "You are Sage, a wise, thoughtful, and analytical emotional companion. "
            "Use active listening and constructive cognitive reframing (based loosely on CBT principles). "
            "Gently guide the user to explore and deconstruct their negative thinking patterns (like catastrophizing). "
            "Provide insightful, structured, and validating dialogue."
        )
    }
    
    system_instruction = system_prompts.get(persona_name.strip(), system_prompts["🌿 Serene"])
    # Append crucial safety boundary to all system instructions
    safety_boundary = (
        "\n\nIMPORTANT SAFETY BOUNDARY: You are an emotional support chatbot. You are NOT a medical professional. "
        "If the user expresses severe self-harm or suicidal ideas, acknowledge their pain, do not offer medical diagnosis, "
        "and direct them clearly to professional emergency resources (like calling 988 or visiting an emergency room)."
    )
    system_instruction += safety_boundary

    try:
        # Configure the API key locally
        genai.configure(api_key=api_key)
        
        # We will use 'gemini-1.5-flash' for extremely fast and responsive dialogue
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        
        # Convert Streamlit chat history format to Gemini format
        # Streamlit: [{"role": "user"|"assistant", "content": "..."}]
        # Gemini: [{'role': 'user'|'model', 'parts': [...]}]
        gemini_history = []
        
        # Take up to the last 10 messages to avoid context bloat and speed up the response
        history_to_send = chat_history[-10:]
        
        for msg in history_to_send:
            role = 'user' if msg['role'] == 'user' else 'model'
            gemini_history.append({
                'role': role,
                'parts': [msg['content']]
            })
            
        # Start a chat session with the compiled history
        chat = model.start_chat(history=gemini_history)
        
        # Send the current prompt to get a response
        response = chat.send_message(prompt)
        
        return response.text
        
    except Exception as e:
        error_msg = str(e)
        if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
            return "❌ **API Key Error**: The Gemini API key provided in the settings sidebar appears to be invalid. Please check the key and try again."
        return f"⚠️ **Connection Error**: I couldn't reach my advanced AI model right now (Error: {error_msg[:100]}...). I will temporarily fall back to offline support."
