import itertools
import time
def nextto(h1,h2):
    return abs(h1-h2) == 1

def imright(h1,h2):
    return h1-h2 == 1

def zebra_puzzle():
    """Return a tuple (WATER, ZEBRA) indicating their house numbers."""
    houses = first, _, middle, _, _ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
		for (englishman, spaniard, ukranian, japanese, norwegian) in orderings
                if englishman is red
                if norwegian is first
                if nextto(norwegian, blue)
		#for (dog, snails, fox, horse, ZEBRA) in orderings
		for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if ukranian is tea
                if milk is middle
		for (oldgold, kools, chesterfields, luckystrike, parliaments) in orderings
		#if englishman is red - this condition will be moved after when we loop through house and nationalities to make it faster
                if kools is yellow
                if luckystrike is oj
                if japanese is parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
		if spaniard is dog
		#if coffee is green
		#if ukranian is tea
		#if imright(green, ivory)
		if oldgold is snails
		#if kools is yellow
		#if milk is middle
		#if norwegian is first
		if nextto(chesterfields, fox)
		if nextto(kools, horse)
		#if luckystrike is oj
		#if japanese is parliaments
		#if nextto(norwegian, blue)
		)
##def t():
##    t0 = time.clock()
##    print (zebra_puzzle())
##    t1 = time.clock()
##    return t1-t0
##print t()
def timedcall(fn, *args):
    """Call function and return elapsed time."""
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result
print timedcall(zebra_puzzle)
