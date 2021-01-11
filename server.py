import socket
import sys
import colorama
from colorama import Fore, Style

def server(log_buffer=sys.stderr):
	address = ('0.0.0.0', 1738)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# allow rapid re-use of the socket
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(address)
	sock.listen(10)

	try:
		while True:
			info = (Fore.CYAN + "[*] ")
			recc = (Fore.YELLOW + "[*] ")
			good = (Fore.GREEN + "[+] ")
			error = (Fore.RED + "[-] ")
			print(info+"Starting echo server...")
			print(info+"Waiting...\n")
						
			conn, addr = sock.accept()
			print(good+"Connection recieved!")
			print(good+"Address and port:")
			print(recc+"[---> " + str(addr))
			print(good+"Full socket info: ")
			print(recc+"[---> " + str(conn))
			try:
				while True:			
					data = conn.recv(16)
					received = str(data)
					print("\n")
					print(good+"Data received!")
					print(info+"Data: " + received)
					print(good+"Echoing back...\n")
						
					if data:
						conn.sendall(data)
					else:
						break
			finally:
				print(error+"Closing connection...")
				print(Style.RESET_ALL)
				conn.close()

	except KeyboardInterrupt:
		sock.close()
		return


if __name__ == '__main__':
	server()
	sys.exit(0)
