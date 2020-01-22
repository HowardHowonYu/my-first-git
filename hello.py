for i in range(1,50+1):
    if i % 3 == 0 and i % 5 ==0:
        print('FastCampus')
    elif i % 3 ==0:
        print('Fast')
    elif i % 5 == 0:
        print('Campus')
    else:
        print("{}".format(i))
