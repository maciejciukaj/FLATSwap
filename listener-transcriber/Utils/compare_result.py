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
