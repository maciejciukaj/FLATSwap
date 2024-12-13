import os

from Config.config_loader import load_model
from Utils.result_formatting import words_to_numbers


def transcription_service(audio_file_name):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    audio_file_path = os.path.join(base_path, "Transmissions", f"{audio_file_name}")
    result_file_path = os.path.join(base_path, "Results", f"{audio_file_name}.txt")
    model = load_model()
    result  = model.transcribe(f"{audio_file_path}.wav", language="en", task="transcribe", without_timestamps=True)

    transcribed_message = words_to_numbers(result["text"])

    result_file = f"{audio_file_name}.txt"

    with open(result_file_path, "w", encoding="utf-8") as f:
        f.write(transcribed_message)

    print(f"Transcription saved in: {result_file}")