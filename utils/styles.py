import streamlit as st

# ==========================================
# --- EmpathyBot 2.0 Modern Styles ---
# ==========================================

CSS_STYLES = """
<style>
/* Import Calming, Elegant Google Font */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

/* Apply font to text-bearing elements safely without breaking icon fonts */
html, body, p, h1, h2, h3, h4, h5, h6, li, button, label, input, textarea, select, option, [data-testid="stMarkdownContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}


/* Background gradient styling for main area */
.stApp {
    background: linear-gradient(135deg, #0b0f19 0%, #1e1e30 50%, #111827 100%);
    color: #f3f4f6;
}

/* Sidebar Custom Styling */
section[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.9) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
}

/* Glassmorphic card custom element */
.glass-card {
    background: rgba(30, 41, 59, 0.45);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 24px;
    margin-bottom: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
    border-color: rgba(20, 184, 166, 0.4);
    box-shadow: 0 8px 32px 0 rgba(20, 184, 166, 0.1);
    transform: translateY(-2px);
}

/* Accent Card for Crisis Warning */
.crisis-card {
    background: rgba(220, 38, 38, 0.15);
    border-radius: 16px;
    border: 1px solid rgba(220, 38, 38, 0.4);
    padding: 24px;
    margin-bottom: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px 0 rgba(220, 38, 38, 0.15);
}

/* Title text highlights */
.gradient-text {
    background: linear-gradient(90deg, #14b8a6 0%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
}

/* --- Breathing Animation Styles --- */
.breathing-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 40px auto;
    width: 100%;
}

.breathing-circle-box {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background-color: rgba(20, 184, 166, 0.2);
    border: 3px solid #14b8a6;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-weight: 600;
    font-size: 1.1rem;
    text-align: center;
    box-shadow: 0 0 20px rgba(20, 184, 166, 0.4);
    animation: box-breathe 16s infinite cubic-bezier(0.4, 0, 0.2, 1);
}

.breathing-circle-calming {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background-color: rgba(20, 184, 166, 0.2);
    border: 3px solid #14b8a6;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-weight: 600;
    font-size: 1.1rem;
    text-align: center;
    box-shadow: 0 0 20px rgba(20, 184, 166, 0.4);
    animation: calming-breathe 19s infinite cubic-bezier(0.4, 0, 0.2, 1);
}

.breathing-circle-relax {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background-color: rgba(20, 184, 166, 0.2);
    border: 3px solid #14b8a6;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-weight: 600;
    font-size: 1.1rem;
    text-align: center;
    box-shadow: 0 0 20px rgba(20, 184, 166, 0.4);
    animation: relax-breathe 10s infinite cubic-bezier(0.4, 0, 0.2, 1);
}

/* Animations Definitions */
/* Box Breathing (Inhale 4, Hold 4, Exhale 4, Hold 4) = 16s total */
@keyframes box-breathe {
    0%, 100% { transform: scale(1); background-color: rgba(20, 184, 166, 0.2); box-shadow: 0 0 20px rgba(20, 184, 166, 0.4); }
    25% { transform: scale(1.5); background-color: rgba(20, 184, 166, 0.5); box-shadow: 0 0 45px rgba(20, 184, 166, 0.8); }
    50% { transform: scale(1.5); background-color: rgba(20, 184, 166, 0.5); box-shadow: 0 0 45px rgba(20, 184, 166, 0.8); }
    75% { transform: scale(1); background-color: rgba(20, 184, 166, 0.2); box-shadow: 0 0 20px rgba(20, 184, 166, 0.4); }
}

/* Calming Breathing 4-7-8 (In 4s, Hold 7s, Out 8s) = 19s total */
@keyframes calming-breathe {
    0%, 100% { transform: scale(1); background-color: rgba(20, 184, 166, 0.2); box-shadow: 0 0 20px rgba(20, 184, 166, 0.4); }
    21% { transform: scale(1.6); background-color: rgba(20, 184, 166, 0.5); box-shadow: 0 0 45px rgba(20, 184, 166, 0.8); }
    58% { transform: scale(1.6); background-color: rgba(20, 184, 166, 0.5); box-shadow: 0 0 45px rgba(20, 184, 166, 0.8); }
}

/* Relaxing Breathing 5-5 (In 5s, Out 5s) = 10s total */
@keyframes relax-breathe {
    0%, 100% { transform: scale(1); background-color: rgba(20, 184, 166, 0.2); box-shadow: 0 0 20px rgba(20, 184, 166, 0.4); }
    50% { transform: scale(1.6); background-color: rgba(20, 184, 166, 0.5); box-shadow: 0 0 45px rgba(20, 184, 166, 0.8); }
}

/* Sub-text beneath animated breathing bubble */
.breathing-subtext {
    font-size: 0.95rem;
    font-weight: 500;
    color: #a78bfa;
    margin-top: 20px;
    height: 24px;
    animation: pulse-text 2s infinite;
}

@keyframes pulse-text {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 1; }
}

/* Custom Cards grid */
.help-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-top: 15px;
}

.help-card {
    background: rgba(30, 41, 59, 0.5);
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.25s ease;
}

.help-card:hover {
    border-color: rgba(139, 92, 246, 0.4);
    background: rgba(45, 30, 80, 0.2);
    transform: translateY(-2px);
}

.help-title {
    font-size: 1.15rem;
    font-weight: 600;
    color: #14b8a6;
    margin-bottom: 8px;
}

.help-number {
    font-size: 1.3rem;
    font-weight: 700;
    color: #ffffff;
    margin: 10px 0;
    font-family: monospace !important;
}

.help-meta {
    font-size: 0.85rem;
    color: #9ca3af;
    line-height: 1.4;
}

/* Grounding checklists styling */
.grounding-step {
    padding: 12px 18px;
    border-radius: 10px;
    margin-bottom: 12px;
    border-left: 4px solid #14b8a6;
    background: rgba(255, 255, 255, 0.02);
    transition: all 0.2s;
}

.grounding-step-complete {
    border-left-color: #8b5cf6 !important;
    background: rgba(139, 92, 246, 0.08) !important;
    opacity: 0.8;
}

/* Custom styled tab selectors */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background-color: rgba(15, 23, 42, 0.3);
    padding: 6px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.stTabs [data-baseweb="tab"] {
    height: 40px;
    white-space: pre-wrap;
    background-color: transparent;
    border-radius: 8px;
    color: #9ca3af;
    font-weight: 500;
    border: none !important;
    padding: 0 16px;
    transition: all 0.2s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #ffffff;
    background-color: rgba(255, 255, 255, 0.05);
}

.stTabs [aria-selected="true"] {
    background-color: #14b8a6 !important;
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* Custom Persona Selectors */
.persona-btn {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(30, 41, 59, 0.4);
    padding: 15px;
    border-radius: 10px;
    cursor: pointer;
    text-align: center;
    transition: all 0.2s ease;
}

.persona-btn:hover {
    border-color: #14b8a6;
    background: rgba(20, 184, 166, 0.1);
}

.persona-btn-active {
    border-color: #14b8a6 !important;
    background: rgba(20, 184, 166, 0.15) !important;
    box-shadow: 0 0 10px rgba(20, 184, 166, 0.2);
}

/* Plotly Responsive styling */
.plotly-graph-container {
    background: rgba(30, 41, 59, 0.3) !important;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 10px;
}
</style>
"""


