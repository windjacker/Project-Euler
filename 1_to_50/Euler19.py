solution = 0


def year(yn, day):
    year = [day]
    for i in range(1, 12):
        if (i==4 or i==6 or i==9 or i==11):
            year.append( (year[i-1]+30)%7 )
        elif i==2:
            if (yn%4==0 and yn!=1900):
                year.append( (year[i-1]+29)%7 )
            else:
                year.append( (year[i-1]+28)%7 )
        else:
            year.append( (year[i-1]+31)%7 )
    
    print yn, year
    
    sundays = 0
    for m in year:
        if m==6:
            sundays += 1
    
    return sundays, (year[11]+31)%7


day = year(1900, 0)[1]
for i in range(1901, 2001):
    y = year(i, day)
    day = y[1]
    solution += y[0]



print(solution)
