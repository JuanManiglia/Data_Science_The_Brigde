abc = 'abcdefghijklmnñopqrstuvwxyz'
corrimiento = int(input('corrimiento: '))


for i in range(5):
    mensaje = input('mensaje: ').lower()
    mensaje_incrip = ""
    
    for i in mensaje:
        if i in abc:
            ind = abc.find(i)
            ind = (ind + corrimiento) % 27
            mensaje_incrip += abc[ind]
        
        else:
            mensaje_incrip += i
    
    print('*** men encrip: ', mensaje_incrip)
