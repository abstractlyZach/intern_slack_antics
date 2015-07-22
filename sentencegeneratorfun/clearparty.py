import re

try:
    file = open('newparty.txt', 'r+', encoding = 'utf-8')

    inp = str()
    
    while inp != 'go away':
        
        file.seek(0)

        text = file.read()[:]

        file.seek(0)

        file.truncate()

        inp = input('select regular expression to replace with ""')

        text = re.sub(inp, '', text)

        file.write(text)

    
        


finally:
    file.close()
