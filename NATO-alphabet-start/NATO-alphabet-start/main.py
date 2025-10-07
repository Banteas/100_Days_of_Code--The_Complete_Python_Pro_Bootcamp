import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonet_dict = {row.letter:row.code for (index,row) in data.iterrows()}
def generate_phonetic():
    while True:
        name_input = input("Enter a name: ").upper()
        try:
            output_name = [phonet_dict[letter] for letter in name_input]
        except KeyError:
            print("Invalid input. Please enter only alphabet letters.")
            generate_phonetic()
        else:
            print(output_name)
            break


generate_phonetic()
