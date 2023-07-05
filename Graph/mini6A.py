import random
import time
import numpy #Joshua, this is for graph I think
quit = False
while quit == False:
  x1 = random.randint (0,5)
  x2 = random.randint (0,5)
  y1 = random.randint (0,5)
  y2 = random.randint (0,5)
  while x1 > x2:
    x1 = random.randint (0,5)
  print ('The first point is at '+str(x1)+','+str(y1)+'.')
  print ('The second point is at '+str(x2)+','+str(y2)+'.')
  gradx = x2-x1
  grady = y2-y1
  gradient = ((round)grady/gradx, 1)
  gradans = float (input ('What is the gradient of the graph, rounded to 1 decimal point?'))
  time.sleep (5)
  if gradient == gradans:
    print ('Congrats! You are correct!)
  else:
    print ('Oops! You are wrong. The correct answer is '+(str(gradient))+'.')
  execrerun = '''
  rerun = input('Do you want to continue? (y/n)'
  if rerun == 'n':
    print ('Alright. Have a good day!')
    quit = True
  elif rerun == 'y':
    print ('------------------')
  else:
    print ('Error')
    exec (execrerun)
  '''
