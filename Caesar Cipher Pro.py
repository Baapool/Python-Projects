"""
A simple Caesar Cipher program that encrypts or decrypts text by shifting
letters through the alphabet. The user chooses encode/decode, enters a
message, selects a shift amount, and receives the transformed output.
"""
#Import and print the logo from art.py when the program starts.
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode": #User choice between Encode or Deocde.
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet: #If letter is not an alphabet.
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount #Moves the alphabet in the right position (adds) by the number of shift amount.
            shifted_position %= len(alphabet) # Adds every single letter in a string for showing a sentence.
            output_text += alphabet[shifted_position] #Text shown to the user.
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Ask the User to continue
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower() #Asks from the user for Encode or Decode.
    text = input("Type your message:\n").lower() #Text from the user.
    shift = int(input("Type the shift number:\n")) #Number of times user wants to move to the right (add) to the text's alphabets.

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) #Assigns user inputs to the function.

    ask = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n".lower()) #Asks if User wants to continue.
    if ask == "no":
        should_continue = False
        print("Goodbye!")
        input("How much do you rate this from 1 to 10: ")
