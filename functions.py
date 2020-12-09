def loadTwee(twis):
    data = dict()
    for i in range(0,len(twis)):
        for word in twis[i]:
            if word in data:
                if data[word][-1][0] is i:
                    data[word][-1][1] = data[word][-1][1] + 1
                else:
                    data[word].append([i,1])
            else:
                data[word] = [[i,1]]
    return data

def findKey(data,keys):
    count = dict()
    for key in keys:
        if key in data:
            for twi in data[key]:
                if twi[0] in count:
                    count[twi[0]] = count[twi[0]] + twi[1]
                else:
                    count[twi[0]] = twi[1]
    sort = list()
    for i in range(0,11):
        sort.append([-1,0])                
    for cand in count:
        num = cand
        wds = count[cand]
        for i in range(9,-1,-1):
            if(wds > sort[i][1]):
                sort[i+1][0] = sort[i][0]
                sort[i+1][1] = sort[i][1]
                sort[i][0] = num
                sort[i][1] = wds
    rtn = list()
    for i in range(0,10):
        rtn.append(sort[i][0])
    return rtn



if __name__=="__main__":
    raw = ["this is the first test sentence",
    "this sentence is about apple",
    "test sentence is a good aplle",
    "anything about apple is a sentence",
    "apple apple apple sentence sentence sentence",
    "apple sentence a a a a ",
    "good sentence good apple a",
    "this sentence a a a a a",
    "good good good",
    "the sentence is a good apple",
    "apple is good sentence is a good thing",
    "nothing is a good apple",
    "good sentence apple"]
    keys = ["apple"]
    twi = list()
    for sent in raw:
        twi.append(sent.split())
    data = loadTwee(twi)
    rtn = findKey(data,keys)
    print(rtn)
