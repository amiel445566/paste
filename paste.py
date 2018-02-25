# example inputs
PEI1 = 'a\nb\nc\nddddddd\ne3'
PEI2 = '123\n@2\nffcg'
PEI3 = 'afc\ngg\nfyxz\nln\ny\nsldakfladshf\n...?__'
PEI4 = '\n\n\n3\n5'

# some examples
'''
print(paste(*paste_header(['a\nb\nc','1\n2\n3'],'x','n'),has_header=True,margin=3))
print(paste(PEI1, PEI2)) # 2 columns
print(paste(PEI1, PEI1)) # 2 identical columns
print(paste(PEI1, PEI2, PEI3, PEI4)) # 4 unique columns
print(paste(*paste_header([PEI1, PEI1], 'header1', 'header2'),
            has_header=True)) # 2 unique columns with header

print(paste(*paste_header([PEI1, PEI1, PEI3], 'header1', 'header2'),
            has_header=True)) # 3 columns with 1 unnamed header
            
print(paste(PEI3, PEI2, margin=14)) # 2 columns with varied margin spacing

print(
      paste(
            *paste_header(['eggs\nmilk\nbread\ncheese\ncheck for sale',
                           '$3.00\n$2.00\n$1.50\n$2.00'],
                          'items', 'price'),
            has_header=True,
            margin=3)) # a human readable example
'''

def paste(string1, string2, *strings, margin=1, has_header=False, depth=0):
    ''' a Python implementation of bash "paste" '''
    string1_list = string1.split('\n') # deconstruct inputs
    string2_list = string2.split('\n')
    result = ''

    if has_header: # adds a row separator to separate header from content
        if depth == 0:
            string1_list.insert(1, '-'*len(max(string1_list, key=len)))
        string2_list.insert(1, '-'*len(max(string2_list, key=len)))
    
    col_width = len(max(string1_list, key=len)) + margin
    col_height = len(max(string1_list, string2_list, key=len))

    string1_list += ['']*(col_height - len(string1_list)) # equate dimensions on s1/s2
    string2_list += ['']*(col_height - len(string2_list))

    for i in range(col_height):
        result += string1_list[i]
        if len(string2_list[i]) != 0: # ensures no trailing spaces
            result += ' '*(col_width - len(string1_list[i])) +\
                      string2_list[i]
        if i != col_height-1: # ensures no trailing newline
            result += '\n'
    
    if len(strings) == 0:
        return result
    else:
        return paste(result, strings[0],
                     *strings[1:],
                     margin=margin, # reassert kwrd args for recursion inheritence
                     has_header=has_header,
                     depth=depth+1) # for loop sensitive functions

def paste_lw(string1, string2, *strings):
    ''' a lightweight version of paste '''
    string1_list = string1.split('\n')
    string2_list = string2.split('\n')
    result = ''
    
    col_width = len(max(string1_list, key=len)) + 1
    col_height = len(max(string1_list, string2_list, key=len))

    string1_list += ['']*(col_height - len(string1_list)) # equate dimensions on s1/s2
    string2_list += ['']*(col_height - len(string2_list))

    for i in range(col_height):
        result += string1_list[i] +\
                  ' '*(col_width - len(string1_list[i])) +\
                  string2_list[i]
        if i != col_height-1:
            result += '\n'
    
    if len(strings) == 0:
        return result
    else:
        return paste(result, strings[0], *strings[1:])

def paste_header(list_of_strings, *headers):
    ''' for adding headers to columns '''
    for i in range(len(list_of_strings)):
        try:
            list_of_strings[i] = headers[i] + '\n' + list_of_strings[i]
        except IndexError:
            list_of_strings[i] = '-\n' + list_of_strings[i] # a default header
        
    return list_of_strings
