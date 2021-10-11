import copy as c

def setup_scores(dice) :
    #dice_res
    res = []
    for i in range(len(dice)) :
        dice[i] = c.deepcopy(int(dice[i]))
    
    res.extend(upper(dice))
    res.extend(lower3(dice))
    res.extend([15,30,50])

    #print("setup_score setup_scores res :",res)
    return res

def upper(dice) :
    res = []
    for j in range(1,7):
        temp = 0
        for i in range(len(dice)) :
            if dice[i] == j :
                temp += j
        res.append(temp)
    return res

def lower3(dice) :
    
    res = []
    for j in range(1,7):
        temp = 0
        for i in range(len(dice)) :
            temp += dice[i]
        res.append(temp)
    return res