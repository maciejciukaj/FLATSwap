import os
from Config.config_loader import load_model
from Database.db_operations import save_transcription_to_db
from Utils.result_formatting import words_to_numbers, parse_audio_file_name


def transcription_service(audio_file_name):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    audio_file_path = os.path.join(base_path, "Transmissions", f"{audio_file_name}")
    result_file_path = os.path.join(base_path, "Results", f"{audio_file_name}.txt")

    try:
        station_code, timestamp, frequency = parse_audio_file_name(audio_file_name)
    except ValueError as e:
        print(f"Error parsing file name: {e}")
        return

    model = load_model()
    result = model.transcribe(f"{audio_file_path}.wav", language="en", task="transcribe", without_timestamps=True)
    transcribed_message = words_to_numbers(result["text"])

    with open(result_file_path, "w", encoding="utf-8") as f:
        f.write(transcribed_message)

    print(f"Transcription saved in: {result_file_path}")

    try:
        save_transcription_to_db(station_code, timestamp, frequency, transcribed_message)
    except Exception as e:
        print(f"Error saving transcription to database: {e}")
