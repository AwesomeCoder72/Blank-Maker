"""
THE PLAN:

    1. Input a text file and the amount of words to be blanked
    2. Output a text file with the amount of words blanked

Different input types:
    Working on:
    - Words per line
    Later:
    - Sort out punctuation
    - part of speech
    Finished:
    - Words total
"""
import random

def blanken_file_by_total(split_total, file_name = "text-input.txt"):
    output_list = []
    with open(file_name, 'r') as file:
        file_lines = file.read().split("\n")
        
    output_list = [line.split() for line in file_lines]
    print(output_list)
    
    for line in output_list:
        for i in range(split_total+1):
            found_word = False
            while not found_word:
                pick_from_list = random.randint(0, split_total)
                if pick_from_list == "___":
                    continue
                else:
                    line[pick_from_list] = "___"
                    found_word = True
            
    output = "\n".join([" ".join(i) for i in output_list])
    
    with open(file_name, "w") as file:
        file.write(output)
            
blanken_file_by_total(2)
