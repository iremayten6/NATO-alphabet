
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
#print(type(data))
pho_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(pho_dict)

word = input("Enter a word: ").upper()
output = [pho_dict[letter] for letter in word]
print(output)
