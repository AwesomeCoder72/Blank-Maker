"""
THE PLAN:

    1. Input a text file and the amount of words to be blanked
    2. Output a text file with the amount of words blanked

Different input types:
    Start with:
    - Words total
    Later:
    - Words per line
    - part of speech
"""
import random

def blanken_file(split_total, file_name = "text-input.txt"):
    file_text = open(file_name).read() # Opens and reads the file
    split_text = file_text.split() # Splits the text
    
    for i in range(split_total+1):
        found_word = False
        while not found_word:
            pick_from_list = random.randint(0, split_total)
            if pick_from_list == "___":
                continue
            else:
                split_text[pick_from_list] = "___"
                found_word = True
            
    with open(file_name, "w") as file:
        file.write(" ".join(split_text))
    
    print(split_text)
            
blanken_file(5)
