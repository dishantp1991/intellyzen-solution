product = []
while(1):
    print(">")
    inp=str(input())
    spl=inp.split(" ")
    #print(spl)
    if spl[0] == "list":
        for p in product:
            print(p)
    elif spl[0] == "add":
        product.append(spl[1])
    elif spl[0] == "find":
        count = 0
        for p in product:
            if spl[1] in p:
                count = count + 1
        print(count)
        else:
     print("wrong input provided.Please provide following option 1.add 2.list 3.Find ")