def apply_custom_styles():
    """Injects custom CSS styling for premium look and animations."""
    st.markdown(CSS_STYLES, unsafe_allow_html=True)


def draw_breathing_circle(mode="box"):
    """
    Renders an animated SVG/HTML container for breathing exercise.
    - box: Box Breathing (4s Inhale, 4s Hold, 4s Exhale, 4s Hold)
    - calming: Calming Breathing 4-7-8 (4s In, 7s Hold, 8s Out)
    - relax: Relaxing Breathing 5-5 (5s In, 5s Out)
    """
    if mode == "box":
        html_code = """
        <div class="breathing-container">
            <div class="breathing-circle-box">
                <span id="breathing-text">Breathe</span>
            </div>
            <div class="breathing-subtext" id="breathing-sub">Focus on the expand/contract timing</div>
        </div>
        <script>
            const textEl = document.getElementById('breathing-text');
            const subEl = document.getElementById('breathing-sub');
            const phases = [
                { text: 'Inhale 💨', sub: 'Inhale slowly through your nose...', duration: 4000 },
                { text: 'Hold 🔒', sub: 'Hold your breath and stay still...', duration: 4000 },
                { text: 'Exhale 🌬️', sub: 'Exhale fully through your mouth...', duration: 4000 },
                { text: 'Hold 🔒', sub: 'Rest before the next breath...', duration: 4000 }
            ];
            let currentPhase = 0;
            
            function runBreathing() {
                const phase = phases[currentPhase];
                textEl.innerText = phase.text;
                subEl.innerText = phase.sub;
                
                setTimeout(() => {
                    currentPhase = (currentPhase + 1) % phases.length;
                    runBreathing();
                }, phase.duration);
            }
            // Run
            runBreathing();
        </script>
        """
    elif mode == "calming":
        html_code = """
        <div class="breathing-container">
            <div class="breathing-circle-calming">
                <span id="breathing-text-calm">Breathe</span>
            </div>
            <div class="breathing-subtext" id="breathing-sub-calm">4-7-8 Calming technique</div>
        </div>
        <script>
            const textEl = document.getElementById('breathing-text-calm');
            const subEl = document.getElementById('breathing-sub-calm');
            const phases = [
                { text: 'Inhale 💨 (4s)', sub: 'Inhale quietly through your nose...', duration: 4000 },
                { text: 'Hold 🔒 (7s)', sub: 'Retain the air comfortably...', duration: 7000 },
                { text: 'Exhale 🌬️ (8s)', sub: 'Exhale completely with a whoosh sound...', duration: 8000 }
            ];
            let currentPhase = 0;
            
            function runBreathingCalm() {
                const phase = phases[currentPhase];
                textEl.innerText = phase.text;
                subEl.innerText = phase.sub;
                
                setTimeout(() => {
                    currentPhase = (currentPhase + 1) % phases.length;
                    runBreathingCalm();
                }, phase.duration);
            }
            runBreathingCalm();
        </script>
        """
    else:  # relax
        html_code = """
        <div class="breathing-container">
            <div class="breathing-circle-relax">
                <span id="breathing-text-relax">Breathe</span>
            </div>
            <div class="breathing-subtext" id="breathing-sub-relax">Coherent Breathing (5s In, 5s Out)</div>
        </div>
        <script>
            const textEl = document.getElementById('breathing-text-relax');
            const subEl = document.getElementById('breathing-sub-relax');
            const phases = [
                { text: 'Inhale 💨 (5s)', sub: 'Breathe in slowly...', duration: 5000 },
                { text: 'Exhale 🌬️ (5s)', sub: 'Breathe out slowly...', duration: 5000 }
            ];
            let currentPhase = 0;
            
            function runBreathingRelax() {
                const phase = phases[currentPhase];
                textEl.innerText = phase.text;
                subEl.innerText = phase.sub;
                
                setTimeout(() => {
                    currentPhase = (currentPhase + 1) % phases.length;
                    runBreathingRelax();
                }, phase.duration);
            }
            runBreathingRelax();
        </script>
        """
    st.components.v1.html(html_code, height=270)


