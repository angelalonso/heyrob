import sys, os
url=os.system('youtube-dl -g https://www.youtube.com/watch?v=vw61gCe2oqI')
os.system('omxplayer '+ str(url))
