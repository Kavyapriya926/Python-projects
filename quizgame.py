
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does CD stand for? ")
if answer.lower() == "compact disk":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does DOC stand for? ")
if answer.lower() == "document":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does IP stand for? ")
if answer.lower() == "internet protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does MS stand for? ")
if answer.lower() == "microsoft":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does ROM stand for? ")
if answer.lower() == "read-only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 9) * 100) + "%.")