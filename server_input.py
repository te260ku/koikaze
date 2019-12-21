import socket
import led_sound
import main
import RPi.GPIO as GPIO

host_ip = "192.168.100.129"        #ホストのIPを取る
port = 1890

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ソケット作成

server.bind((host_ip, port))                                #IPとポート結び付け

server.listen(1)                                            #接続数

print ("[*]Server waiting on %s : %s" % (host_ip, port))    

client, addr = server.accept()                              

print ("[Connection from %s:%s ]" % (addr[0], addr[1])) 

# ここまででコネクション確立



def decode(response):                                       #デコード 
    response = response.decode()

    # exitで両者が終了する
    if response == "exit":                                  #終了条件
        print ("////Finish Connect////")
        client.close()
        exit()

    return response



while True:
    try:
        response_data = client.recv(1024)                       #データ受け取り
        response_data = decode(response_data)

        if response_data == 'on':
            print ("ON")
        # led_sound.main()
            main.main()
    except KeyboardInterrupt:
        client.close()
        GPIO.cleanup()
