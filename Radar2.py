import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from main import PlayerName, Season, FullPlayerName, PlayerName2, Season2, FullPlayerName2
from Writer import StatWriter
from Shooting import ShotStats
from Passing import PassingStats


variables = ('Touches in box', 'Succ Dribbles','xG/Shot', 'xG/90', 'Shots/90','xA/90', 'Passes into box','Kp/90', "Passing%", 'Pressure Regains','Fouls won')
df = StatWriter(PlayerName, Season).df_stats()
df2 = StatWriter(PlayerName2, Season2).df_stats()
values = df.iloc[0].tolist()
values2 = df2.iloc[0].tolist()
data = list(map(float, values))
data2 = list(map(float, values2))

ranges = [(0, 10), (0, 5),(0, 0.25), (0, 0.55), (0, 4), (0, 0.5), (0, 4),(0, 4), (0, 90), (0, 10), (0, 5)]
colour = "cornsilk"
colour2 = "black"


def _invert(x, limits):
    """inverts a value x on a scale from
    limits[0] to limits[1]"""
    return limits[1] - (x - limits[0])

def _scale_data(data, ranges):
    """scales data[1:] to ranges[0],
    inverts if the scale is reversed"""
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        assert (y1 <= d <= y2) or (y2 <= d <= y1)
    x1, x2 = ranges[0]
    d = data[0]
    if x1 > x2:
        d = _invert(d, (x1, x2))
        x1, x2 = x2, x1
    sdata = [d]
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        if y1 > y2:
            d = _invert(d, (y1, y2))
            y1, y2 = y2, y1
        sdata.append((d-y1) / (y2-y1) 
                     * (x2 - x1) + x1)
    return sdata

class ComplexRadar():
    def __init__(self, fig, variables, ranges,colour,colour2,
                 n_ordinate_levels=6):
        angles = np.arange(0, 360, 360./len(variables))

        axes = [fig.add_axes([0.1,0.1,0.8,0.78],polar=True,
                label = "axes{}".format(i)) 
                for i in range(len(variables))]
        l, text = axes[0].set_thetagrids(angles, 
                                         labels=variables, fontsize=11.8, position=(-0, -0.13), color="cornsilk",  fontweight='bold')
        [txt.set_rotation(angle-180) for txt, angle 
             in zip(text, angles)] 
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i], 
                               num=n_ordinate_levels)
            gridlabel = ["{}".format(round(x,2)) 
                         for x in grid]
            if ranges[i][0] > ranges[i][1]:
                grid = grid[::-1] # hack to invert grid
                          # gridlabels aren't reversed
            gridlabel[0] = "" # clean up origin
            ax.set_rgrids(grid, labels=gridlabel,
                         angle=angles[i], fontsize=7)
            #ax.spines["polar"].set_visible(False)
            ax.set_ylim(*ranges[i])
        # variables for plotting
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]
    def plot(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)
    def fill(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)
    def bgcolour(self, colour):
        self.ax.set_facecolor(colour)
    def figcolour(self, fig, colour2):
        fig.set_facecolor(colour2)
    

fig1 = plt.figure(figsize=(15, 15))
plt.figtext(0.09,0.23,FullPlayerName+" ("+str(Season)+")",color="magenta", fontsize=15, fontweight='bold')

plt.figtext(0.09,0.185,str(int(ShotStats(PlayerName, Season).total_goals()))+" goals & "+str(int(PassingStats(PlayerName, Season).get_assists()))+" assists in "+str(int(PassingStats(PlayerName, Season).get_mins()))+" league minutes", color="magenta", fontsize=11, fontweight='bold')

plt.figtext(0.09,0.93,FullPlayerName2+" ("+str(Season2)+")",color="Lime", fontsize=15, fontweight='bold')

plt.figtext(0.09,0.885,str(int(ShotStats(PlayerName2, Season2).total_goals()))+" goals & "+str(int(PassingStats(PlayerName2, Season2).get_assists()))+" assists in "+str(int(PassingStats(PlayerName2, Season2).get_mins()))+" league minutes", color="Lime", fontsize=11, fontweight='bold')

#plt.figtext(0.8,0.8,str(Season), color="magenta", fontsize=12, fontweight='bold')

axes = ComplexRadar(fig1, variables, ranges, colour, colour2)


axes.plot(data2, color="green")
axes.fill(data2, alpha=0.5, color="Lime")
axes.plot(data, color="purple")
axes.fill(data, alpha=0.5, color="magenta")
axes.bgcolour(colour)
axes.figcolour(fig1, colour2)
plt.show()