import serial

def menu():
    print("Comandos disponibles")
    print("1 -> Encender led")
    print("0 -> Apagar led")
    print("q -> Salir")

print("Iniciando conexión...")
ser = serial.Serial('COM8', 115200)
print("Puerto serial conectado [OK]")
while True:
    print("Comandos disponibles")
    print("1 -> Encender led")
    print("0 -> Apagar led")
    print("q -> Salir")
    cmd = input("Digite el comando: ")
    if cmd == '1':
        ser.write('1'.encode())
        print("LED -> ON")
    elif cmd == '0':
        ser.write('0'.encode())
        print("LED -> OFF")
    elif cmd == 'q':
        ser.close()
        print("Puerto serial desconectado [OK]")
        break
    else:
        print("Comando invalido")
    print()
print("Hasta pronto")