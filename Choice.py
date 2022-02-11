import random

choice1 = 8.6
choice2 = 3.6
choice3 = 6.9
choice4 = 9.7
choice5 = 2.3
choice6 = 2.5
choice7 = 0.3
choice8 = 0.1
choice9 = 0.0
choice10 = 0.0

ChoiceList = [choice1,choice2,choice3,choice4,choice5,choice6,choice7,choice8,choice9,choice10]

def CalculateChoice():
    List = []
    total = 0
    for i in range(0,len(ChoiceList),1):
        total += ChoiceList[i]
        List.append(ChoiceList[i])

    final = round(random.uniform(0,total),1)
    print(total)
    print(final)
    
def Maine():
    CalculateChoice()

Maine()
