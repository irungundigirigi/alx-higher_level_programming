#!/usr/bin/python3
"""

Module of a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    str = text[:]

    for d in ".?:":
        list_text = str.split(d)
        str = ""
        for i in list_text:
            i = i.strip(" ")
            str = i + d if str is "" else str + "\n\n" + i + d

    print(str[:-3], end="")