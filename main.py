import os
import PyPDF2
from google.cloud import texttospeech

# Set the input PDF file and output MP3 file paths
input_pdf_path = "pdfs/dummy.pdf"
output_audio_path = "mp3s/output.mp3"

# Read the PDF file
with open(input_pdf_path, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(reader.pages)
    text = ""

    # Extract text from each page
    for page in range(num_pages):
        text += reader.pages[page].extract_text()

# Initialize the Text-to-Speech API client
client = texttospeech.TextToSpeechClient()

# Set the input text and voice parameters
input_text = texttospeech.SynthesisInput(text=text)
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Set the audio configuration
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Generate the speech audio
response = client.synthesize_speech(
    input=input_text, voice=voice, audio_config=audio_config
)

# Save the audio to an MP3 file
with open(output_audio_path, "wb") as audio_file:
    audio_file.write(response.audio_content)

