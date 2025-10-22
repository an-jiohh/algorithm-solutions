# 언어,직군,경력,소울푸드는 dict를 이용해서 최적화가 가능
# 실패코드
# from bisect import bisect_left

# def solution(info, query):
#     answer = []
#     d_lan = ["-","cpp","java","python"]
#     d_position = ["-","backend", "frontend"]
#     d_year = ["-","junior", "senior"]
#     d_food = ["-","chicken", "pizza"]
#     dict = {}
#     for i in d_lan :
#         dict[i] = {}
#         for j in d_position :
#             dict[i][j] = {}
#             for k in d_year :
#                 dict[i][j][k] = {}
#                 for l in d_food :
#                     dict[i][j][k][l] = []
#     for i in info :
#         lan, position, year, food, score = i.split()
#         score = int(score)
#         dict[lan][position][year][food].append(score)
#         dict[lan][position][year]["-"].append(score)
#         dict[lan][position]["-"][food].append(score)
#         dict[lan]["-"][year][food].append(score)
#         dict["-"][position][year][food].append(score)
#         dict["-"]["-"][year][food].append(score)
#         dict[lan]["-"]["-"][food].append(score)
#         dict[lan][position]["-"]["-"].append(score)
#         dict["-"][position]["-"][food].append(score)
#         dict[lan]["-"][year]["-"].append(score)
#         dict["-"][position][year]["-"].append(score)
#         dict["-"]["-"]["-"][food].append(score)
#         dict[lan]["-"]["-"]["-"].append(score)
#         dict["-"][position]["-"]["-"].append(score)
#         dict["-"]["-"][year]["-"].append(score)
#         dict["-"]["-"]["-"]["-"].append(score)
        
#         dict[lan][position][year][food].sort()
#         dict[lan][position][year]["-"].sort()
#         dict[lan][position]["-"][food].sort()
#         dict[lan]["-"][year][food].sort()
#         dict["-"][position][year][food].sort()
#         dict["-"]["-"][year][food].sort()
#         dict[lan]["-"]["-"][food].sort()
#         dict[lan][position]["-"]["-"].sort()
#         dict["-"][position]["-"][food].sort()
#         dict[lan]["-"][year]["-"].sort()
#         dict["-"][position][year]["-"].sort()
#         dict["-"]["-"]["-"][food].sort()
#         dict[lan]["-"]["-"]["-"].sort()
#         dict["-"][position]["-"]["-"].sort()
#         dict["-"]["-"][year]["-"].sort()
#         dict["-"]["-"]["-"]["-"].sort()
#     for i in query :
#         lan, position, year, food = i.split(" and ")
#         food,score = food.split()
#         score = int(score)
#         # count = 0
#         # for j in dict[lan][position][year][food] :
#         #     if j >= score : count += 1
#         index = bisect_left(dict[lan][position][year][food], score)
#         answer.append(len(dict[lan][position][year][food]) - index)
#     return answer

from bisect import bisect_left

def solution(info, query):
    answer = []
    d_lan = ["-","cpp","java","python"]
    d_position = ["-","backend", "frontend"]
    d_year = ["-","junior", "senior"]
    d_food = ["-","chicken", "pizza"]
    dict = {}
    for i in d_lan :
        for j in d_position :
            for k in d_year :
                for l in d_food :
                    dict[i+j+k+l] = []

    for i in info :
        lan, position, year, food, score = i.split()
        score = int(score)
        for j in [lan, "-"]:
            for k in [position, "-"]:
                for l in [year, "-"]:
                    for m in [food, "-"]:          
                        dict[j+k+l+m].append(score)
    for i in dict:
        dict[i].sort()
    for i in query :
        lan, position, year, food = i.split(" and ")
        food,score = food.split()
        score = int(score)
        index = bisect_left(dict[lan+position+year+food], score)
        answer.append(len(dict[lan+position+year+food]) - index)
    return answer