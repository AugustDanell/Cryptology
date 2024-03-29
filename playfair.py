def split_into_group_of_five(l):
    ''' split_into_group_of_five
        As the name suggests, this function takes in a list and splitts it up into groups of five. It can be made to fit into any arbitary size but here it goes up to size 25 because
        it is specifically tailored to the playfair cipher, that needs 5 rows of 5 letters, omitting the 'q' specifically.
    '''

    return [l[0:5],l[5:10],l[10:15],l[15:20], l[20:]]

def split_into_pairs(l):
    ''' split_into_pairs
        Similar to the split_into_groups_of_five function but instead splits it up into pairs. 
    '''

    new_list = []
    for i in range(1, len(l), 2):
        new_list.append(l[i-1:i+1])

    if(len(l) % 2 == 1):
        new_list.append([l[-1]])

    return new_list

def transform_digraphs(digraph_list):
    ''' transform_diagraphs
        Applying the rules on each diagraph as per the playfair cipher instructions.
    '''

    made_transform = False
    # rule 1:
    

    return made_transform

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
plain_text = list(input().replace(" ", ""))
digraph_list = split_into_pairs(plain_text)

while(transform_digraphs(digraph_list)):
    pass

