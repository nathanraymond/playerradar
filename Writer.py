import pandas as pd 
from Shooting import ShotStats
from Possesion import PossesionStats
from Passing import PassingStats
from Defence import DefenceStats
from Misc import MiscStats

PlayerName = "Hazard" # Enter Player folder name e.g. Lukaku
Season = "2018-2019" # Enter season e.g. 2018-2019

class StatWriter():
	def __init__(self, PlayerName, Season):
		self.PlayerName = PlayerName
		self.Season = Season
	
	def list_stats(self):
		PlayerName = self.PlayerName
		Season = self.Season
		sh = ShotStats(self.PlayerName, self.Season).get_shots_stats()
		pos = PossesionStats(self.PlayerName, self.Season).get_possesion_stats()
		pas = PassingStats(self.PlayerName, self.Season).get_pass_stats()
		defe = DefenceStats(self.PlayerName, self.Season).get_defence_stats()
		mis = MiscStats(self.PlayerName, self.Season).get_misc_stats()
		liststats = []
		
		for s in pos:
			liststats.append(s)
		for s in sh:
			liststats.append(s)
		for s in pas:
			liststats.append(s)
		liststats.append(defe)
		liststats.append(mis)
		
		
		
		#for s in defe:
			#liststats.append(s)
		return liststats

	def df_stats(self):
		df = pd.DataFrame([self.list_stats()])
		df.columns=['touches_box', 'succ_dribbles','xG_per_shot', 'xG_90', 'shots_90', 'kp_90','ppa_90','xA_90', 'pperc','pressure_regains','fls_90']
		return df


df = StatWriter(PlayerName, Season).df_stats()
