import pandas as pd 




class DefenceStats():
	def __init__(self, PlayerName, Season):
		self.PlayerName = PlayerName
		self.Season = Season
	
	def get_season(self):
		df_defence = pd.read_csv("players\\"+self.PlayerName+"\\"+self.PlayerName+"_Defence.csv")
		df_defence.set_index("Season", inplace=True)
		defence = df_defence.loc[self.Season]
		return defence
	def get_defence_stats(self):
		defence = self.get_season()
		pressures = defence['Press']
		pressure_regains = defence['Succ']
		nineties = defence['90s']
		pressures_90 = round((pressures/nineties),2)
		pressure_regains_90 = round((pressure_regains/nineties),2)
		return pressure_regains_90
