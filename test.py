import socket
from urllib import response

def tcp_server():
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 8008
    
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    sock_server.bind((SERVER_HOST, SERVER_PORT))
    
    sock_server.listen()
    
    print("Server ready")
    
    while True:
        sock_client, client_address = sock_server.accept()
        request = sock_client.recv(1024).decode()
        print(request)
        response = handle_request()
        sock_client.send(response.encode())
        sock_client.close()
    sock_server.close()
    

def handle_request():
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html\r\n\r\n"
    
    file = open("html_docs", 'r')
    message_body = file.read()
    file.close()
    
    response = response_line+content_type+message_body
    return response
    
if __name__ == "__main__":
    tcp_server()