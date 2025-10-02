
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonet_dict = {row.letter:row.code for (index,row) in data.iterrows()}

name_input = input("Enter a name: ").upper()
output_name = [phonet_dict[letter] for letter in name_input]
print(output_name)