list = []
def capital_indexes(string):
    for i in enumerate(string):
        if i[1].isupper():
            list.append(i[0])
    return list
print(capital_indexes("TTTtTT"))

