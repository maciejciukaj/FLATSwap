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

    result = []
    for word in words:
        if word in word_to_digit:
            result.append(word_to_digit[word])
        elif word.isdigit():
            result.append(word)

    return ' '.join(result)