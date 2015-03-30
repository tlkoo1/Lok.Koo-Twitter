import twitter, datetime
#import HTTP library
import urllib2 

#open Google Chrome History
currentSession = open("/Users/tlkoo1/Library/Application Support/Google/Chrome/Default/Current Session") 

#variable that reads lastest session info
recentSession = currentSession.read() 

#My Twitter id
user = 3096333975 

#All my keys and access tokens
file = open("TwitterCredentials.txt")

#read TwitterCredentials
cred = file.readline().strip().split(',')

#create API wrapper
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

#get status update
statuses = api.GetUserTimeline(user,count=200) 

Indexopen = recentSession.rfind("http") 
Indexstop = recentSession.find(chr(0), Indexopen) 

url = recentSession[Indexopen:Indexstop]

print(url)

receivingurl = urllib2.urlopen(url) 
html = receivingurl.read()

#search for sources in between "title" tags
Titleopen = html.find("<title>") + len("<title>") 
Titleend = html.find("</title>", Titleopen)
#Open titles
Titles = html[Titleopen:Titleend] 

#displays "times"
stamp = datetime.datetime.utcnow() 

response = api.PostUpdate("Tweeted at - " + url + " at  " + str(stamp) + " Webpage: " + str(Titles)) 

print("Status updated to: " + response.text) 

