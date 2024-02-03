class Morse:
    """
    Encodes input into morse code.
    """
    def __init__(self, value: str):
        MorseCode = {"a": "._", 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....', 'i': '..', 'j': '.___', 'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '...', 'p': '.__.', 'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._', 'y': '_.__', 'z': '__..', '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____', '.': '._._._', '!': '_._.__', '?': '..__..', ',': '__..__'}
        self.MorseDic = MorseCode
        text = list(value)
        final = ''
        for letter in text:
            if letter == ' ':
                final = final + " / "
            elif letter == '\n' or letter == '␤':
                final = final + " / "
            else:
                try:
                    final = final + MorseCode[str(letter.lower())]
                except Exception as _:
                    final = final + MorseCode[str(letter)]
        self.Morsevalue = final
        self.Value = value
    
    def __repr__(self):
        return self.Morsevalue

class ShiftEncoder:
    """
    Shifts every letter input by the `shift` value (default = 15)
    """
    def __init__(self, value: str, shift: int = 15):
        letters = list("abcdefghijklmnopqrstuvwxyz")
        self.LetterDic = letters
        text = list(value)
        final = ''
        for letter in text:
            final = final + letters[(letters.index(letter.lower()) + shift) % len(letters)]
        self.EncodedValue = final
        self.Value = value
        self.shift = shift
    
    def __repr__(self):
        return self.EncodedValue
    
    def __eq__(self, __value: object) -> bool:
        if self.Value == __value:
            return True
        return False
