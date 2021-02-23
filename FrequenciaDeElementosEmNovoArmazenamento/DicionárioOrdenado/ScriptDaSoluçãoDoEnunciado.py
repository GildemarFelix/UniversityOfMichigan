
'''entrada'''
fname = input("Enter file name: ")  
fh = open(fname)                    
lista=list()                        
dic=dict()

'''encontra horário o qual é adicionado no dicionário dic para
   mapeamento da ordem e frequência dos horários'''
for line in fh:
    if line.startswith('From'):
        a=line.split()
        if a[0] != 'From:':
            b = line.find(':')
            c = line[b-2:b]
            dic[c]=dic.get(c,0)+1

'''saída'''
'''ordena os horários e os imprime com a respctiva frequência'''
for key, value in sorted(dic.items()):
    print(key,value)

fh.close()
