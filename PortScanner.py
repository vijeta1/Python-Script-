import socket

def retResult(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((ip,port))
		result=s.recv(1024)
		return result
	except:
		return

def CheckVulns(result):
	if 'FreeFloat Ftp Server(Version 1.00)' in result:
		print '[+] FreeFloat FTP Server is vulnerable.'
	elif '3Com 3CDaemon FTP Server Version 2.0' in result:
		print '[+] Ability FTP Server is vulnerable.'
	elif 'Sami FTP Version 2.0.2' in result:
		print '[+] Sami FTP Server is vulnerable.'
	else:
		print '[-] FTP Server is not vulnerable.'
	return

def main():
	portlist=[21,22,25,80,110,443]
	for i in range(1,255):
		ip='192.168.95'+str(i)
		for port in portlist:
			result=retResult(ip,port)
			if result:
				print '[+]'+ip+':'+result
				CheckVulns(result)

