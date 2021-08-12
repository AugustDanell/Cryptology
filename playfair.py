def split_into_group_of_five(l):
    return [l[0:5],l[5:10],l[10:15],l[15:20], l[20:]]

# 1. Initiate a table:
occured_letters = {}
table = []

# 2.1 Generate table with keyphrase:
keyphrase = list(input())
for i in keyphrase:
    if(not occured_letters.__contains__(i) and i.isalpha() and not i == 'q'):
        occured_letters[i] = True
        table.append(i)

# 2.2 Generate table by letting the rest of the alphabet to follow:
for i in range(26):
    small_letter = chr(97 + i)

    if(not occured_letters.__contains__(small_letter) and not small_letter == 'q'):
        occured_letters[small_letter] = True
        table.append(small_letter)

# ok! --> print(split_into_group_of_five(table))

# 3. Encryption:
plain_text = list(input())
