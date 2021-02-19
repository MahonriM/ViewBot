import pywhatkit
from time import  sleep
try:
    url="https://www.youtube.com/watch?v=MvodXLnd89o"
    #"https://www.youtube.com/watch?v=Jp1p_cEpyR8"
    while 10:
        sleep(30)
        pywhatkit.playonyt(url)
        print("Playing")
except:
    print("Network Error Occured")
