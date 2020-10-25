import socket 
import subprocess
 
from _thread import *
import threading 
  
print_lock = threading.Lock() 
  

def threaded(c): 
    name = str(threading.get_ident())
    while True: 
 
        code = c.recv(1024)
        msg = code.decode('ascii')
        print("Received message")
        if not code: 
            print_lock.release() 
            break
        if msg == "PING":
            c.send("Server Pinged".encode('ascii'))

        else:

            loc = {}
            exec(code, globals(), loc)
            res = loc['result']
            result = "Job Done. Output : "+str(res)
            c.send(result.encode('ascii'))
   
    c.close() 
  
  
def Main():
    host = ''
    port = 1235
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("Socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        id = start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 