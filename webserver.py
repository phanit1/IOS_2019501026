import socket
import os, filetype
from pathlib import Path

enable_directory_browsing = True
actual_path = "F:/"
docroot = "F:/"

def init(HOST, PORT):
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listen_socket.bind((HOST, PORT))
	print("server started")
	return listen_socket

def start_server(listen_socket):
	listen_socket.listen(1)
	execute_scripts("")
	serve_clients(listen_socket)

def serve_clients(listen_socket):
	while True:
		client_connection, client_address = listen_socket.accept()
		request_data = client_connection.recv(1024)
		client_connection.sendall(getcontent(request_data))


def geturi(request_data):
	temp = request_data.split(" ")[1]
	if(temp == "/") or temp == "/favicon.ico":
		return temp
	return temp



def get_files(path):
	files = []
	for file in os.listdir(path):
		files.append("<a href = \""+os.path.join(path, file) + "\"  > " + os.path.join(path, file) +"</a> <br>")
	return ''.join(files)
	

def get_content_type(path):
	kind = filetype.guess(path)
	if kind is None:
		return "text"
	else:
		return kind.mime

def is_file_exist(uri):
	try:
		os.path.isdir(uri)
		return True
	except:
		return False

def getcontent(data):
	request_data = data.decode("UTF-8")
	uri = geturi(request_data)
	flag = is_file_exist(uri)
	http_response = b""
	if request_data.split(" ")[0] != "GET" or uri == "":
		http_response = b"""\
HTTP/1.1 400 BAD REQUEST
Content-Type: html;

				
<b><center><font color="red">BAD REQUEST</font></center></b>"""
	if not flag:
		http_response = b"""\
HTTP/1.1 400 BAD REQUEST
Content-Type: html;

				
<b><center><font color="red">File Not Found</font></center></b>"""

	if enable_directory_browsing:
		if (uri) == "/" or (uri) == docroot:
			get_files(docroot)
			http_response = b"""\
HTTP/1.1 200 OK
Content-Type: html;

				
""" + bytes(get_files(docroot),"UTF-8")
		elif uri == '/favicon.ico':
			pass
		elif flag and os.path.isfile(uri):
			content_type = get_content_type(uri)
			print(content_type, "content_type")
			f = open(uri,'rb')
			string = f.read()
			http_response = b"""\
HTTP/1.1 200 OK
Content-Type: """ +bytes(content_type,"UTF-8")+b"""


				
""" + string

		else:
			http_response = b"""\
HTTP/1.1 200 OK
Content-Type: html;

				
""" + bytes(get_files(uri),"UTF-8")


	else:
		http_response = b"""\
HTTP/1.1 400 BAD REQUEST
Content-Type: html;

				
<b><center><font color="red">BAD REQUEST</font></center></b>"""

	return http_response



def execute_scripts(filename):
	# p = Pipe()
	n = os.fork()
	exec(Path("F:/Socket Programming/Web server/scripts/ExecutionFile.py").read_text())
	# print(out)

start_server(init('',5667))


