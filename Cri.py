#Author: Yash Shah
#Email: blazonware@gmail.com

#!/usr/bin/python
import urllib
import sys
from subprocess import call
import commands
from time import sleep

class Score(object):
       
    scoreUrl = "<this should be the URL of score file>"
     
    def __init__(self):
    	# dictionary variables read from the score file
        self.vars = {} 
         
    def refresh(self):
        #Refresh the score
        url_opener = urllib.URLopener()
        url = url_opener.open(self.scoreUrl)
        self.vars = {}
        for stmt in url.read().split('\n'):
            stmt = stmt.strip()
            if stmt == "": continue
            var, val = stmt.split('=')
            self.vars[var] = val
        url.close()
        return self.vars
         
    def render(self):
        #Return the rendered text
        return "%(l1)s - %(message)s - %(tagline)s" % self.vars 
         
         
class RediffScore(Score):

	
    scoreUrl = "http://livechat.rediff.com:80/sports/score/score.txt"
    global sleepTime
    sleepTime=120 
         
    def getMatchName(self):
        return self.vars['tagline']
         
    def getScore(self):
        return self.vars['l2']
         
    def getTeams(self):
        return self.vars['l1']
         
    def getDate(self):
        return self.vars['date']
         
    def getMessage(self):
        return self.vars['message']
             

if __name__ == "__main__":
    while True:
    	try:
        #print 'Current score'
        	sc = RediffScore()
        	sc.refresh()
        	str="notify-send \"" + sc.render() + "\"" 
        	commands.getstatusoutput(str)
        #if sys.argv[1] is None:time.sleep(120) 
        except:
        	sleep(60)
	sleep(sleepTime)
