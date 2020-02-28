import socket
import os,mimetypes
root = "C:\\Users\\personal\\Desktop\\MSIT\\IT\\IOS_2019501026\\m3"
is_directory = True

def get_files(path):
    files = []
    for file in os.listdir(root + path):
        if(path == root):
            files.append("<a href = \""+file + "\" > " + file + "</a> <br>")
        else:
            files.append("<a href = \""+os.path.join(path,file) + "\" >" + file + "</a> <br>")
    return ''.join(files)    
def get_content_type(path):
    kind, a = mimetypes.guess_type(root + path)
    if kind is None:
        return "text"
    else:
        return kind      

def start_server(IP, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as s:
        s.bind((IP, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                # TODO read the request and extract the URI
                input = conn.recv(1024).decode("UTF-8")
                
                uri = input.split(" ")[1]
                flag = os.path.exists(root+uri)
                if input.split(" ")[0] != 'GET' or uri ==" ":
                    response = b'''\
HTTP/1.1 404 File Not Found
Content - Type:html

<h1>bad request </h1>'''
                elif flag == False:
                    response = b"""\
HTTP/1.1 404 File Not Found
Content - Type:html

<h1>File Not Found<h1>""" 
                elif is_directory:
                    if uri == "/favicon.ico":
                        pass
                    elif flag and os.path.isfile(root + uri):
                        content_type = get_content_type(uri)
                        f = open(root + uri, 'rb')
                        string = f.read()
                        response = b"""\
HTTP/1.1 200 OK
Content - Type: """ +bytes(content_type,"UTF-8")+b"""

""" + string
                    else:
                        response = b"""\
HTTP/1.1 200 OK
Content - Type:html

""" + bytes(get_files(uri), "UTF-8")

                else:
                    response = b"""\
HTTP/1.1 400 BAD REQUEST
Content-Type: html;

<h1>BAD REQUEST</h1>"""                              

                conn.sendall(response) 
                conn.close()

def main():
# test harness checks for your web server on the localhost and on port 8888
# do not change the host and port
# you can change  the HTTPServer object if you are not following OOP
    start_server('127.0.0.1', 8888)

if __name__ == "__main__":
    main()




