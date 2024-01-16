import sys

file = open(sys.argv[1], 'r')
text = file.read()
filtered_lines = [line for line in text.split('\n') if not line.startswith('#')]

# Join the lines back into a string
result_text = '\n'.join(filtered_lines)

# Split the text by empty lines
data_parts = result_text.split('\n\n')

# Create an array for each part
string_arrays = [part.split('\n') for part in data_parts]

result_arrays = []
current_array = []

for item in string_arrays[0]:
    s = item.strip().split('\t')
    if len(s[0]) == 1 and int(s[0]) == 1:
        if current_array:
            result_arrays.append(current_array)
        current_array = [item]
    else:
        current_array.append(item)

# Adding the last array if any
if current_array:
    result_arrays.append(current_array)

with open('result.txt', 'w') as file:
    for arr in result_arrays:
        new_arr0 = arr[0].split('\t')
        new_arr1 = arr[len(arr) - 1].split('\t')
        if len(new_arr1) > 7 and len(new_arr0) > 7:
            tkn_n = new_arr1[0]
            tkn1 = new_arr0[0]
            if len(tkn_n) < 3 and len(tkn1) < 3:
                tkn1 = int(tkn1)
                tkn_n = int(tkn_n)
                for i in arr:
                    arr = i.strip().split('\t')
                    if len(arr) > 7 and len(arr[0]) < 3 and arr[0].isdigit() and arr[6].isdigit():
                        if int(arr[6]) == (int(arr[0]) + 1) or int(arr[6]) == (int(arr[0]) - 1):
                            # print(f"{arr[0]}\t{arr[6]}")
                            file.write(f"{i}\n")
                        elif (int(arr[6]) >= tkn1) and (int(arr[6]) <= tkn_n):
                            # print(f"{arr[0]}\t{arr[6]} - NP")
                            file.write(f"{i} - NP\n")
                        elif int(arr[6]) == 0:
                            # print(f"{arr[0]}\t{arr[6]}")
                            file.write(f"{i}\n")
                    else:
                        file.write(f"{i}\n")
                file.write("\n")
    file.write("\n")