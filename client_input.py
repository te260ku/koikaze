import socket
import RPi.GPIO as GPIO
import time
import signal
import sys


target_host = "192.168.100.119"                       
target_port = 1890

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #ソケット作成
client.connect((target_host, target_port))                      #サーバのIPとポートで接続 

print ("Connect Success!! %s : %s" % (target_host, target_port))


buttonPin = 18
ledPin = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
before = 0
count = 0


def handler(signum, frame):
    print ('Signal handler called with signal', signum)
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)


def decode(response):                                           #デコード
    response = response.decode()

    if response == "exit":                                      #終了条件
        print ("////Finish Connect////")
        client.close()
        exit()

    return response



while True:
    now = GPIO.input(18)
    if before == 0 and now == 1:
        print("Push!!!")
        count += 1
        if sendFlag == False:
            if count%2 == 0:
                GPIO.output(ledPin, 1)
                msg = 'on'
                client.send(msg.encode('utf-8'))
                sendFlag = True
            else:
                GPIO.output(ledPin, 0)
                msg = 'off'
                client.send(msg.encode('utf-8'))
        else:
            break
    time.sleep(0.1)
    before = now
