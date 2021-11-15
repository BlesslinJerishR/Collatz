def collatz(num):
    coll = list()
    while num != 1:
        coll.append(num)

        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    coll.append(1)
    l = len(coll)

    print(f"The Length of my collatz is {l}")
    print("The sequence is :", end=" ")
    for i in range(0, l):
        print(coll[i], end=" ")


# player one driver codes
num = int(input('Enter a number for initiating Collatz sequence : '))
collatz(num)
