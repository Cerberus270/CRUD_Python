#Definimos un registro(lista) principal
registros=[]
while True:
	try:
		print(" Manejo de registros".center(70,"#"))
		print("1) Ingresar articulo")
		print("2) Consultar articulo")
		print("3) Comprar")
		print("4) Vender")
		print("5) Eliminar articulo")
		print("6) Salir")
		opc=int(input("Elija una opcion: "))
		if opc==1:
			cod=int(input("Ingrese el codigo: "))
			cant=int(input("Ingrese la cantidad: "))
			#Validamos la cantidad >0
			while cant<=0:
				print("La cantidad no puede ser negativa")
				print("Intente de nuevo")
				cant=int(input("Ingrese la cantidad: "))
			pre=float(input("Ingrese el Precio: "))
			#Validamos el precio >0
			while pre<=0:
				print("La cantidad no puede ser negativa")
				print("Intente de nuevo")
				pre=float(input("Ingrese la cantidad: "))
			nom=input("Ingrese el nombre ")
			#Creamos un registro de nodo
			reg=[cod,cant,pre,nom]
			#Agregamos el nodo al registro principal
			registros=registros+[reg]
		elif opc==2:
			c=int(input("Ingrese el codigo del articulo: "))
			#Definimos la variable centinela
			p=-1
			for i in range(len(registros)):
				if c==registros[i][0]:
					#Hacemos la variable centinela a la variable bandera
					p=i
					break
			if p<0:
				print("El articulo no existe")
			else:
				#Mostramos el articulo
				print("Articulo: ".center(70,'*'))
				print("Cantidad: ",registros[p][1])
				print("Precio: ",registros[p][2])
				print("Nombre: ",registros[p][3])
				print("".center(70,'*'))
		elif opc==3:
			c=int(input("Ingrese el codigo: "))
			p=-1
			for i in range(len(registros)):
				if c==registros[i][0]:
					p=i
					break

			if p<0:
				print("El articulo no existe")
			else:
				k=int(input("Ingrese la cantidad comprada: "))
				#Validamos la cantidad comprada > 0
				while k<=0:
					print("La cantidad no puede ser negativa")
					print("Intente de nuevo")
					k=int(input("Ingrese la cantidad comprada: "))
					#Hacemos el proceso de compra
				registros[p][1]=registros[p][1]+k
		elif opc==4:
			c=int(input("Ingrese el codigo del articulo: "))
			p=-1
			for i in range(len(registros)):
				if c==registros[i][0]:
					p=i
					break
			if p<0:
				print("El articulo no existe")
			else:
				k=int(input("Ingrese la cantidad vendida: "))
			#Validamos la cantidad vendida>0
			while k<=0:
				print("La cantidad no puede ser negativa")
				print("Intente de nuevo")
				k=int(input("Ingrese la cantidad comprada: "))
			#Mientras el valor egresado sea mayor a la cantidad del articulo
			#Volvelos a preguntar la cantidad, ahora mostrando cuando hay
			#En el inventario
			while k>registros[p][1]:
				#print ("la cantidad es mucho mayor, intente de nuevo")
				print("La cantidad que se encuentra disponible es: ",registros[p][1])
				k=int(input("Ingrese la cantidad comprada: "))
				while k<=0:
					print("La cantidad no puede ser negativa")
					print("Intente de nuevo")
					k=int(input("Ingrese la cantidad comprada: "))
			#Hacemos el proceso de ventas
			registros[p][1]=registros[p][1]-k
		elif opc==5:
			c=int(input("Ingrese el codigo del articulo: "))
			p=-1
			for i in range(len(registros)):
				if c==registros[i][0]:
					p=i
					break
			if p<0:
				print("El articulo no existe")
			else:
				#Eliminamos el nodo del registro principal
				del registros[p]
		elif opc==6:
			print("Adios")
			break
	#Por se registro, debe tener exepciones en caso que el usuario
	#ingresa cadena en vez de entero o flotante
	except (ValueError, NameError):
		print("No puede escribir una cadena, donde es entero o flotante".center(70,'!'))
		print("\n")
		#Volvemos al primer while
		continue
