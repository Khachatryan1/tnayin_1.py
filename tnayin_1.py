lst = [10,'alo',[52,41,False,'ola'],'hello',5,6,2]

for i in lst:
    if type(i) == list:
        for j in i:
            print(j)
