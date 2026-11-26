from entities.tower_subclasses.basetower import BaseTower

class Power(BaseTower):
	DEFAULT_SPRITE = "✪"
	DEFAULT_DAMAGE = 25
	DEFAULT_FIRE_RATE = 20
	DEFAULT_RANGE = 20
	DEFAULT_COST = 15
	DEFAULT_MAX_TARGETS = 1
	DEFAULT_N_TARGETS = 0
	DEFAULT_PROJECTILE = "✢"
	DEFAULT_SOUND = "power"