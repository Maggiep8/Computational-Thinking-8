# Beginning: Create Variables
cat_points = 0
dog_points = 0

# Middle: Ask Questions
answer = input ("would you rather have A) chocolate ice cream, or B) vanilla ice cream")
if answer == "A":
    cat_points += 1
elif answer == "B":
    dog_points += 1


answer = input ("would you rather spend a day A) on the beach B) in the snow")   
if answer == "A":
    dog_points += 1
elif answer == "B":
    cat_points += 1


answer = input ("would you rather live A) in the forest B) in the city")
if answer == "A":
    cat_points += 1
elif answer == "B":
    dog_points += 1


answer = input ("would you rather always be A) too hot or B) too cold")
if answer == "A":
    dog_points += 1
elif answer == "B": 
    cat_points += 1


answer = input ("would you rather have A) sweet B) salty")
if answer == "A":
    dog_points += 1
elif answer == "B":
    cat_points 

#End: Results
if cat_points > dog_points:
    print("your are a cat person")
if dog_points > cat_points:
    print("you are a dog person")
if dog_points == cat_points:
    print ("you are a cat and dog person")