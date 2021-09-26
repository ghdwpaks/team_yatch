import copy as c
def check_able(dice) :
    #dice = [2,3,4,4,5]
    return  [1,1,1,1,1,1,1,check_4_of_a_kind(dice),check_full_house(dice),check_small_straight(dice),check_large_straight(dice),check_yacht(dice)]
    
    

def check_4_of_a_kind(dice) :
    #print("check_4_of_a_kind dice :",dice)
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
        if stack >= 4 :
            return 1
    return 0
            
def check_full_house(dice) :
    suba = ""
    canpass = False
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
            if stack >= 3 :
                suba = str(dice[i])
                canpass = True
                #print("suba :",suba)
                #print("canpass :",canpass)
                break
        if canpass :
            #print("canpass 1 :",canpass)
            break
    
    if canpass :
        for i in range(len(dice)) :
            stack = 0
            base_num = dice[i]
            if str(base_num) == suba :
                continue
            #print("str(base_num) :",str(base_num))
            #print("suba :",suba)
            for j in range(len(dice)) :
                if dice[j] == base_num :

                    stack += 1
                if stack >= 2 :
                    return 1
    #print('last stack :',stack)
    return 0

def check_small_straight(dice) :
    dice = set(dice) 
    dice = list(dice)
    #print("check_small_straight dice :",dice)
    base_num = 0
    stack = 0
    
    base_num = c.deepcopy(dice[0])
    for i in range(len(dice)) :
        #print("base_num + i :",base_num + i)
        #print("dice[i] :",dice[i])
        if base_num + i == dice[i] :
            stack += 1

    #print("stack 1 :",stack)
    if stack >= 4 :
        return 1

    return 0

def check_large_straight(dice) :
    dice = c.deepcopy(dice)
    dice = set(dice) 
    dice = list(dice)
    #print("check_small_straight dice :",dice)
    base_num = 0
    stack = 0
    
    base_num = c.deepcopy(dice[0])
    for i in range(len(dice)) :
        #print("base_num + i :",base_num + i)
        #print("dice[i] :",dice[i])
        if base_num + i == dice[i] :
            stack += 1

    #print("stack 1 :",stack)
    if stack >= 5 :
        return 1

    return 0

def check_yacht(dice) :
    for i in range(len(dice)) :
        base_num = dice[i]
        stack = 0
        for j in range(len(dice)) :
            if dice[j] == base_num :
                stack += 1
        if stack >= 5 :
            return 1
    return 0