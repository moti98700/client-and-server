import socket            
import sys

#tcp_ip = input("enter ip_server: " )
#file_name = input("enter file_name to upld: ")
#file_name1 = input("enter file_name to download: ")

port=12345
my_socket = socket.socket()

def conn(tcp_ip):
    my_socket.connect((tcp_ip , port))

def upld(file_name):
    open_file = open((file_name), 'r')
    read_file = open_file.read()
    data=f"{read_file}${file_name}$up"
    my_socket.send(data.encode())


def download(file_name):
    data_send = f"Irrelevant${file_name}$do"
    my_socket.send(data_send.encode())
    file_name = my_socket .recv(1024).decode()
    print(file_name)

def files_server(list1):
    data_send = f"Irrelevant$Irrelevant$list1"
    my_socket.send(data_send.encode())
    list1 = my_socket .recv(1024).decode()
    print(list1)



conn('127.0.0.1')
upld('1234.txt')
#download('22.txt')
#files_server('list1')




    

