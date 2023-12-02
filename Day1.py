# Part 1 
values = input("Enter values array")

valueLines = values.split(" ")
sum = 0
for valueLine in valueLines :
    number = 0
    for character in valueLine :
        if character.isdigit():
            number = int(character)*10
            break

    for i in range(len(valueLine) - 1, -1, -1) :
        if valueLine[i].isdigit():
            number = number + int(valueLine[i])
            break
        
    print(f"Line {valueLine} :" + str(number))
    sum = sum + number
print("Sum :" + str(sum))

