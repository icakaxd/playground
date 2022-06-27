#!/usr/bin/env python3
import socket


def main():
	while True:
		url = input('Send URL: ')
		if url[0:4] != 'http':
			url = f'http://{url}'
		send(url)

def send(url = None):
	s = socket.socket()
	s.connect(('127.0.0.1', 60606))
	s.sendall(url.encode())
	s.close()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		# print(e)
		exit(e)
	except Exception as e:
		print(e)