'''entrada'''
fname = input("Enter file name: ")  
fh = open(fname)                    
lista=list()                        

'''encontra os números solicitados do enunciado'''
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        b=line.find(':')            
        a=line[b+1:] 	                     
        lista.append(float(a))                    

'''efetua o cálculo da média'''
total=0
for index in lista:
    total=total+index
w=len(lista)    
media=float(total/w)

'''saída'''
print('Average spam confidence:',media)
fh.close()

