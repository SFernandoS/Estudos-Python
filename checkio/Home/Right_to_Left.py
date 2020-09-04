"""
    https://py.checkio.org/en/right-to-left/
"""

def left_join(phrases: tuple) -> str:
    phrases = ','.join(phrases)
    phrases = phrases.replace('right','left')
    
    return phrases
