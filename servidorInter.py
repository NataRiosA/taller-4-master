# Python 3.7
import socketserver
import socket
import threading

host1 = ""
puerto1 = ""
operacion1 = ""

# Clase socket servidor qeu se conecta con el servidor especifico
class miHandler(socketserver.BaseRequestHandler):

	def handle(self):

		# Recibe datos de operacion que se debe realizar y convierte a String
		self.dirSerFinal = str(self.request.recv(1024).decode("UTF-8"))
		print("La direccion es =", self.dirSerFinal)
		# Convertimos a lista
		self.listaDir = self.dirSerFinal.split()
		global operacion1
		operacion1 = self.listaDir[2]

		if operacion1 == 'suma':
			global host1
			host1 = self.listaDir[0]
			global puerto1
			puerto1 = self.listaDir[1]

		elif operacion1 == 'resta':
			global host2
			host2 = self.listaDir[0]
			global puerto2
			puerto2 = self.listaDir[1]
			

#Creando hilo para servidor
class serverThread2(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		print("\n\t\tTaller 4 \nServidor intermedio listado dinamico con hilos\n")
		print("\n\t Servidor intermedio escuchando...\n")
		print("Conexion establecida con servidor especifico...")
		host2 = "localhost"
		lspuerto2 = [9998, 9996]
		server1 = socketserver.TCPServer((host2, lspuerto2[0]), miHandler)
		server1.serve_forever()

		# Llamamos la clase socket servidor con los parametros de direccion y puerto
		server2 = socketserver.TCPServer((host2, lspuerto2[1]), miHandler)
		# Mantenemos al servidor en estado de escucha
		server2.serve_forever()


# # Clase socket servidor
class myHandler(socketserver.BaseRequestHandler):

	def handle(self):
		self.operacion = str(self.request.recv(1024).decode("UTF-8"))

		if self.operacion == '1':
			self.listaDir = []
			# Agregamos a lista
			self.listaDir.append(host1)
			self.listaDir.append(puerto1)
			# Convertimos de lista a string
			self.listaStringDir = ' '.join(self.listaDir)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir.encode("UTF-8"))

		elif self.operacion == '2':
			self.listaDir1 = []
			# Agregamos a lista
			self.listaDir1.append(host2)
			self.listaDir1.append(puerto2)
			# Convertimos de lista a string
			self.listaStringDir1 = ' '.join(self.listaDir1)

			# Enviamos respuesta de datos de direccion al cliente
			self.request.send(self.listaStringDir1.encode("UTF-8"))

		else:
			pass

# # Creando hilo para Clientes
class serverThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		# Direccion comunicacion cliente
		host3 = "localhost"
		puerto3 = 9999

		# Llamamos la clase socket servidor con los parametros de direccion y puerto
		serverCli = socketserver.TCPServer((host3, puerto3), myHandler)
		print("Conexion establecida con cliente")

		# Mantenemos al servidor en estado de escucha
		serverCli.serve_forever()


hiloServerEspecifico = serverThread2()
hiloServerEspecifico.start()
hiloServerCliente = serverThread()
hiloServerCliente.start()
# # hiloServerCliente.daemon = True
# # hiloServerCliente.join()
