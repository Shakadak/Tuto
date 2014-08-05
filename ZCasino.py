#!/usr/bin/python
# -*-coding:Latin-1 -*

from random import randrange
from math import ceil

total = 100
while total > 0:
	print "you possess $", total
	bet = input("Please, enter the amount of your bet: ")
	try:
		bet = int(bet)
		assert 0 < bet and bet <= total
	except ValueError:
		print "You did not enter a number"
		continue
	except AssertionError:
		print "You are not allowed to propoe such a bet"
		continue
	pos = input("Please, enter where you want to place your bet: ")
	try:
		pos = int(pos)
		assert 0 <= pos and pos <= 49
	except ValueError:
		print "You did not enter a number"
		continue
	except AssertionError:
		print "You are not allowed to place your bet here"
		continue
	real = randrange(50)
	print "The boulder stopped at :", real
	if pos == real:
		total += 2 * bet
	elif pos % 2 == real % 2:
		total -= bet - ceil(0.5 * bet)
	else:
		total -= bet
print "No more currency, you may leave"
