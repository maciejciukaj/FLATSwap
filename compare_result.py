def clean_sequence(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned_sequence = " ".join(content.replace(",", " ").split())
    return cleaned_sequence


def compare_sequences(seq1_str, seq2_str):
    seq1 = list(map(int, seq1_str.split()))
    seq2 = list(map(int, seq2_str.split()))

    differences = [
        {"index": i, "seq1": seq1[i], "seq2": seq2[i]}
        for i in range(min(len(seq1), len(seq2))) if seq1[i] != seq2[i]
    ]

    extra_elements = {
        "longer_sequence": "seq1" if len(seq1) > len(seq2) else "seq2",
        "extra_elements": seq1[len(seq2):] if len(seq1) > len(seq2) else seq2[len(seq1):]
    } if len(seq1) != len(seq2) else None

    return {
        "differences": differences,
        "extra_elements": extra_elements
    }


result_path = "result.txt"
expected_path = "Tests/test_data/expected.txt"

actual = clean_sequence(result_path)
expected = clean_sequence(expected_path)

comparison_result = compare_sequences(actual, expected)

if not comparison_result["differences"] and not comparison_result["extra_elements"]:
    print("Strings are the same.")
else:
    print("Różnice:")
    for diff in comparison_result["differences"]:
        print(f"Indeks: {diff['index']}, actual: {diff['seq1']}, expected: {diff['seq2']}")

    if comparison_result["extra_elements"]:
        print("\nAdditional elements:")
        print(f"{comparison_result['extra_elements']['longer_sequence']}: {comparison_result['extra_elements']['extra_elements']}")
