"""
    https://py.checkio.org/mission/right-to-left/solve/
"""

def left_join(phrases: tuple) -> str:
    phrases = ','.join(phrases)
    phrases = phrases.replace('right','left')
    
    return phrases
