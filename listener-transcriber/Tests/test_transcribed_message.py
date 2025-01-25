import os

from Utils.compare_result import clean_sequence, compare_sequences


def test_compare_sequences():
    file_name = "sample_1.txt"
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    expected_file_path = os.path.join(base_path, "Tests/test_data", f"{file_name}")
    actual_file_path = os.path.join(base_path, "Results/", f"{file_name}")

    expected = clean_sequence(expected_file_path)
    actual = clean_sequence(actual_file_path)

    result = compare_sequences(expected, actual)

    if not result["differences"] and not result["extra_elements"]:
        print("Test passed: Messages are identical.")
        return True
    else:
        print("Test failed: Messages are different.")
        print("Differences:")
        for diff in result["differences"]:
            print(f"Position: {diff['index']}, actual: {diff['seq1']}, expected: {diff['seq2']}")
        if result["extra_elements"]:
            print("Extra elements:")
            print(f"{result['extra_elements']['longer_sequence']}: {result['extra_elements']['extra_elements']}")
        return False
