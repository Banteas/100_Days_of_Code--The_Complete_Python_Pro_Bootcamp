alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_function = False
while not is_function:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        is_function = True
    else:
        print("Wrong input")
try:
    text = input("Type your message:\n").lower()
except ValueError:
    print("That's not a valid number!")
shift = int(input("Type the shift number:\n"))

def caesar(function_type, original_text, shift_amount):
    output_text = ""
    if function_type == "decode":
        shift_amount *= -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {function_type}d result: {output_text}")

caesar(function_type=direction, original_text=text, shift_amount=shift)