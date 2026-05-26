# 🧠 EmpathyBot 2.0 - Virtual Wellness Companion

A premium, highly-designed, interactive mental health and emotional support companion built with **Streamlit**, **Plotly**, and **Google Gemini AI**.

This application is styled with a gorgeous dark-theme glassmorphic UI, smooth micro-animations, customizable companion personas, and full local-first mood data logging.

---

## 🌟 Premium Features

- **💬 Companion Chat**: Talk through your thoughts with three custom-designed, highly supportive virtual personas:
  - **🌿 Serene**: Quiet, soft, and soothing; ideal for anxiety and stress relief.
  - **⚡ Joy**: Radiant, optimistic, and highly validating; focuses on celebrating minor wins and self-compassion.
  - **🧠 Sage**: Reflective, wise, and analytical; leverages cognitive reframing (CBT) principles.
- **📊 Mood Journey & Analytics**: Record your emotional state, log contributing lifestyle factors (sleep, relationships, exercise), and view stunning interactive wellness trends, average factor weights, and donut distribution charts using **Plotly**.
- **🚨 Crisis Safeguard & regional Helpline Directory**: High-priority real-time sentiment keyword screening instantly triggers empathetic boundaries and displays active emergency hotline details across multiple regions (**US**, **UK**, **India**, **Canada**, and **International**).
- **🧘 Calming Exercises**: Integrated interactive breathing modules with dynamic expand-and-contract CSS visual timings for Box Breathing, Calming 4-7-8, and Coherent breathing.

---

## 🛠️ Technology Stack

- **Frontend/Logic**: Python, Streamlit, HTML5/CSS3 (Glassmorphism & animations)
- **Data & Visualizations**: Pandas, Plotly Express, Matplotlib
- **AI Core**: Google Gemini 1.5 Flash (for rich contextual conversations)

---

## 📂 Project Directory Structure

```
mental_health_project/
├── app.py                   # Main Landing Page / Configuration Initialization
├── pages/                   # Feature Pages
│   ├── Chatbot.py           # Premium Empathy Chatbot Interface
│   ├── Mood_Tracker.py      # Interactive Mood Journeys & Plotly Analytics
│   └── Helpline.py          # Comprehensive regional Crisis Directory
├── utils/                   # Shared Helper Utilities
│   ├── bot_engine.py        # Gemini API connectors, Prompt Engineering, & offline Fallback
│   ├── bot_logic.py         # Primary mood analysis & compatibility wrappers
│   ├── data_store.py        # CSV local storage interface for mood metrics
│   └── styles.py            # Glassmorphism design system & breathing SVG engines
├── .streamlit/
│   └── config.toml          # Native Streamlit color themes & server setups
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Install Dependencies
Make sure you have `streamlit`, `pandas`, `plotly`, and `google-generativeai` installed:
```bash
pip install streamlit pandas plotly google-generativeai matplotlib
```

### 2. Launch the Application
Run the Streamlit server from the project root directory:
```bash
streamlit run app.py
```
This will automatically spin up the development server and open a new tab in your browser at `http://localhost:8501`.

---

## ⚠️ Important Clinical Disclaimer
This application is designed as a technological demonstration for emotional support, grounding, and self-reflection. It is **not a clinical diagnostic tool** and does not substitute for medical health advice, therapy, or formal psychiatric care. If you are in crisis, please navigate to the Helpline page and contact emergency services immediately.
