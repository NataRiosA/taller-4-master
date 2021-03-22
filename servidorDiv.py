import socketserver
import socket
## Python 3.7

# Direccion y puerto local, comuncacion servidor intermedio
host = "localhost"
puerto = 9992
puertoDiv = "9991"
operacion = "division"

# Creamos los socket
socket1 = socket.socket()
# Establecemos conexion con servidor intermedio
socket1.connect((host, puerto))
listaDir = []
# Agregamos a lista
listaDir.append(host)
listaDir.append(puertoDiv)
listaDir.append(operacion)
# Convertimos de lista a string
listaStringDir = ' '.join(listaDir)
socket1.send(listaStringDir.encode("UTF-8"))


def division(numero1, numero2):
	return numero1 / numero2

# Clase socket servidor	division
class miHandler(socketserver.BaseRequestHandler):

	def handle(self):

		# Recibe 2 numeros, de a 1024 datos
		self.numero1 = str(self.request.recv(1024).decode("UTF-8"))
		#self.numero2 = int(self.request.recv(1024).decode("UTF-8"))
		print("los numeros recibidos son: ", self.numero1)
		# Convertimos a lista
		self.listaNum = self.numero1.split()
		# Convertimos a enteros para operar
		self.num1 = int(self.listaNum[0])
		self.num2 = int(self.listaNum[1])

		# Llamamos la funcion suma y Convertimos a String el resultado de la suma
		self.dividir = str(division(self.num1, self.num2))
		print("La division es =", self.dividir)

		# Enviamos el resultado
		self.request.send(self.dividir.encode("UTF-8"))


def main():
	print("\n\t\tTaller 4 \nServidor intermedio listado dinamico con hilos\n")
	print("Servidor Suma escuchando...")
	# Direccion comunicacion cliente
	host2 = "localhost"
	puerto2 = 9991

	# Llamamos la clase socket servidor con los parametros de direccion y puerto
	server1 = socketserver.TCPServer((host2, puerto2), miHandler)
	print("Servidor corriendo")
	# Mantenemos al servidor en estado de escucha
	server1.serve_forever()


main()
