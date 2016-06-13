import sys, os, re, operator, math
#This class is not used.
class Player:  #I decided not to use the player class ultimately, but I left it here just for my use later since our lab isn't being graded on style
    def _init_(self, name, totalHits, totalBats, totalRuns):
        self.name = name
        self.totalHits = totalHits
        self.totalBats = totalBats
        self.totalRuns = totalRuns
    
    @staticmethod
    def get_definition():
        return "A Player is a record of the stats of someone who plays for a baseball team."
    
    @staticmethod
    def get_batting_average():
        return totalBats/totalHits
    #END CLASS
    
#this is where the actually used code begins    
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename = sys.argv[1]
 
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

f = open(filename)  

file_info = f.read()

baseball_regex = re.compile("(\w+ \w+) batted (\d+?) times with (\d+?) hits and (\d+?) runs")

bplayer_stats = baseball_regex.findall(file_info)

players = {}  #I was going to use a player class to hold/manipulate the player stats/information, but I realized that a dictionary would be easier in
# this case considering what I needed to do

for p in bplayer_stats:  #goes through the file information and assigns the appropriate batting, hitting, and running amounts for each player
    if (p[0] in players.keys()): # adds the new hits/bats/runs to the old one for this player
        bats, hits, runs = players[p[0]]
        players[p[0]] = ((int)(bats) + (int)(p[1]), (int)(hits) + (int)(p[2]), (int)(runs) + (int)(p[3]))
    else:  #otherwise, creates a new player with these stats
        players[p[0]] = (p[1], p[2], p[3]) 

#print players        
batting_averages = {};
for b, p in players.items(): ##calculates the batting averages for every player to 3 decimal places
    batting_averages [b] = '%.3f' % round((float)(p[1])/(float)(p[0]), 3)

#sorts the batting averages in descending order based
sorted_batting_averages = sorted(batting_averages.items(), key = operator.itemgetter(1), reverse=True)

for i in sorted_batting_averages:
    print i[0] + ": " + i[1]

#End Program