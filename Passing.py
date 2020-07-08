import pandas as pd 



class PassingStats():
	def __init__(self, PlayerName, Season):
		self.PlayerName = PlayerName
		self.Season = Season
	
	def get_season(self):
		df_passing = pd.read_csv("players\\"+self.PlayerName+"\\"+self.PlayerName+"_Passing.csv")
		df_passing.set_index("Season", inplace=True)
		passing = df_passing.loc[self.Season]
		return passing
	
	def get_pass_stats(self):
		passing = self.get_season()
		xA = passing['xA']
		kp = passing['KP']
		ppa = passing['PPA']
		pperc = passing['TCmp%']
		nineties = passing['90s']
		kp_90 = round((kp/nineties),2)
		xA_90 = round((xA/nineties),2)
		ppa_90 = round((ppa/nineties), 2)
		return xA_90, ppa_90,kp_90,pperc
	
	def get_assists(self):
		passing = self.get_season()
		assits = passing['Ast']
		return assits

	def get_mins(self):
		passing = self.get_season()
		nineties = passing['90s']
		Mins = round(nineties*90)
		return Mins
