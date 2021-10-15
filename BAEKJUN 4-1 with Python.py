while True:
    A, B = map(int, input("수를 입력하세요").split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)
