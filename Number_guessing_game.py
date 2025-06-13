import random 
Number_to_guess= random. randint (1,100)
guess= None
attempts= 0       
print("Welcome Player, guess a number between 1 to 100 ")
while guess! = Number_to_guess:
  guess= int(input("your guess😊: "))
  attempts += 1
while guess < Number_to_guess:
  print("Too low !")
elif guess > Number_to_guess:
  print("Too high ")
else:
  print("Correct! you guessed the number  "in attempts)

  