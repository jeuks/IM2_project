def charcount():
    fchar = input("Enter a string: ")

    char = [c.strip() for c in fchar.split(",")]

    for cc in char:
        ccount = {}
        for cch in cc:
            if cch in ccount:
                ccount[cch] += 1
            else:
                ccount[cch] = 1

        output = ",".join([f"{x}={y}" for x, y in ccount.items()])
        print(output)

charcount()