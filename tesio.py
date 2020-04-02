tc = int(input())
for n in range(tc):
    detail = input()
    detail = detail.split()
    length = int(detail[0])
    queries = int(detail[1])
    string = input()
    string = string[:length]
    for n in range(queries):
        check = input()
        check = check.split()
        if int(check[0]) == 1:
            string = string[-int(check[1]):] + string[0:-int(check[1])]
        else:
            print(string[int(check[1])])