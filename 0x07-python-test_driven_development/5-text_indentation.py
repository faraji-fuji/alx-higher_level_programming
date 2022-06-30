#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """replace the characters ., ? and : for a 2 blank_lines

    Args:
        text (str): str that will be modified

    Returns:
        prints the new text

    Raises:
        TypeError: if text is not a str

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    replacers = ".?:"

    text = text.strip()

    for replacer in replacers:
        text = text.replace(replacer, "{}\n\n".format(replacer))

    print("\n".join([li.strip() for li in text.split("\n")]), end="")
