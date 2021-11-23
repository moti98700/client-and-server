import socket
import os


def get_upld(read_file,file_name):



    filepath = os.path.join('Desktop/moti/server15', file_name)
    os.makedirs('Desktop/moti/server15')
    f = open(filepath, "w")
    f.write(read_file)


    







server_socket = socket.socket()
print ("Socket successfully created")


port = 12345


server_socket.bind(('', port))
print ("socket binded to %s" %(port))


server_socket.listen(5)
print ("socket is listening")



while True:
 

  c, addr = server_socket.accept()    
  print ('Got connection from', addr )
 
  
  
  data_user= c.recv(1024).decode()
  sorting_data = data_user.split("$")
  
  read_file= sorting_data[0]
  file_name  = sorting_data[1]
  tag = sorting_data[2]
  
  if tag == 'up':
    #print(file_name)
    #print(read_file)
    get_upld(read_file,file_name)
  
  if tag == 'do':
      c.send(file_name.encode())
  
  if tag == 'list1':
      arr = os.listdir('Desktop/moti/server14')
      a = str(arr)
      c.send(a.encode())




      



  

