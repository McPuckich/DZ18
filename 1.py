from random import randint

def minusi(chis):
    otr = 0
    for i in chis:
        if i < 0:
            otr +=1
    return otr


list = [randint(-10, 10) for i in range(randint(5, 10))]
print(list)
print(minusi(list))
