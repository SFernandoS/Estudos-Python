""" 
    https://py.checkio.org/en/first-word/
"""

def first_word(text: str) -> str:
    text = text.replace(',',' ')
    text = text.replace('.',' ')
    text = text.split()

    return text[0]


print(first_word("... greating, happy"))