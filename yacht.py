import random
from typing import Counter
import copy as c
import pandas as pd

class roll_dice : 
    # 주사위 굴리는 파트
    def Random_dice() :
        list = []  
        for i in range(5) :
            dice = random.randrange(1,6)
            list.append(dice)    
        return list

    # 주사위 교체 파트
    def Change_dice(query, dice_result) :
        while True :
            if query == 'y' or query == 'Y' :
                choice_list = []
                while True :
                    input_select = input("다시 굴릴 주사위 번호를 하나씩 입력 후 Enter(종료 F, 재입력 A) : ")
                    if input_select in ['1', '2', '3', '4', '5'] :
                        choice_list.append(input_select)
                        print("입력한 번호 : ", choice_list)
                        continue
                    elif input_select == 'a' or input_select == 'A':
                        print("번호 초기화!!")
                        choice_list = []
                    elif input_select == 'f' or input_select == 'F' :
                        print("주사위 선택 종료")
                        break
                    else :
                        print("유효하지 않은 값 입니다 !!")
                        continue
                
                # i가 choice_list를 쭈욱 훑음
                # 0번 인덱스부터 다시 굴려야하니까 -1
                for i in choice_list :
                    dice_result[int(i)-1] = random.randrange(1,6)
                return dice_result

            elif query == 'n' or query == 'N' :
                return dice_result

            else :
                print("유효하지 않은 값 입니다 !!")
                continue

# class result_dice :
#     #주사위 결과값 파트
#     def Show_result(dice_result) :
#         dice_list = {}
#         dice_list['1번 주사위'] = dice_result[0]
#         dice_list['2번 주사위'] = dice_result[1]
#         dice_list['3번 주사위'] = dice_result[2]
#         dice_list['4번 주사위'] = dice_result[3]
#         dice_list['5번 주사위'] = dice_result[4]

#         return dice_list

class setup_score :
    def setup_scores(dice) :
        #dice_res
        res = []
        for i in range(len(dice)) :
            dice[i] = c.deepcopy(int(dice[i]))
        
        res.extend(setup_score.upper(dice))
        res.extend(setup_score.lower3(dice))
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
        
    

    



class check_able :

    
        

    def check_able(dice) :
        #dice = [2,3,4,4,5]
        return  [1,1,1,1,1,1,1,check_able.check_4_of_a_kind(dice),check_able.check_full_house(dice),check_able.check_small_straight(dice),check_able.check_large_straight(dice),check_able.check_yacht(dice)]
    
    

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

def score_part(dice_res) :
    global points 
    insert_able_list =  check_able.check_able(dice_res)
    #print(insert_able_list)
    #print("score_part insert_able_list :",insert_able_list) 
    prints = [  "========================\n"
                "Aces\t\t:{}점",
                "Deuces\t\t:{}점",
                "Threes\t\t:{}점",
                "Fours\t\t:{}점",
                "Fives\t\t:{}점",
                "Sixes\t\t:{}점",
                "Choice\t\t:{}점",
                "4_of_a_Kind\t:{}점",
                "Full_House\t:{}점",
                "Small_Straight\t:{}점",
                "Large_Straight\t:{}점",
                "Yacht\t\t:{}점"
                "\n========================"]

    scores = setup_score.setup_scores(dice_res)
    #print("score_part scores :",scores)
    
    '''

    for i in range(len(insert_able_list)) :
        if insert_able_list[i] == 1 :
            print(prints[i].format(scores[i]))
            
    '''
    for i in range(len(insert_able_list)) :
            print(prints[i].format(scores[i]))


    pass

class Score_board :
    
    def score(player_list) :
        df = pd.DataFrame(columns=player_list, index=['Aces', 'Deuces', 'Threes', 'Fours', 'Fives', 'Sixes', 'Choice', '4_of_a_Kind'
                                                      'Full_House', 'Small_Straight', 'Large_Straight', 'Yacht', 'Total_Score'])
        df = df.fillna(0)
        




# main
points = [0,0,0,0,0,0,0,0,0,0,0,0]
print("프로그램을 시작합니다.")

print("1. 게임시작")
print("2. 게임설명")
input_start = input("입력 : ")
count = 0

if input_start == "1" :
    #게임 시작 코드 추가 필요
    while(True) : 
        player_list = []
        player1_name = input("1번 플레이어의 이름 : ")
        player_list.append(player1_name)
        player2_name = input("2번 플레이어의 이름 : ")
        player_list.append(player2_name)
        if player2_name != '' and player1_name != '':
            break
        else :
            print("플레이어의 이름을 입력해야만 합니다! (2인용)")
    
    print('\n' + '☆' * 16 + '\n' + "\t게임을  시작하지\t" + '\n' +'★' * 16 + '\n')

    for turn in range (1,13) :
        for player_turn in player_list :
            print("\n12턴 중 " + str(turn) + "번째\n")
            print(str(player_turn)+"의 차례!\n")

            dice_result = roll_dice.Random_dice()
            print("주사위 값 : " + str(dice_result))
            score_part(dice_result)
            count = 1
            
            while(count < 3) :
                query = input("값을 바꾸시겠어요? (Y/N)")
                if query == 'y' or query == 'Y' :
                    roll_dice.Change_dice(query, dice_result)
                    print("주사위 값 : " + str(dice_result))
                    score_part(dice_result)
                    count+=1
                elif query == 'n' or query == 'N' :
                    break
                else :
                    print("유효하지 않은 값입니다 !! ")

            print("=================================================================\n"
                "1 = Aces\t 2 = Deuces\t 3 = Threes\t 4 = Fours\n"
                "5 = Fives\t 6 = Sixes\t 7 = Choice\t 8 = 4_of_a_Kind\n"
                "9 = Full_House\t 10 = Small_Straight\t 11 = Large_Straight\n"
                "12 = Yacht"
                "\n=================================================================")
            
            select_point = input("몇 번 값으로 선택하시겠어요 ? (1 ~ 12) : ")

elif input_start == "2" :
    #게임 설명 코드 추가 필요
    pass









