# How to use Morse()
## How to use Morse()
Morse(x) # Will turn the text stored in variable `x` into morsecode. Using strings directly also works. Only strings work, other data types, such as int, dont.
```py
text = "Text, ha ha"
text = Morse(text)
print(text) # Will print the variable `text` translated into morse code
text.Value # Will return the un-translated value of `text`
text.MorseValue # Will return the encoded value
text.MorseDic # Will return a dictionary containing every letter, and its value in morse code
text == "Text, ha ha" # Will return `True`. It compares the un-translated text stored in the variable `text` to the other string
text.MorseValue == "Text, ha ha" # Will return `False`. It compares the encoded value stored in `text` to the other string.
```

## Example

```py
from Encoder import Morse
from os import system as sys
from time import sleep as wait

import colorama

text = ""

while True:
    try:
        print(f"""{colorama.Style.BRIGHT}
{colorama.Fore.GREEN}Type `A` or `1` to encode a string.
{colorama.Fore.RED}Type `D` or `2` to decode the string.
{colorama.Fore.RESET}Current encoded string: {text}{colorama.Style.RESET_ALL}
""")
        inpt = input()
        if inpt == "A" or inpt == "a" or inpt == "1":
            text = Morse(input("Type a string: ")) # , int(input("Choose a shift: "))
        elif inpt == "D" or inpt == 'd' or inpt == '2':
            print("The decoded string is: ", text.Value)
        else:
            print("That's not a valid command!")
        wait(3)
        sys("cls")
    except KeyboardInterrupt as e:
        if input(f"{colorama.Style.BRIGHT}{colorama.Fore.RED}Are you sure you want to exit? Press enter if you don't. Type something and press enter if you do.\n{colorama.Style.RESET_ALL}> ") == "":
            pass
        else:
            exit(1)
```

[Linux Example.zip](https://github.com/cornusandu/Encoder/files/14151589/Linux.Example.zip)

[Windows Example.zip](https://github.com/cornusandu/Encoder/files/14151594/Windows.Example.zip)
