import math

def distance(position1, position2):
	return math.sqrt(pow(position1[1] - position2[1], 2) + pow(position1[0] - position2[0], 2))