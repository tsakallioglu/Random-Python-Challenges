# Assumed  1 <= x,y,z <= 99 and x,y,z = integer
def answer(x,y,z):
    a =str(x).zfill(2)
    b =str(y).zfill(2)
    c =str(z).zfill(2)
    
    if x<12 and (x==y==z):
        return a+"/"+a+"/"+a
        return
    elif (x>12 and y>12 and z<=12) or (x>12 and z>12 and y<=12) or (y>12 and z>12 and x<=12):
        if z<=12:
            if z != 2:            
                rem=z/2
                if rem==1:
                    if (x<=31 and x==y):
                        return c+"/"+a+"/"+b
                    elif (x<=31 and y>31):
                        return c+"/"+a+"/"+b
                    elif (x>31 and y<=31):
                        return c+"/"+b+"/"+a
                else:
                    if (x<=30 and x==y):
                        return c+"/"+a+"/"+b
                    elif (x<=30 and y>30):
                        return c+"/"+a+"/"+b
                    elif (x>30 and y<=30):
                        return c+"/"+b+"/"+a
            else:
                if (x<=28 and x==y):
                    return c+"/"+a+"/"+b
                if (x<=28 and y>28):
                    return c+"/"+a+"/"+b
                elif (x>28 and y<=28):
                    return c+"/"+b+"/"+a
        if y<=12:
            if y != 2:            
                rem=y/2
                if rem==1:
                    if (x<=31 and x==z):
                        return b+"/"+a+"/"+c
                    if (x<=31 and z>31):
                        return b+"/"+a+"/"+c
                    elif (x>31 and z<=31):
                        return b+"/"+c+"/"+a
                else:
                    if (x<=30 and x==z):
                        return b+"/"+a+"/"+c
                    if (x<=30 and z>30):
                        return b+"/"+a+"/"+c
                    elif (x>30 and z<=30):
                        return b+"/"+c+"/"+a
            else:
                if (x<=28 and x==z):
                    return b+"/"+a+"/"+c
                if (x<=28 and z>28):
                    return b+"/"+a+"/"+c
                elif (x>28 and z<=28):
                    return b+"/"+c+"/"+a
        if x<=12:
            if x != 2:            
                rem=x/2
                if rem==1:
                    if (y<=31 and y==z):
                        return a+"/"+b+"/"+c
                    if (y<=31 and z>31):
                        return a+"/"+b+"/"+c
                    elif (y>31 and z<=31):
                        return a+"/"+c+"/"+b
                else:
                    if (y<=30 and y==z):
                        return a+"/"+b+"/"+c
                    if (y<=30 and z>30):
                        return a+"/"+b+"/"+c
                    elif (y>30 and z<=30):
                        return a+"/"+c+"/"+b
            else:
                if (y<=28 and y==z):
                    return a+"/"+b+"/"+c
                if (y<=28 and z>28):
                    return a+"/"+b+"/"+c
                elif (y>28 and z<=28):
                    return a+"/"+c+"/"+b
        
    return "Ambiguous"