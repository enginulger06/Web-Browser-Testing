import socket, time
from urllib.request import urlopen
from urllib.parse import urlparse

URL='http://www.rarlab.com/rar/winrar-x64-420.exe'

print (URL, 'timing:')

urlinfo = urlparse(URL)

start = time.time()
ip = socket.gethostbyname( urlinfo.netloc )
dns_tm = time.time()-start
print ('DNS:\t\t{:.3f} seconds'.format( dns_tm ))

start = time.time()
_data = urlopen(URL).read()
load_tm = time.time()-start
print ('load:\t\t{:.3f} seconds'.format( load_tm ))
print ('w/o DNS:\t{:.3f} seconds'.format( load_tm-dns_tm ))

print("---------------------")

'''
nf =urlopen(URL)
start = time.time()
page = nf.read()
end = time.time()
nf.close()
print(round(end-start,3))# end - start sayfa yükleme süresini size verir
'''



