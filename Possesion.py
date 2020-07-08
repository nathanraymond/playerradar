import pandas as pd 
from Shooting import ShotStats

class PossesionStats():
	def __init__(self, PlayerName, Season):
		self.PlayerName = PlayerName
		self.Season = Season
	
	def get_season(self):
		PlayerName = self.PlayerName
		Season = self.Season
		df_possesion = pd.read_csv("players\\"+self.PlayerName+"\\"+self.PlayerName+"_Possesion.csv")
		df_possesion.set_index("Season", inplace=True)
		possesion = df_possesion.loc[self.Season]
		return possesion

	def get_possesion_stats(self):
		possesion = self.get_season()
		nineties = possesion['90s']
		att_pen = possesion['Att Pen']
		touches = possesion['Touches']
		dribbles = possesion['Succ']
		dribbles_90 = round((dribbles/nineties),2)
		touches_in_box = round((att_pen/nineties),2)
		shots = ShotStats(self.PlayerName, self.Season).total_shots()
		shot_touch_perc = round(((shots/touches)*100),2)
		return touches_in_box, dribbles_90

