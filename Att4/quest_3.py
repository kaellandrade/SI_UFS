def invertString(string):
    '''
        Entrada: String s 
        Saida: String s invertida, porém com o primeiro caracter no final.
    '''
    M = len(string)-1
    nova_string = ''
    lastChar = ''
    for i in range(M, -1, -1):
        if(i!=M):
            nova_string += string[i]
        else:
            lastChar = string[i]
        
    
    return nova_string + lastChar


print(invertString('casa'))
