isa = ["", "isa", "dalawa", "tatlo", "apat", "lima", "anim", "pito", "walo", "siyam", "sampu"]
 
put = ["","labing","dalawampu","tatlompu","apatnapu", "limampu","animnapu","pitompu","walompu","siyamnapu"]
 
libo = ["","libo","milyon", "bilyon"]
 
 
def num999(n):
    x = int(n % 10) # singles digit
    y = int(((n % 100) - x) / 10) # tens digit
    z = int(((n % 1000) - (y * 10) - x) / 100) # hundreds digit
    a = ""
    b = ""
    switch = {
        1:  "ng daan ",
        2:  "ng daan ",
        3:  "ng daan ",
        4:  "naraan ",
        5:  "ng daan ",
        6:  "naraan ",
        7:  "ng daan ",
        8:  "ng daan ",
        9:  "naraan "
    }
    
    if z != 0 and y == 0 and x == 0:
        z = isa[z] + + switch.get(z, "")
    elif z != 0:
        a = isa[z] + switch.get(z, "") + "at "
    if y <= 1:
        b = isa[n%100]
    elif y > 1:
        b = put[y] + "t " + isa[x]
    st = a + b
    return st
 
def num2word(num):
    if num == 0:
        return 'zero'
    i = 1
    n = int(num)
    word = ""
    k = 0
    switch = {
        1:  "ng ",
        2:  "ng ",
        3:  "ng ",
        4:  " na ",
        5:  "ng",
        6:  " na ",
        7:  "ng ",
        8:  "ng ",
        9:  " na "
    }
    while(n != 0):
        nw = ((float(n%1000)))
        n = int(n/1000)
        if i == 1:
            word = num999(int(nw)) + word
        else:
            word = num999(int(nw)) + switch.get(nw%10, "") + libo[k] + ", " + word
        k += 1
        i += 1
    return word

print(num2word(123456789))
