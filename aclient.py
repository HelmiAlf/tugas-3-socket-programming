import socket
  
  
def Main(): 
    host = '3.86.87.188'
    port = 1235

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 

    run = True
    print("Write code below")
    while run: 
        message = input("")
        status = "Active"
        while len(message) > 0:
            # print(message)
            if message.lower() == "check status":
                print(status)

            if message.lower() == "stop":
                run = False
                break
            

            if message.lower() == "execute job light":
                s.send("a=2\nb=3\nresult=a*b".encode('ascii'))
                status = "Running"
            
            if message.lower() == "execute job medium":
                s.send("import time\ntime.sleep(5)\nresult=1\nfor i in range(200):\n\tresult*=5\nresult/=4".encode('ascii'))
                status = "Running"
            
            if message.lower() == "execute job heavy":
                s.send("import time\ntime.sleep(25)\na=4\nb=15\nresult=a**b".encode('ascii'))
                status = "Running"

            if message.lower() == "ping":
                s.send("PING".encode('ascii'))

            message = input("")

        data = s.recv(1024)

        print('Response received from the server : ',str(data.decode('ascii')))
        status = "Active"

    s.close() 
  
if __name__ == '__main__': 
    Main() 