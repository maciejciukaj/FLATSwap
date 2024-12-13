import torch
import whisper

from Utils.result_formatting import words_to_numbers

if torch.cuda.is_available():
    print("CUDA available")
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available")

model = whisper.load_model("medium", device="cuda")

audio_file = "rus_2024-12-10T15_31_55Z_12139.0kHz"

result  = model.transcribe(f"Transmissions\\{audio_file}.wav", language="en", task="transcribe", without_timestamps=True)
print(result)
print(result["text"])
print(words_to_numbers(result["text"]))

result_file = f"{audio_file}.txt"

with open(f"Results/{result_file}", "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcription saved in: {result_file}")

