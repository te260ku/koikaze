import socket
import RPi.GPIO as GPIO
import main

host = "192.168.100.129"
port = 1890

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(1)

print ("[*]Server waiting on %s : %s" % (host, port))    

client, addr = server.accept()                              

print ("[Connection from %s:%s ]" % (addr[0], addr[1])) 


def decode(response):
    response = response.decode()

    if response == "exit": 
        print ("////Finish Connect////")
        client.close()
        exit()

    return response


while True:
    try:
        response_data_raw = client.recv(1024)
        response_data = decode(response_data_raw)
        print(response_data)

        if response_data == 'on':
            main.main()

    except KeyboardInterrupt:
        client.close()
        GPIO.cleanup()
