'''entrada'''
fname = input("Enter file name: ")
fh = open(fname)
PrimeiraLista = list()
SegundaLista = list()

'''base fixa: cria a PrimeiraLista com as posições em formato listas de strings'''
'''exemplo: [['bla','bla','bla'],['ok','ok']]'''
for line in fh:
    PrimeiraLista.append(line.split())

'''ajusta a PrimeiraLista em uma única lista'''
'''exemplo: ['bla','bla','bla','ok','ok']'''
for l in PrimeiraLista:
    for i in l:
        SegundaLista.append(i)

'''procura item repetido e o elimina'''
i=0
while i < len(SegundaLista):
    j=i+1
    while j < len(SegundaLista):
        if SegundaLista[i]==SegundaLista[j]:
            SegundaLista.pop(j)
        else :
            j+=1

    i+=1

'''coloca a SegundaLista em ordem alfabetica'''
SegundaLista.sort()  
       
'''saída'''
print(SegundaLista)
fh.close()

