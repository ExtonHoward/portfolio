
numbers = ["Items:",]

def adding_report():
    sum = 0
    while sum <= 0:
        q1 = input("Choose report type (A or T): ")
        if q1.lower() == "a":
            while q1.lower() == "a":
                a1 = input ('Enter an integer or press "Q" to quit: ')
                if a1.isdigit():
                    x = int(a1)
                    sum += x
                    numbers.append(str(x))
                elif a1.lower().startswith("q"):
                    print(*numbers, sep ='\n')
                    print("\nTotal of your integers is " + str(sum))
                    break
                else:
                    print(a1 + " is an invalid input")
                    pass
        elif q1.lower() == "t":
            while q1.lower() == "t":
                t1 = input ('Enter an integer or press "Q" to quit: ')
                if t1.isdigit():
                    x = int(t1)
                    sum += x
                    numbers.append(str(x))
                elif t1.lower().startswith("q"):
                    print("\nTotal of your integers is " + str(sum))
                    break
                else:
                    print(t1 + " is an invalid input")
                    pass
        else:
            print(q1 + " is an invalid input")
            pass

adding_report()
