def server_cost(d1, m1, y1, d2, m2, y2):
    if d1==d2 and m1==m2 and y1==y2:
        return 20
    elif d1-d2!=0 and m1-m2<=30 and y1==y2:
        return 30*(d2-d1)
    elif m2-m1>=1 and y2-y1==0:
        return 1000*(m2-m1)
    elif y2-y1!=0:
        return 20000

if __name__ == '__main__':
    d1M1Y1 = input('enter').split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])

    d2M2Y2 = input('enter 2').split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')


