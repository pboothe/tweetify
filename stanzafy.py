#!/usr/bin/env python3

def breakline(line):
    if len(line) <= 140:
        yield line
        return

    pieces = line.split(",")
    piece = ""
    for i in range(len(pieces)):
        if len(pieces[i]) >= 140:
            print("BAD LINE", line)
            print("FIX THIS CODE IF YOU SEE THIS MESSAGE")
        else:
            if len(piece + "," + pieces[i]) >= 140:
                yield piece + ","
                piece = pieces[i]
            else:
                piece = piece + "," + pieces[i]
    yield piece

def makeTweets(stanza):
    wholething = "\n".join(stanza)
    if len(wholething) < 140:
        return [ wholething ]
    else:
        tweets = []
        i = len(stanza) - 1
        while i >= 0:
            if i >= 1:
                tweet = stanza[i] + "\n" + stanza[i-1]
                if len(tweet) >= 140:
                    for subtweet in breakline(stanza[i]):
                        tweets.append(subtweet)
                    i -= 1
                    
                else:
                    tweets.append(tweet)
                    i -= 2
            else:
                tweet = stanza[0]
                i -= 1
                tweets.append(tweet)
        return tweets[::-1]
                

import sys
input = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
stanza = []
tweetcount = 0
for line in input:
    if line.strip() == "":
        tweets = makeTweets(stanza)
        for tweet in tweets: 
            f = open("tweets/%05d.txt" % tweetcount, "w") 
            tweetcount += 1
            print(tweet, file=f, end="")
        stanza = []
    else:
        if line.startswith(" ") and not line.strip().isdigit():
            stanza[-1] = stanza[-1] + " " + line.strip()
        else:
            stanza.append(line.strip())

if len(stanza) > 0:
    tweets = makeTweets(stanza)
    for tweet in tweets: 
        f = open("tweets/%05d.txt" % tweetcount, "w") 
        tweetcount += 1
        print(tweet, file=f)
    stanza = []
    
