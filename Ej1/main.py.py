from Email import Email
from os import path
import re
import csv

def EmailfromStr(string: str) -> Email:
	matches = re.search(r"(.+)@(.+)\.(.+)", string)
	if(matches == None):
		raise Exception("El Email no es valido")
		
	return Email(matches.group(1), matches.group(2), matches.group(3))

def leerArch(filePath: str) -> list[Email]:
	with open(filePath, "r") as file:
		reader = csv.reader(file, delimiter=',')
		next(reader, None)
		emails: list[Email] = []

		for line in reader:
			emails.append(EmailfromStr(line[0]))

		return emails

def test():
	email = Email("Agustin", "gmail", "com", "126")
	Email("Agustin", "gmail", "com")

	assert email.getDominio() == "gmail"
	assert email.getIDCuenta() == "Agustin"

if __name__ == "__main__":
	test()


	nombre = input("Nombre: ")
	email = Email(
		input("Nombre de usuario: "), 
		input("Dominio: "),
		input("Tipo de dominio: "),
		input("Contraseña: ")
	)


	print()
	print("Estimado " + nombre + " te enviaremos tus mensajes a la dirección " + email.retornaEmail())


	print()
	email.modificarContraseña(input("Contra Antigua: "), input("Contra Nueva: "))
	print()


	EmailfromStr(input("email: "))
	print()


	emailsDelArchivo = leerArch(path.dirname(__file__) + "/emails.csv")
	identificador = input("Ingresar identificador de cuenta: ")
	contador = 0

	for email in emailsDelArchivo:
		if email.getIDCuenta() == identificador:
			contador += 1
	
	if contador == 0:
		print("El email con ese identificador no existe")
	elif contador == 1:
		print("El email con ese identificador es unico")
	else:
		print("El email con ese identificador esta repetido") # Agustindormi1 es el unico repetido
