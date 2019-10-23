input_list = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
value = "Re"

count = 0

for item in input_list:
    count = count + 1
print(count)
input_list[count:count] = [value]
print(input_list)