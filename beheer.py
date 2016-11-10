import os
count = len(open('queue.csv').readlines())
while count > 1:
    count = len(open('queue.csv').readlines())
    os.system("tweetbeheren.py 1")

print('Op dit moment zijn er geen openstaande berichten.')
