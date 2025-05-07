from caeser_art import art
print(art)

# encrypt and decrypt function is minimized into caeser function for more readability

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#
#     for n in original_text:
#         shifted_position = alphabet.index(n) + shift_amount
#
#         shifted_position = shifted_position % len(alphabet)
#         cipher_text += alphabet[shifted_position]
#
#     print("Here is the encoded result: "+cipher_text)
#
#
# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for n in original_text:
#         shifted_position = alphabet.index(n) - shift_amount
#         shifted_position = shifted_position % len(alphabet)
#         cipher_text += alphabet[shifted_position]
#
#     print("Here is your decoded result: "+cipher_text)


def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for n in original_text:

        if n not in alphabet:
            cipher_text += n

        shifted_position = alphabet.index(n) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")




# encrypt(text,shift)
# decrypt(text,shift)
should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' to go again. Otherwise, type 'no' \n ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

