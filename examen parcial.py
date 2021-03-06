print('¡Hola a ,” todas “, y “, todos!,”,')


name = input('introduce tu nombre : ')
print('Hola', name)


v1=  int(input ('introduce un valor 0 o 1: '))
v2=   int (input('introduce un valor 0 o 1: '))
suma = v1 + v2 

if (suma==0):
 print('resultado= 0' )

if (suma>=1):
    print('resultado= 1 ')



    v3= int(input('escriba el total de horas estudiadas para programacion:  ' ))
    v4= int(input('escriba numero de horas diarias utilizadas: '))

promedio= v3/v4
print ('el promedio de horas diarias es = ', promedio)




v6=  int(input ('introduce tu peso en libras : '))
v7=  int(input ('introduce tu estatura en  metros :   '))

imc= v6/ (v7*v7)
print('su indice de masa corporal es :',"{:.2f}".format(imc))



v9=  int(input ('introduce el monton a depositar : '))
v10=  int(input ('introdusce el interes anual en porcentaje:  '))
v11=  int(input ('intruce el numerop de años: '))
v12=  v9/100*v10

capital= v12*v11
print('el capital obtenido en la inversion es: ',capital)



v12=  int(input ('introduce el monton de sierras a compar : '))
v14=  int(input ('introdusce el monto de barrenos a comprar:  '))
v15= (112*v14)+(75*v12)

print('el peso total en kg es de: ',v15)






v16=  int(input ('introduce el monton de tarjetas a comprar  : '))
v17= 60
v18= 20
  
descuento= v18/100*60
valorn= v16*v18
descuenton=v16*descuento 
valorf= v16*v18-descuenton

print('valor en dolares precio normal es:',valorn)
print('esta obteniendo un descuento en dolares de:',descuenton)
print('valor ya con el descuento aplicado en dolares es:',valorf)

https://github.com/eddy199908/examen-parcial.git