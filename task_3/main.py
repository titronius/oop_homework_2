files_names = ['1.txt', '2.txt', '3.txt']

list_of_string = []
for file_name in files_names:
    with open(f'files/{file_name}') as f:
        string_array = []
        for l in f:
            string_array.append(l.strip())
        string_array = [file_name] + [str(len(string_array))] + string_array
        list_of_string.append(string_array)

list_of_string.sort(key = lambda part:part[1])

final_string = ""
for i, part in enumerate(list_of_string):
    if i != 0:
        final_string += '\n'
    final_string += '\n'.join(part)

with open('files/result.txt','w') as f:
    f.write(final_string)
