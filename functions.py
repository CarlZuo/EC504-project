import os.path
import time
import csv
def load_csv(path,file_name):
    documents_list = []
    with open(os.path.join(path, file_name), newline='',encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            documents_list.append(row['content'])
    print("Total Number of Documents:",len(documents_list))
    return documents_list


def findKeynorm(twis,keys):
    time_start = time.time_ns()

    count = list()
    for i in range(0,len(twis)):
        twi = twis[i]
        num = 0
        for word in twi:
            for key in keys:
                if word == key:
                    num = num+1
        count.append([i,num])
    sort = list()
    for i in range(0,11):
        sort.append([-1,0])                
    for cand in count:
        num = cand[0]
        wds = cand[1]
        for i in range(9,-1,-1):
            if(wds > sort[i][1]):
                sort[i+1][0] = sort[i][0]
                sort[i+1][1] = sort[i][1]
                sort[i][0] = num
                sort[i][1] = wds
    rtn = list()
    for i in range(0,10):
        rtn.append(sort[i][0])

    time_end = time.time_ns()
    time_tot = time_end-time_start
    print("it takes "+ str(time_tot) + " nano second to finsh search")
    return rtn


def loadTwee(twis):
    time_start = time.time_ns()
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

    time_end = time.time_ns()
    time_tot = time_end-time_start
    print("it takes "+ str(time_tot) + " nano second to load inverted index dataset")
    return data

def findKey(data,keys):
    time_start = time.time_ns()
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

    time_end = time.time_ns()
    time_tot = time_end-time_start
    print("it takes "+ str(time_tot) + " nano second to finsh search in inverted index")
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
    keys = ["apple","pie","sweet","trump","2020"]

    raw = load_csv("","IRAhandle_tweets_1.csv")
    twi = list()
    for sent in raw:
        twi.append(sent.split())


    
    #print(rtn)
    data = loadTwee(twi)
    rtn = findKey(data,keys)
    rtn = findKeynorm(twi,keys)
    #print(rtn)
    #for i in rtn:
    #    print(raw[i])
