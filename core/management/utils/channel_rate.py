from core.models import Channel,Content
import operator

ratingDict = {}
tempArr = []

def average(lst: list[float]) -> float:
    return sum(lst) / len(lst)

def containsSubChan(chan: Channel) -> float:
    relatedSubs = Channel.objects.filter(parent_channel_id = chan.id)
    for subs in relatedSubs:
        if subs.title in ratingDict: 
            tempArr.append(ratingDict[subs.title])
        else: 
            containsSubChan(subs)
    return round(average(tempArr),2)

def containsContents(channels: list[Channel]) -> None:
    for chan in channels:
        relatedSubs = Channel.objects.filter(parent_channel_id = chan.id)
        content = Content.objects.filter(channel_id = chan.id)
        if not relatedSubs:
            arr = []
            for con in content:
                arr.append(con.rating)  
            ratingDict[chan.title] = round(average(arr),1) 

def ratingAlgorithm(channels: list[Channel]) -> dict[str, float]:
    containsContents(channels)
    for chan in channels:
        if chan.title not in ratingDict:
            ratingDict[chan.title] = containsSubChan(chan)
            tempArr.clear()

    return (dict(sorted(ratingDict.items(), key=operator.itemgetter(1),reverse=True)))