ip = 'input.txt'
op = 'output.txt'

i = open(ip, 'r')
    
content = i.read()

i.close()

reversed_content = content[::-1]    
o = open(op, 'w')
o.write(reversed_content)
o.close()
print(f"Content reversed and saved to {op}")



