import streamlit as st
from utils.styles import apply_custom_styles, render_sidebar

# Page Setup
st.set_page_config(
    page_title="Emergency Helplines - Virtual Wellness Companion",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global premium custom styles
apply_custom_styles()

# Render unified sidebar settings
render_sidebar()

# Page Title
st.markdown('<h1 class="gradient-text" style="font-size: 2.8rem; margin-bottom:0;">🚨 Emergency Helpline Directory</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size:1.15rem; color:#9ca3af; margin-top:5px; margin-bottom:20px;">If you, a friend, or a loved one are in distress, please reach out immediately. The following professional resources are entirely free, confidential, and available 24/7.</p>', unsafe_allow_html=True)

region = st.radio(
    "Choose Your Region:",
    ["🇺🇸 United States", "🇬🇧 United Kingdom", "🇮🇳 India", "🇨🇦 Canada", "🌐 International"],
    horizontal=True
)

st.write("##")

# Helplines Cards grids based on region choice
if "United States" in region:
    st.markdown(
        '<div class="help-grid">'
        '  <div class="help-card">'
        '    <div class="help-title">Suicide & Crisis Lifeline</div>'
        '    <div class="help-number">Call or Text: 988</div>'
        '    <div class="help-meta">Available 24/7 in English & Spanish. Free, private, and secure.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">Crisis Text Line</div>'
        '    <div class="help-number">Text: HOME to 741741</div>'
        '    <div class="help-meta">Connect with a real volunteer crisis counselor via text 24/7.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">The Trevor Project (LGBTQ+)</div>'
        '    <div class="help-number">Call: 1-866-488-7386</div>'
        '    <div class="help-meta">Dedicated crisis counselors supporting LGBTQ+ youth 24/7. Text START to 678-678.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">Veterans Crisis Line</div>'
        '    <div class="help-number">Call: 988, then press 1</div>'
        '    <div class="help-meta">Crisis support custom-tailored for Veterans, service members, and their families.</div>'
        '  </div>'
        '</div>',
        unsafe_allow_html=True
    )
elif "United Kingdom" in region:
    st.markdown(
        '<div class="help-grid">'
        '  <div class="help-card">'
        '    <div class="help-title">Samaritans UK Helpline</div>'
        '    <div class="help-number">Call: 116 123</div>'
        '    <div class="help-meta">Free phone support for anyone struggling to cope, 365 days a year.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">NHS Mental Health Services</div>'
        '    <div class="help-number">Call: 111</div>'
        '    <div class="help-meta">Direct line to local UK mental health services for urgent psychiatric assessment.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">Shout Crisis Text Line</div>'
        '    <div class="help-number">Text: SHOUT to 85258</div>'
        '    <div class="help-meta">A free, confidential 24/7 text support service in the UK.</div>'
        '  </div>'
        '</div>',
        unsafe_allow_html=True
    )
elif "India" in region:
    st.markdown(
        '<div class="help-grid">'
        '  <div class="help-card">'
        '    <div class="help-title">Kiran Mental Health Helpline</div>'
        '    <div class="help-number">Call: 1800-599-0019</div>'
        '    <div class="help-meta">Official Government of India helpline. 24/7, free, confidential, in 13 languages.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">AASRA Crisis Support</div>'
        '    <div class="help-number">Call: +91-9820466726</div>'
        '    <div class="help-meta">Professional suicide prevention and emotional support service based in Mumbai.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">Vandrevala Foundation</div>'
        '    <div class="help-number">Call: +91-9999666555</div>'
        '    <div class="help-meta">24/7 clinical mental health counseling and crisis support in multiple Indian languages.</div>'
        '  </div>'
        '</div>',
        unsafe_allow_html=True
    )
elif "Canada" in region:
    st.markdown(
        '<div class="help-grid">'
        '  <div class="help-card">'
        '    <div class="help-title">Canada Suicide Crisis Helpline</div>'
        '    <div class="help-number">Call or Text: 988</div>'
        '    <div class="help-meta">Bilingual (English & French) support available 24/7 for Canadians. Free.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">Kids Help Phone</div>'
        '    <div class="help-number">Call: 1-800-668-6868</div>'
        '    <div class="help-meta">24/7 phone support and crisis text line (text CONNECT to 686868) for Canadian youth.</div>'
        '  </div>'
        '</div>',
        unsafe_allow_html=True
    )
else:  # International
    st.markdown(
        '<div class="help-grid">'
        '  <div class="help-card">'
        '    <div class="help-title">Befrienders Worldwide</div>'
        '    <div class="help-number">Visit: www.befrienders.org</div>'
        '    <div class="help-meta">Search and locate free, confidential helplines in over 40 countries across the globe.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">Find A Helpline</div>'
        '    <div class="help-number">Visit: www.findahelpline.com</div>'
        '    <div class="help-meta">A secure search engine tool linking you directly to local mental health lines anywhere in the world.</div>'
        '  </div>'
        '  <div class="help-card">'
        '    <div class="help-title">International Association for Suicide Prevention (IASP)</div>'
        '    <div class="help-number">Visit: www.iasp.info</div>'
        '    <div class="help-meta">Access and browse verified global crisis resources, directories, and supportive networks.</div>'
        '  </div>'
        '</div>',
        unsafe_allow_html=True
    )
