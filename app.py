import streamlit as st
import base64

st.set_page_config(page_title="EQ-Scan AI Demo", layout="centered")

st.title("🎧 EQ-Scan AI — Emotional Communication Analyzer (Demo)")
st.write("Upload a short audio clip or enter text to analyze your emotional tone, clarity, confidence, and stress level.")

# -------- TEXT INPUT ----------
st.subheader("📝 Text Input")
text_input = st.text_area("Type or paste your message here:")

# -------- AUDIO INPUT ----------
st.subheader("🎤 Voice Input")
audio_file = st.file_uploader("Upload a WAV/MP3 file (10–30 sec)", type=["wav", "mp3"])

def encode_audio(file):
    return base64.b64encode(file.read()).decode("utf-8")

# -------- BUTTON ----------
if st.button("Analyze Communication"):
    if not text_input and not audio_file:
        st.error("Please enter text or upload audio.")
    else:
        st.info("⏳ Analyzing...")

        # FAKE RESPONSE (demo only)
        result = {
            "emotion": {
                "joy": 0.42,
                "sadness": 0.10,
                "anger": 0.05,
                "fear": 0.08,
                "surprise": 0.15,
                "disgust": 0.04,
                "neutral": 0.16
            },
            "confidence": 78,
            "clarity": 82,
            "energy": "Medium",
            "stress_risk": "Low",
            "advice": "Your tone sounds mostly positive. Slow down your pace slightly and maintain consistent volume."
        }

        st.success("✔ Analysis Complete!")

        st.subheader("📊 Emotion Breakdown")
        st.json(result["emotion"])

        st.subheader("🔥 Communication Scores")
        st.write(f"**Confidence:** {result['confidence']}%")
        st.write(f"**Clarity:** {result['clarity']}%")
        st.write(f"**Energy:** {result['energy']}")
        st.write(f"**Stress Risk:** {result['stress_risk']}")

        st.subheader("💡 Personalized Advice")
        st.write(result["advice"])

st.write("---")
st.caption("Demo version — backend not connected, using mock response.")
