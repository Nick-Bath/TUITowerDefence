from entities.tower_subclasses.basetower import BaseTower

class Magic(BaseTower):
	"""Magic Tower inherits from BaseTower"""
	
	DEFAULT_SPRITE = "✷"
	DEFAULT_DAMAGE = 10
	DEFAULT_RANGE = 20
	DEFAULT_COST = 30
	DEFAULT_MAX_TARGETS = 2
	DEFAULT_N_TARGETS = 0
	DEFAULT_FIRE_RATE = 10
	DEFAULT_PROJECTILE = "✧"
	DEFAULT_SOUND = "magic"