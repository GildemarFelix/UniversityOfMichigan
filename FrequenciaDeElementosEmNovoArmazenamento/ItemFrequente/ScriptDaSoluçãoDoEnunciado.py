'''entrada'''
fname = input("Enter file name: ")  
fh = open(fname)                    
lista=list()                        
dic=dict()


'''encontra e-mail o qual é adicionado no dicionário dic para
   o mapeamento do e-mail mais frequente'''
for line in fh:
    if line.startswith('From'):
        a=line.split()
        if a[0] != 'From:':
            pos=a[1]
            dic[pos]=dic.get(pos,0)+1

'''encontra o e-mail mais frequente'''
ValueFrequente=None
KeyFrequente=None
for key,value in dic.items():
    if ValueFrequente is None or value > ValueFrequente:
        KeyFrequente=key
        ValueFrequente=value

'''saída'''
print(KeyFrequente,ValueFrequente)
fh.close()
