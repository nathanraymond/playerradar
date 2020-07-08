import pandas as pd 



class MiscStats():
	def __init__(self, PlayerName, Season):
		self.PlayerName = PlayerName
		self.Season = Season
	
	def get_season(self):
		df_misc = pd.read_csv("players\\"+self.PlayerName+"\\"+self.PlayerName+"_Misc.csv")
		df_misc.set_index("Season", inplace=True)
		misc = df_misc.loc[self.Season]
		return misc
	def get_misc_stats(self):
		misc = self.get_season()
		fouls = misc['Fld']
		nineties = misc['90s']
		fls_90 = round((fouls/nineties),2)
		return fls_90