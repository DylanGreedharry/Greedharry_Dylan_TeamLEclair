import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Greedharry-Dylan"
        # On initialise une variable afin d'avoir les pas de temps
        self.pas_temps = 0

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
    	# On ajoute la condition qu'on avance le temps de 200 pas de temps
    	if (self.pas_temps < 200):
    		print(self.pas_temps) # On affiche les pas de temps
    		acceleration = 1
    		#On regarde le 3ème noeud afin d'avoir le steering
    		steering = np.array(obs["paths_end"][self.path_lookahead-1][0])
    		action = {
    			"acceleration": acceleration,
    			"steer": steering,
    			# On met tout à False afin que ça ne perturbe pas le kart
    			# avec des infos non nécessaire
    			"brake": False,
    			"drift": False,
    			"nitro": False,
    			"rescue": False,
    			"fire": False,
    		}
    		self.pas_temps += 1 # Incrémentation de la variable pas de temps
    		return action
