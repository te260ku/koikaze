import socket


target_host = "192.168.100.123"                       
target_port = 1890

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #ソケット作成
client.connect((target_host, target_port))                      #サーバのIPとポートで接続 

print ("Connect Success!! %s : %s" % (target_host, target_port))



def input_encode():                                             #エンコード
    data = input("[Client] > ")

    if data == "exit":                                          #終了条件
        client.send(b'exit')
        print ("////Finish Connect////")
        client.shutdown(1)
        client.close()
        exit()

    data = data.encode('utf-8')
    return data

def decode(response):                                           #デコード
    response = response.decode()

    if response == "exit":                                      #終了条件
        print ("////Finish Connect////")
        client.close()
        exit()

    return response

while True:
    client.send(input_encode())         

    response = client.recv(4096)                                #データ受け取り

    response = decode(response)                                 #受け取りデータをデコード
    print ("[Server] > %s " % (response))                