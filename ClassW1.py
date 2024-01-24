#Q1
def getPigLatin(pigStr):
    pigList = pigStr.split() #convert a string variable pigStr to a list pigList
    pigLatin = []
    for x in pigList:
        if len(x) > 1:
            word = x[1:] + x[0] + 'ay'
        else:
            word = x + 'ay'
        pigLatin.append(word)
    return ' '.join(pigLatin)
def main_PigLatin():
    message = input("Please enter a scentence: ")
    print(getPigLatin(message))

rivers = {'Nile': 'Egypt'}
print(len(rivers))

#add something within a dictionary
rivers["Hillsborough"] = "Tampa"

print(rivers)
