import argparse
import re
from argparse import ArgumentParser
from collections import Counter


def count_words(file_path: str):
    try:
        with open(file_path, "r") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    # Use regex to extract words (considering words as sequences of alphanumeric characters)
    words = re.findall(r"\b\w+\b", text)

    word_count = Counter(words)

    # Sort primarily by frequency (descending) and secondarily by word (alphabetical)
    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    for word, count in sorted_word_count:
        print(f"{count} {word}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Count the frequency of words in a text file."
    )
    parser.add_argument("file_path", type=str, help="Path to the text file.")
    args = parser.parse_args()
    count_words(args.file_path)
