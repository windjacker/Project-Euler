import time
from datetime import datetime

inp = input("Geplante Berechnungszeit in min: ");
dt = int(inp)


data = file('Primzahlen.txt', 'r+w')

primarr = []
for i in data:
    primarr.append(int(i[:-1]))


t = time.time();
i = primarr[-1]+2
print("Start: {:%H:%M} - {}".format(datetime.now(), i) )
while ( time.time()-t <= dt*60):
    for p in primarr:
        if i%p==0:
            i += 2
            break
    primarr.append(i)
    data.write( str(i) + '\n' )
    i += 2

print("Stop : {:%H:%M} - {}".format(datetime.now(), i) )

