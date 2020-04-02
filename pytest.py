


# def lstre(x,y,z,n):
#     lst = []
#     flst = []
#     for i in range(0,x+1):
#         for j in range(0,y+1):
#             for k in range(0,z+1):
#                 if i+j+k != n:
#                     lst.extend([i,j,k])
#                     flst.append(lst)
#                     i=i+1
#                     j=j+1
#                     k=k+1
#     return flst

# print(lstre(2,2,2,2))
           
# # x = int(input())
# # y = int(input())
# # z = int(input())  
# # n = int(input())  
# # lst = [[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n ]
# # print(lst)


# def cals(n):
#     lst = []
#     slst = []
#     for x in range(n):
#         name = input()
#         score = float(input())
#         lst.extend([name,score])
    
#     for y in range lst:
#         slst.append(lst[2])
#         slst.sort(reverse=True)
#         return slst[]

# print(cals(2))




def climbingLeaderboard(scores, alice):
    for i in range(len(scores)):
        count = 0
        for j in range(len(alice)):
            lst = []
            if alice[i] < scores[j] and alice[i] > scores[j+1]:
                lst.insert(count+1 , alice[i])
                count += 1 
            elif alice[i] == scores[j] :
                lst.insert(count+1 , alice[i])
                count = count+1 
            else:
                pass 
        return count 


print(climbingLeaderboard([100,100,50,40,40 ,20 ,10],[5,25,50,120]))