def render_sidebar():
    """
    Renders the unified sidebar across all pages, ensuring settings and
    state persist correctly.
    """
    from utils.data_store import clear_all_logs

    # Initialize states if not set yet (just in case)
    if 'selected_persona' not in st.session_state:
        st.session_state.selected_persona = "🌿 Serene"
    if 'gemini_api_key' not in st.session_state:
        st.session_state.gemini_api_key = ""
    if 'crisis_detected' not in st.session_state:
        st.session_state.crisis_detected = False

    with st.sidebar:
        st.markdown('<h2 style="color: #14b8a6; font-weight:700;">🧠 EmpathyBot 2.0</h2>', unsafe_allow_html=True)
        st.caption("Your Premium Virtual Wellness Companion")
        st.write("---")
        
        # 1. Select Persona
        st.markdown('<p style="font-weight:600; color:#a78bfa; margin-bottom:5px;">🎭 Choose Your Companion</p>', unsafe_allow_html=True)
        
        # Determine the index for the selectbox to prevent reset
        personas = ["🌿 Serene", "⚡ Joy", "🧠 Sage"]
        try:
            p_index = personas.index(st.session_state.selected_persona)
        except ValueError:
            p_index = 0

        selected_persona = st.selectbox(
            "Select Companion:",
            personas,
            index=p_index,
            label_visibility="collapsed",
            help="🌿 Serene is calming and soft. ⚡ Joy is uplifting and bright. 🧠 Sage is reflective and wise.",
            key="selected_persona_widget"
        )
        
        # Update session state immediately
        st.session_state.selected_persona = selected_persona
        
        # Show bios based on persona
        if selected_persona == "🌿 Serene":
            st.markdown(
                '<div class="glass-card" style="padding:15px; font-size:0.85rem; border-color: rgba(20,184,166,0.3); margin-bottom: 10px;">'
                '<strong>🌿 Serene:</strong> Focuses on peace, breathing exercises, and warm comforting reassurance. Perfect for anxiety or stress relief.'
                '</div>', 
                unsafe_allow_html=True
            )
        elif selected_persona == "⚡ Joy":
            st.markdown(
                '<div class="glass-card" style="padding:15px; font-size:0.85rem; border-color: rgba(139,92,246,0.3); margin-bottom: 10px;">'
                '<strong>⚡ Joy:</strong> Promotes gratitude, highlights tiny victories, and spreads positive vibes. Great for self-compassion and brightening your day.'
                '</div>', 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="glass-card" style="padding:15px; font-size:0.85rem; border-color: rgba(255,255,255,0.15); margin-bottom: 10px;">'
                '<strong>🧠 Sage:</strong> Uses analytical active listening and gentle cognitive reframing to help you reason through worries.'
                '</div>', 
                unsafe_allow_html=True
            )
            
        st.write("---")
        
        # 2. Advanced AI Settings
        with st.expander("⚙️ Advanced AI Settings", expanded=False):
            gemini_api_key = st.text_input(
                "Google Gemini API Key",
                type="password",
                placeholder="AI Studio API key (AI Mode)...",
                value=st.session_state.gemini_api_key,
                help="Securely input your Google Gemini API key to activate full contextual conversational AI. Key remains in-memory only."
            )
            st.session_state.gemini_api_key = gemini_api_key
            
            if gemini_api_key:
                st.markdown('<p style="color:#22c55e; font-size:0.85rem; font-weight:600; margin:0;">🟢 Advanced AI Mode Active</p>', unsafe_allow_html=True)
                st.caption("Powered by Gemini 1.5 Flash.")
            else:
                st.markdown('<p style="color:#3b82f6; font-size:0.85rem; font-weight:600; margin:0;">🔵 Offline Companion Mode Active</p>', unsafe_allow_html=True)
                st.caption("Using local rules & empathetic responses.")
                
        st.write("---")
        
        # 3. System Reset buttons
        st.markdown('<p style="font-weight:600; color:#ef4444; margin-bottom:5px;">🗑️ Reset Data</p>', unsafe_allow_html=True)
        if st.button("Clear App Data", help="Resets chat history and clears persistent local CSV log file.", use_container_width=True):
            clear_all_logs()
            st.session_state.chat_history = [
                {"role": "assistant", "content": "Hello. I am your emotional companion. How are you feeling today? I am here to listen without judgment."}
            ]
            st.session_state.last_significant_mood = None
            st.session_state.crisis_detected = False
            st.success("All logs and chat history cleared successfully.")
            st.rerun()
