print('You are welcome to our quiz app!😱')
playing = input('Do you want to play? ')
if playing.lower() != 'yes':
    print('Come again when you are ready👇')
    quit()
print('Lets start🤘')
score = 0
answer = input('What is CRUD? ')
if answer.lower() == 'create, read, update, delete':
    print('correct👍')
    score += 1
else:
    print('Incorrect🥸')
answer = input('What is JSON? ')
if answer.lower() == 'javaScript object notation':
    print('correct👍')
    score += 1
else:
    print('Incorrect🥸')
answer = input('What is SQL? ')
if answer.lower() == 'structured query language':
    print('correct👍')
    score += 1
else:
    print('Incorrect🥸')
print("You have" + str(score) + "questions correct")
print("You got" + str((score / 4) * 100) + "%")