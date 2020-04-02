text = open('input.csv').read()
text = text.split('\n')
text = [x.split('\t') for x in text]

with open('output.csv', 'w') as file:
    for line in text:
        if line[0] == '':
            continue
        file.write(str(str(line)) + ',\n')
print("completed")
