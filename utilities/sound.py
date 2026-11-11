import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"  # must be set before importing pygame

import time

try:
	import pygame
except ImportError:
	pygame = None

ASSET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

class SoundManager:
	def __init__(self, num_channels=32, min_gap=0.04):
		self.enabled = False
		self.sounds = {}
		self.last_played = {}
		self.min_gap = min_gap
		if pygame is None:
			return
		try:
			pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
			pygame.mixer.set_num_channels(num_channels)
			self.enabled = True
		except pygame.error:
			pass

	def load(self, name, filename, volume=1.0):
		if not self.enabled:
			return
		try:
			sound = pygame.mixer.Sound(os.path.join(ASSET_DIR, filename))
			sound.set_volume(volume)
			self.sounds[name] = sound
		except (pygame.error, FileNotFoundError):
			pass

	def play(self, name):
		sound = self.sounds.get(name)
		if not sound:
			return
		now = time.monotonic()
		if now - self.last_played.get(name, 0) < self.min_gap:
			return
		self.last_played[name] = now
		sound.play()

	def close(self):
		if self.enabled:
			pygame.mixer.quit