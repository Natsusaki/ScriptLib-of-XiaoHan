################################################################################
#            This script is used for fucking guess number                      #
#                               XiaoHan                                        #
#                      xiaohan16@mails.ucas.ac.cn                              #
#                              2019.3.3                                        #
################################################################################

def GetNum(number,i):
    number=str(number)
    lens=len(number)
    n = int(number[lens-(i):lens-(i-1)])
    return n

def Main():
    abond = [ ]
    guess = [ ]
    for i in range(0,10):
        for j in range(0,10):
            if i == j:
                for k in range(0,10):
                    for l in range(0,10):
                        abond.append(str(i*1000 + j*100 + k*10 + l).zfill(4))
            else:
                for k in range(0,10):
                    if k == i or k == j:
                        for l in range(0,10):
                            abond.append(str(i*1000 + j*100 + k*10 + l).zfill(4))
                    else:
                        for l in range(0,10):
                            if l==i or l==j or l==k:
                                abond.append(str(i*1000 + j*100 + k*10 + l).zfill(4))
                            else:
                                guess.append(str(i*1000 + j*100 + k*10 + l).zfill(4))


    print(guess[0])
    active = True

    N = 1

    while active:
        abond = []
        A = int(input("number of A："))
        B = int(input("number of B："))
        B = A + B
        if B == 0:
            a = GetNum(guess[0],4)
            b = GetNum(guess[0],3)
            c = GetNum(guess[0],2)
            d = GetNum(guess[0],1)
            for number in guess:
                a2 = GetNum(number,4)
                b2 = GetNum(number,3)
                c2 = GetNum(number,2)
                d2 = GetNum(number,1)
                total = 0
                if a2 == a or a2 == b or a2 == c or a2 == d:
                    total = total + 1
                if b2 == a or b2 == b or b2 == c or b2 == d:
                    total = total + 1
                if c2 == a or c2 == b or c2 == c or c2 == d:
                    total = total + 1
                if d2 == a or d2 == b or d2 == c or d2 == d:
                    total = total + 1
                if total != 0:
                    abond.append(number)

        elif B == 1:
            a = GetNum(guess[0],4)
            b = GetNum(guess[0],3)
            c = GetNum(guess[0],2)
            d = GetNum(guess[0],1)
            for number in guess:
                a2 = GetNum(number,4)
                b2 = GetNum(number,3)
                c2 = GetNum(number,2)
                d2 = GetNum(number,1)
                total = 0
                if a2 == a or a2 == b or a2 == c or a2 == d:
                    total = total + 1
                if b2 == a or b2 == b or b2 == c or b2 == d:
                    total = total + 1
                if c2 == a or c2 == b or c2 == c or c2 == d:
                    total = total + 1
                if d2 == a or d2 == b or d2 == c or d2 == d:
                    total = total + 1
                if total != 1:
                    abond.append(number)
            if A == 1:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 1:
                        abond.append(number)
            elif A == 0:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 0:
                        abond.append(number)
    ########################################################
        elif B == 2:
            a = GetNum(guess[0],4)
            b = GetNum(guess[0],3)
            c = GetNum(guess[0],2)
            d = GetNum(guess[0],1)
            for number in guess:
                a2 = GetNum(number,4)
                b2 = GetNum(number,3)
                c2 = GetNum(number,2)
                d2 = GetNum(number,1)
                total = 0
                if a2 == a or a2 == b or a2 == c or a2 == d:
                    total = total + 1
                if b2 == a or b2 == b or b2 == c or b2 == d:
                    total = total + 1
                if c2 == a or c2 == b or c2 == c or c2 == d:
                    total = total + 1
                if d2 == a or d2 == b or d2 == c or d2 == d:
                    total = total + 1
                if total != 2:
                    abond.append(number)
            if A == 2:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 2:
                        abond.append(number)
            elif A == 1:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if int(a2) == int(a):
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 1:
                        abond.append(number)
            elif A == 0:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 0:
                        abond.append(number)
    ###############################################################
        elif B == 3:
            a = GetNum(guess[0],4)
            b = GetNum(guess[0],3)
            c = GetNum(guess[0],2)
            d = GetNum(guess[0],1)
            for number in guess:
                a2 = GetNum(number,4)
                b2 = GetNum(number,3)
                c2 = GetNum(number,2)
                d2 = GetNum(number,1)
                total = 0
                if a2 == a or a2 == b or a2 == c or a2 == d:
                    total = total + 1
                if b2 == a or b2 == b or b2 == c or b2 == d:
                    total = total + 1
                if c2 == a or c2 == b or c2 == c or c2 == d:
                    total = total + 1
                if d2 == a or d2 == b or d2 == c or d2 == d:
                    total = total + 1
                if total != 3:
                    abond.append(number)
            if A == 3:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 3:
                        abond.append(number)        
            elif A == 2:
                for number in guess:
    ####################################
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 2:
                        abond.append(number)
            elif A == 1:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 1:
                        abond.append(number)
            elif A == 0:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 0:
                        abond.append(number)
    ################################################
        elif B == 4:
            a = GetNum(guess[0],4)
            b = GetNum(guess[0],3)
            c = GetNum(guess[0],2)
            d = GetNum(guess[0],1)
            for number in guess:
                a2 = GetNum(number,4)
                b2 = GetNum(number,3)
                c2 = GetNum(number,2)
                d2 = GetNum(number,1)
                total = 0
                if a2 == a or a2 == b or a2 == c or a2 == d:
                    total = total + 1
                if b2 == a or b2 == b or b2 == c or b2 == d:
                    total = total + 1
                if c2 == a or c2 == b or c2 == c or c2 == d:
                    total = total + 1
                if d2 == a or d2 == b or d2 == c or d2 == d:
                    total = total + 1
                if total != 4:
                    abond.append(number)
            if A == 4:
                print('The right number is',guess[0])
                print("The number of guess is",N)
            elif A == 3:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 3:
                        abond.append(number)        
            elif A == 2:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 2:
                        abond.append(number)
            elif A == 1:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 1:
                        abond.append(number)
            elif A == 0:
                for number in guess:
                    a2 = GetNum(number,4)
                    b2 = GetNum(number,3)
                    c2 = GetNum(number,2)
                    d2 = GetNum(number,1)
                    total = 0
                    if a2 == a:
                        total = total + 1
                    if b2 == b:
                        total = total + 1
                    if c2 == c:
                        total = total + 1
                    if d2 == d:
                        total = total + 1
                    if total != 0:
                        abond.append(number)
    #########################################
        elif B >= 5 or A >= 5 :
            return

        for number in abond:
            if number in guess:
                guess.remove(number)
        print(guess[0])
        print("The number of candidate is",len(guess))
        if len(guess) <= 20:
            print(guess)
        N = N + 1

    
while True:
    Main()
