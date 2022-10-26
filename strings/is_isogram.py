"""
wiki: https://en.wikipedia.org/wiki/Heterogram_(literature)#Isograms
"""
import re


def is_isogram(string: str) -> bool:
    """
    An isogram is a word in which no letter is repeated. 
    Examples of isograms are uncopyrightable and ambidextrously.
    >>> is_isogram('Uncopyrightable')
    True
    >>> is_isogram('allowance')
    False
    >>> is_isogram('copy1')
    ValueError: String must only contain alphabetic characters.
    """
    if bool(re.search(r'\d', string)):
        raise ValueError("String must only contain alphabetic characters.")

    letters = sorted(string.lower())
    return len(letters) == len(set(letters))


if __name__ == "__main__":
    input_str = input("Enter a string ").strip()

    isogram = is_isogram(input_str)
    print(f"{input_str} is {'an' if isogram else 'not an'} isogram.")
