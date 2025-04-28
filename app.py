import streamlit as st
import streamlit.components.v1 as components
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
import time

# Set up API key
google_api_key = st.secrets["GOOGLE_API_KEY"]

# Initialize Gemini model
chat_model = ChatGoogleGenerativeAI(
    google_api_key=google_api_key,
    model="gemini-2.0-flash-exp",
    temperature=1
)

# Set Streamlit page
st.set_page_config(layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: green;'>🌱 AI Plant Disease Analyzer 🌿</h1>",
    unsafe_allow_html=True
)

# Fun animation (falling leaves)
snowfall_html = """
<div id="snow-container"></div>
<style>
  #snow-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; }
  .snowflake { position: absolute; font-size: 15px; opacity: 0.9; user-select: none; }
</style>
<script>
  function createSnowflake() {
    let snowflake = document.createElement('div');
    snowflake.innerHTML = '🍃';
    snowflake.classList.add('snowflake');
    snowflake.style.left = Math.random() * window.innerWidth + 'px';
    snowflake.style.top = '-20px';
    snowflake.style.fontSize = Math.random() * 20 + 10 + 'px';
    snowflake.style.color = '#00a86b';
    document.getElementById('snow-container').appendChild(snowflake);

    let speed = Math.random() * 3 + 2;
    let angle = Math.random() * 2 - 1;

    function fall() {
      if (parseFloat(snowflake.style.top) < window.innerHeight) {
        snowflake.style.top = parseFloat(snowflake.style.top) + speed + 'px';
        snowflake.style.left = parseFloat(snowflake.style.left) + angle + 'px';
        requestAnimationFrame(fall);
      } else {
        snowflake.remove();
      }
    }
    fall();
  }
  setInterval(createSnowflake, 300);
</script>
"""
components.html(snowfall_html, height=150)

# Sidebar: Language selection
st.sidebar.header("🌍 Select Output Language")
languages = {
    "English": "English",
    "Hindi": "Hindi",
    "Japanese": "Japanese",
    "French": "French",
    "Telugu": "Telugu",
    "Spanish": "Spanish",
    "German": "German",
    "Chinese": "Chinese",
    "Russian": "Russian",
    "Arabic": "Arabic",
    "Portuguese": "Portuguese",
    "Italian": "Italian",
    "Dutch": "Dutch"
}
selected_language = st.sidebar.radio("Choose a language:", list(languages.keys()))

# Two-column layout
col1, col2 = st.columns([1, 2])

# Left column: Upload image
with col1:
    st.subheader("📸 Upload Plant Image")
    uploaded_file = st.file_uploader("Upload a plant image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

# Right column: Show results
with col2:
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Plant Image", use_container_width=True)

        if st.button("🔎 Analyze Plant Health"):
            try:
                image_bytes = uploaded_file.read()

                # Convert image to base64 data URL
                base64_image = base64.b64encode(image_bytes).decode("utf-8")
                image_data_url = f"data:image/jpeg;base64,{base64_image}"

                # Create HumanMessage with text and image_url
                message = HumanMessage(
                    content=[
                        {
                            "type": "text",
                            "text": f"You are an expert agricultural assistant. Please analyze the plant image and provide the following details:\n"
                                    f"1. Name of disease (if any)\n"
                                    f"2. Description of symptoms\n"
                                    f"3. Suggested treatment or medicine\n"
                                    f"4. Specialized doctor recommendations for further diagnosis and treatment:\n"
                                    f"    - Plant Pathologist: For detailed analysis of plant diseases\n"
                                    f"    - Horticulturist: For guidance on plant care and treatment\n"
                                    f"    - Agricultural Scientist: For research-based treatment options\n"
                                    f"    - Pest Management Specialist: To identify and handle pest-related issues\n"
                                    f"5. Where to go for further assistance:\n"
                                    f"    - Local Agricultural Extension Office for expert consultations\n"
                                    f"    - Local Plant Clinics for in-person diagnosis and care\n"
                                    f"    - Online consultation platforms like [PlantNet](https://plantnet.org) for immediate advice\n"
                                    f"Please answer in {languages[selected_language]}. Use bullet points."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": image_data_url}
                        }
                    ]
                )

                
                response = chat_model.invoke([message])

                st.success("✅ Analysis Complete!")
                st.markdown(f"### 📋 Results in {selected_language}:")
                st.write(response.content)

                # 🎉 Confetti effect after success
                time.sleep(1)
                st.balloons()
                st.toast('🎉 Thank you for using AI Plant Analyzer!', icon='🌿')

                # Result text
                result_text = response.content
                

            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")
    else:
        st.info("📥 Please upload an image to start analysis.")
