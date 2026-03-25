import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent1(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Greedharry-Dylan"
        self.time_marche_arr_init = 0

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        # Pendant 60 frames, le kart fait un tour sur
        # lui-même vers la droite
        if (self.time_marche_arr_init < 60):
            acceleration = 0.1
            steering = 1
            action = {
                "acceleration": acceleration,
                "steer": steering,
                "brake": False, # bool(random.getrandbits(1)),
                "drift": bool(random.getrandbits(1)),
                "nitro": bool(random.getrandbits(1)),
                "rescue":bool(random.getrandbits(1)),
                "fire": bool(random.getrandbits(1)),
            }
            self.time_marche_arr_init += 1
            print(self.time_marche_arr_init)
            return action
        #A partir de ce moment-là le kart est dans la bonne position
        # Et il roule en marche arrière jusqu'à la fin de la course
        else:
            acceleration = 0
            steering = obs["paths_end"][self.path_lookahead-1][0] #Visé du troisième
            action = {
                "acceleration": acceleration,
                "steer": steering,
                "brake": True, # bool(random.getrandbits(1)),
                "drift": bool(random.getrandbits(1)),
                "nitro": bool(random.getrandbits(1)),
                "rescue":bool(random.getrandbits(1)),
                "fire": bool(random.getrandbits(1)),
            }
            self.time_marche_arr_init += 1
            return action