text = open('input.csv').read()
text = text.split('\n')
text = [x.split('\t') for x in text]

line1 = '    ' + 'description: ' + text[0][1]
line2 = '    ' + 'precondition: ' + text[2][1]
line3 = '    ' + 'trigger: ' + text[1][1]
line4 = '    ' + 'extensions: ' + text[3][1]
output = '\n'.join([line1, line2, line3, line4])

with open('output.csv', 'w') as file:
    file.write(output)
print("completed")
