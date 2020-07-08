import pandas as pd 




class ShotStats():
	def __init__(self, PlayerName, Season):
		self.PlayerName = PlayerName
		self.Season = Season

	def get_season(self):
		PlayerName = self.PlayerName
		Season = self.Season
		df_shooting = pd.read_csv("players\\"+self.PlayerName+"\\"+self.PlayerName+"_Shooting.csv")
		df_shooting.set_index("Season", inplace=True)
		shooting = df_shooting.loc[self.Season]
		return shooting
	
	def total_shots(self):
		shooting = self.get_season()
		shs = shooting['Sh']
		return shs
	
	def total_goals(self):
		shooting = self.get_season()
		goals = shooting['Gls']
		return goals
	
	def get_shots_stats(self):
		shooting = self.get_season()
		xG = shooting['xG']
		shots = shooting['Sh']
		nineties = shooting['90s']
		goals = shooting['Gls']
		shots_90 = round((shots/nineties),2)
		xG_per_shot = round((xG/shots),2)
		xG_90 = round((xG/nineties),2)
		Goals_90 = round((goals/nineties),2)
		return xG_per_shot, xG_90, shots_90
	
