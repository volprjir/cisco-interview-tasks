from word_counter.counter import count_words


def test_count_words():
    count_words("input.txt")
    with open("output.txt", "r") as file:
        expected_output = file.read()
    with open("output.txt", "r") as file:
        output = file.read()
    assert output == expected_output
