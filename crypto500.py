import socket
import gmpy2
from Crypto.Util.number import bytes_to_long, long_to_bytes
import time

for i in range(10):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('crypto.chal.csaw.io', 1003))
    m1=2**20 + 100 
    m2=2**20 - 100
    m3=2**20 + 101

    m1d = m1**2
    m2d = m2**2
    m3d = m3**2

    s.send('38,1'+'\n')
    s.recv(1024)
    enc_flag = s.recv(1024)
    enc_flag = int(enc_flag.split('\n')[0][16:], 16)

    s.send('1' + '\n')
    s.recv(1024)
    s.send(long_to_bytes(m1) + '\n')
    c1 = int(s.recv(1024)[:-1], 16)
    s.recv(1024)

    s.send('1' + '\n')
    s.recv(1024)
    s.send(long_to_bytes(m1d) + '\n')
    c1d = int(s.recv(1024)[:-1], 16)
    s.recv(1024)

    s.send('1' + '\n')
    s.recv(1024)
    s.send(long_to_bytes(m2) + '\n')
    c2 = int(s.recv(1024)[:-1], 16)
    s.recv(1024)

    s.send('1' + '\n')
    s.recv(1024)
    s.send(long_to_bytes(m2d) + '\n')
    c2d = int(s.recv(1024)[:-1], 16)
    s.recv(1024)

    s.send('1' + '\n')
    s.recv(1024)
    s.send(long_to_bytes(m3) + '\n')
    c3 = int(s.recv(1024)[:-1], 16)
    s.recv(1024)

    s.send('1' + '\n')
    s.recv(1024)
    s.send(long_to_bytes(m3d) + '\n')
    c3d = int(s.recv(1024)[:-1], 16)
    s.recv(1024)

    N = gmpy2.gcd(c3**2-c3d, gmpy2.gcd(c2**2-c2d,c1**2-c1d))

    UB = N
    LB = 0

    s.send('1' + '\n')
    s.recv(1024)
    s.send(chr(2) + '\n')
    c_2 = int(s.recv(1024)[:-1], 16)
    s.recv(1024)
    start = (c_2 * enc_flag) % N

    for _unused in range(83):
        s.send('2' + '\n')
        s.recv(1024)
        s.send(long_to_bytes(start) + '\n')
        bytee = int(s.recv(1024)[:-1], 16)
        s.recv(1024)
        
        if (bytee % 2 == 0):
            UB = (UB + LB)/2;
        else:
            LB = (UB + LB)/2;
        start = (start * c_2) % N;

    #print 'Upper:', hex(UB)[2:]
    #print 'Lower:', hex(LB)[2:]
    print 'Byte:', hex(UB)[2:].zfill(256)[10:12]
    s.close()
