import socket
import RPi.GPIO as GPIO
import time
import signal
import sys
import mpu6050

host = "192.168.100.119"                       
port = 1890

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #ソケット作成
client.connect((host, port))                      #サーバのIPとポートで接続 

print ("Connected %s : %s" % (host, port))


def handler(signum, frame):
    print ('Signal handler called with signal', signum)
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)


def decode(response):
    response = response.decode()

    if response == "exit":
        print ("Disconnected")
        client.close()
        exit()

    return response


while True:
    if mpu6050.get_motion() == True:
        print("start walking")

        if sendFlag == False:
            msg = 'on'
            client.send(msg.encode('utf-8'))
            sendFlag = True

    time.sleep(0.1)
