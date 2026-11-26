from entities.tower_subclasses.basetower import BaseTower

class Rock(BaseTower):
	DEFAULT_SPRITE = "♖"
	DEFAULT_DAMAGE = 30
	DEFAULT_RANGE = 30
	DEFAULT_COST = 20
	DEFAULT_MAX_TARGETS = 1
	DEFAULT_N_TARGETS = 0
	DEFAULT_FIRE_RATE = 30
	DEFAULT_PROJECTILE = "❁"
	DEFAULT_SOUND = "rock"