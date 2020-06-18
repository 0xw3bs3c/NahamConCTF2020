from base64 import b64decode

def checkChar(res):
    for ch in res:
        if ch <=126 and ch>=33:
            pass 
        else:
            return False
    
    return True

prompt = list('zmxhz3tkb2vzx3roaxnfzxzlbl9jb3vudf9hc19jcnlwdg9vb30=')

final = ''
for i in range(0, len(prompt), 4):
    for j in range(0, 2**4):
        curr_char = prompt[i:i+4].copy()
        for k in range(0, 4):
            if(j & (1<<k)):
                curr_char[k] = curr_char[k].upper()
            
        curr_res = b64decode(''.join(curr_char))
        if (checkChar(curr_res)):
            final += curr_res.decode('ASCII')
            break

print(final)
        
