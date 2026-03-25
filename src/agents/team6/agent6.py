import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Greedharry-Dylan"

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
    	# Nous mettons une valeur faible tel que 0.1 
    	# afin que le kart ne finisse pas dans un mur
    	# et qu'il puisse faire un tour sur lui-même
        acceleration = 0.1
        # Le steering est à 1 afin qu'il puisse faire ne steer qu'à droite
        # et faire un tour sur lui-même à droite.
        # Mais on aurait pu mettre -1 également 
        # afin que le kart fait un tour sur lui-même qu'à gauche
        steering = 1
        # steering = -1
        action = {
            "acceleration": acceleration,
            "steer": steering,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": bool(random.getrandbits(1)),
            "nitro": bool(random.getrandbits(1)),
            "rescue":bool(random.getrandbits(1)),
            "fire": bool(random.getrandbits(1)),
        }
        return action
