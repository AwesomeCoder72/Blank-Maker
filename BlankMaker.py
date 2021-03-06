"""
THE PLAN:

    1. Input a text file and the amount of words to be blanked
    2. Output a text file with the amount of words blanked

Different input types:
    Working on:
    - Don't blank certain list of words
    Later:
    - part of speech
    Finished:
    - Words per line
    - Sort out punctuation
    - Words total
"""
import random
import re

file_path = r"\Users\Noah\Documents\Programs\Python Programs\BlankMaker\text-input.txt"

def blanken_file_by_line(split_total, file_name = file_path):
    output_list = []
    with open(file_name, 'r') as file:
        file_lines = file.read().split("\n")
        
    output_list = [re.findall(r"[\w']+|[.,!?;:]", unsplit)
                       for unsplit in file_lines]
    print(output_list)
    
    for line in output_list:
        if len(line) <= split_total:
            amount_to_split = int(len(line) / 2)
        else:
            amount_to_split = int(split_total)
        for i in range(amount_to_split):
            found_word = False
            while not found_word:
                pick_from_list = random.randint(0, len(line)-1)
                if line[pick_from_list] == "___" or\
                not line[pick_from_list] or\
            re.match("^[.,!?;:]+$", line[pick_from_list]):
                    continue
                else:
                    line[pick_from_list] = "___"
                    found_word = True
    output = "\n".join([re.sub(r' (?=\W)', '', " ".join(i)) for i in 
                        [line for line in output_list]])
    print(output)
    with open(file_name, "w") as file:
        file.write(output)
            
def blanken_file_by_total(split_total, file_name = file_path):
    with open(file_name, 'r') as file:
        file_lines = file.read().split("\n")
    output_list = [re.findall(r"[\w']+|[.,!?;:]", unsplit)
                       for unsplit in file_lines]
            
    for i in range(split_total):
        found_word = False
        while not found_word:
            pick_from_list = random.randint(0, len(output_list)-1)
            pick_from_line = random.randint(0, len(output_list[pick_from_list])-1)
            if output_list[pick_from_list][pick_from_line] == "___" or\
            not output_list[pick_from_list][pick_from_line] or\
            re.match("^[.,!?;:]+$", output_list[pick_from_list][pick_from_line]):
                continue
            else:
                output_list[pick_from_list][pick_from_line] = "___"
                found_word = True
    output = "\n".join([re.sub(r' (?=\W)', '', " ".join(i)) for i in 
                        [line for line in output_list]])
    with open(file_name, "w") as file:
        file.write(output)

blanken_file_by_line(4)