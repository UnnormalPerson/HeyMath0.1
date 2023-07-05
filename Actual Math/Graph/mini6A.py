#Hey, if gradx is zero, then it's supposed to be undefined, due to the graph being a vertical line.
#Exec statement is necessary, due to it if being an erorr then it would entirely skip re-asking if the user wants to continue.
import random
import time
quit = False
while not quit:
  x1 = random.randint(0, 5)
  x2 = random.randint(0, 5)
  y1 = random.randint(0, 5)
  y2 = random.randint(0, 5)
  while x1 > x2:
    x1 = random.randint(0, 5)
  print('The first point is at ' + str(x1) + ',' + str(y1) + '.')
  print('The second point is at ' + str(x2) + ',' + str(y2) + '.')
  gradx = x2 - x1
  grady = y2 - y1
  if gradx != 0:  # Check if gradx is non-zero
    gradient = round(grady / gradx, 1)
  else:
    gradient = 'undefined'
  gradans = float(input('What is the gradient of the graph, rounded to 1 decimal point? '))
  time.sleep(5)
  if gradient == 'undefined':
    if gradans.lower == gradient:
      print ('Congrats! You are correct!')
    else:
      print('Oops! You are wrong. The correct answer is undefined, as the x axis remains the same.')
  elif gradient == gradans:
    print('Congrats! You are correct!')
  else:
    print('Oops! You are wrong. The correct answer is ' + str(gradient) + '.')
  rerun_exec = '''rerun = input('Do you want to continue? (y/n) ')
if rerun == 'n':
  print('Alright. Have a good day!')
  quit = True
elif rerun == 'y':
  print('------------------')
else:
  print('Error')
  exec (rerun_exec)'''
  exec (rerun_exec)
