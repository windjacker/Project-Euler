import time
from datetime import datetime


def read_data(a):
    data = open('Primzahlen.txt', 'r')

    for i in data:
        a.append(int(i[:-1]))
    
    data.close()

def calculation(a):
    inp = input("Geplante Berechnungszeit in min: ");
    dt = float(inp)
    data = open('Primzahlen.txt', 'a')

    t = time.time();
    i = a[-1]+2
    print("Start: {:%H:%M:%S} - {}".format(datetime.now(), i) )
    while ( time.time()-t <= dt*60):
        isPrime = True
        for p in a:
            if i%p==0:
                isPrime = False
                break
            if p**2>i:
                break
        if isPrime:
            a.append(i)
            data.write( str(i) + '\n' )
        i += 2

    print("Stop : {:%H:%M:%S} - {}".format(datetime.now(), i) )


primarr = []
read_data(primarr)

if __name__ == '__main__':
    calculation(primarr)
