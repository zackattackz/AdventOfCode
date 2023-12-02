from ._1 import answer as answer_one


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
    "nine": "9",
}


def convert_words(amended_val, word_to_digit):
    """
    Replaces the words in an amended value with
    their digit equivalents

    :param amended_val: The amended value to replace in
    :param word_to_digit: Dict mapping words to digits for the replacement
    """

    words = word_to_digit.keys()

    # Replace all words in amended_val with it's
    # corresponding digit, keeping the first and last letters
    # of the word on the left and right side.
    for word in words:
        amended_val = amended_val.replace(
            word, word[0] + word_to_digit[word] + word[-1]
        )

    return amended_val


def answer(file):
    """
    The solution for this part.

    :param file: The problem input.
    :return: The problem solution.
    """

    simplified_file = [convert_words(line, word_to_digit) for line in file]
    return answer_one(simplified_file)
