# input_string = input()
# final = ""
# for i in input_string:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#         pass
#     else:
#         final = final + i
    
# print(final)


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


print(disemvowel('thisisnew'))