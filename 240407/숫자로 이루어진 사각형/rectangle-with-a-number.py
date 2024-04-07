def square(n):
    NUM = 1
    for i in range(n):
        arr = []
        for j in range(n):
            if (NUM > 9):
                NUM = 1
            arr.append(str(NUM))
            NUM+=1
        print(" ".join(arr))

n = int(input())
square(n)