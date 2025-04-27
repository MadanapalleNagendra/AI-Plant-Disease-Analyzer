# 🌱 AI Plant Disease Analyzer 🌿

This is an AI-powered application built with **Streamlit** and **Google's Gemini Model** via **Langchain** to analyze plant health based on uploaded images. The app helps identify potential diseases in plants, provide symptoms, treatments, and recommendations, and also allows users to download the results in PDF or text format.

## Features:
- **Image Upload:** Users can upload an image of a plant for analysis.
- **Disease Analysis:** The app uses AI to analyze the plant image and detect diseases, providing:
  1. Disease name (if any)
  2. Symptoms description
  3. Suggested treatment
  4. Recommendations for further professional help (Plant Pathologist, Horticulturist, etc.)
  5. Suggestions for where to seek help (local clinics, online platforms)
- **Language Support:** Users can choose from a variety of languages for the analysis results (English, Hindi, Japanese, etc.).
- **PDF & TXT Download:** Users can download the analysis results as a PDF or plain text.

## Requirements:
To run the app, make sure you have the following Python packages installed:

- `streamlit`
- `langchain`
- `requests`
- `fpdf`

You can install these packages using the following command:

```bash
pip install -r requirements.txt
