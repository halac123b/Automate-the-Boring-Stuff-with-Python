import random

numberOfStreak = 0
streak = 0
check = 0

for i in range(10000):
	for j in range(100):
		# Code that creates a list of 100 'heads' or 'tails' values.
		coin = random.randint(0, 1)
		if coin == check:
			streak += 1
		else:
			check = coin
			streak = 1
		if streak == 6:
			numberOfStreak += 1
			streak = 0
	streak = 0

print('Chance of streak: %s%%' % (numberOfStreak / (100 / 6 * 10000)))
print(numberOfStreak)