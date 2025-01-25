import re


def words_to_numbers(input_string):
    word_to_digit = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    words = input_string.lower().replace(",", " ").split()
    digits = [word_to_digit[word] if word in word_to_digit else word for word in words if word in word_to_digit or word.isdigit()]
    return ' '.join(digits)


def parse_audio_file_name(file_name):
    try:
        match = re.match(r"^(?P<station_code>[a-zA-Z0-9]+)_(?P<timestamp>[0-9T:_Z\-]+)_(?P<frequency>[0-9,\.]+)kHz$", file_name)
        if not match:
            raise ValueError(f"Invalid file name format: {file_name}")

        station_code = match.group("station_code")
        timestamp = match.group("timestamp")
        frequency = float(match.group("frequency").replace(",", "."))

        return station_code, timestamp, frequency
    except Exception as e:
        raise ValueError(f"Error parsing file name '{file_name}': {e}")
