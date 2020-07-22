#Page 340
import time
import requests

print('Started.')
startTime = time.time() # get the first lap's start time
round(startTime)
print("startTime = ",startTime)

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

print("***Download complete***")
lastTime = time.time() # reset the last lap time
round(lastTime)
print("lastTime = ",lastTime)
print("time taken = ",lastTime-startTime)
print('\nDone.')
