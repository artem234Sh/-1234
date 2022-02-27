a = True
while a:
    ps = input("напиши пороль")
    if lenw(ps) < 8:
        print("короткий")
    else:
        print("ок")
        a = False
print("пороль отличьный")