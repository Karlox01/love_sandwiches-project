import random

print('Welcome User!')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
horizontal = 3
vertical = 3


choose = input('\n Do you wish to proceed with the tic tac toe game? :').lower()


def displayField():
  for x in range(horizontal):
    print('\n+---+---+---+')
    print('|', end='')
    for y in range(vertical):
      print('', field[x][y], end=' |')
  print('\n+---+---+---+')





def inputInArray(num, turn):
  num -= 1
  if (num == 0):
    field[0][0] = turn
  elif (num == 1):
    field[0][1] = turn
  elif (num == 2):
    field[0][2] = turn
  elif (num == 3):
    field[1][0] = turn
  elif (num == 4):
    field[1][1] = turn
  elif (num == 5):
    field[1][2] = turn
  elif (num == 6):
    field[2][0] = turn
  elif (num == 7):
    field[2][1] = turn
  elif (num == 8):
    field[2][2] = turn


def checkWhoWon(field):

  ### X Axis
  if (field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X'):
    print('X has won!')
    return True
  elif (field[0][0] == 'O' and field[0][1] == 'O' and field[0][2] == 'O'):
    print('O has won!')
    return True
  elif (field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X'):
    print('X has won!')
    return True
  elif (field[1][0] == 'O' and field[1][1] == 'O' and field[1][2] == 'O'):
    print('O has won!')
    return True
  elif (field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X'):
    print('X has won!')
    return True
  elif (field[2][0] == 'O' and field[2][1] == 'O' and field[2][2] == 'O'):
    print('O has won!')
    return True

  ### Y Axis
  elif (field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X'):
    print('X has won!')
    return True
  elif (field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O'):
    print('O has won!')
    return True
  elif (field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X'):
    print('X has won!')
    return True
  elif (field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O'):
    print('O has won!')
    return True
  elif (field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X'):
    print('X has won!')
    return True
  elif (field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O'):
    print('O has won!')
    return True
  ### Cross  wins
  elif (field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X'):
    print('X has won!')
    return True
  elif (field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O'):
    print('O has won!')
    return True
  elif (field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X'):
    print('X has won!')
    return True
  elif (field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O'):
    print('O has won!')
    return True
    


leaveLoop = False
turn = 'X'
turnCounter = 0


if (choose == 'yes'):
  while (leaveLoop == False):
    if (checkWhoWon(field) == True):
      break

  ### Its the player turn
    if (turnCounter % 2 == 1):
      displayField()
      chosenNumber = int(input('\n chose a number between 1 and 9 : '))
      if (chosenNumber >= 1 and chosenNumber <= 9 and chosenNumber != aiChoice):
        inputInArray(chosenNumber, 'X')
        numbers.remove(chosenNumber)
        checkWhoWon(field)
        turnCounter += 1
      else:
        print('Invalid input number, Please try again , Numbers 1 - 9 ONLY!****')
      

  ### Competitors turn
    else:
      while (True):
        aiChoice = random.choice(numbers)
        print('\n Computer has chosen: ', aiChoice)
        if (aiChoice in numbers):
          inputInArray(aiChoice, 'O')
          numbers.remove(aiChoice)
          turnCounter += 1
          break
else:
  print('Oh never mind than play once u feel like it :)')



