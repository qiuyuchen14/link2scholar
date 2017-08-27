import json
with open("papers-2017-02-21-sample.json") as f:
    Authors = {}
    j=0
    missing = 0
    for i, line in enumerate(f):
        #print(line)
        data = json.loads(line)
        #  )
        A=data['authors']

        for x in A:
            if len(x['ids']) == 0:
                missing+=1
                continue
            if len(x['ids']) == 2:
                print(x)
                continue
            if x['ids'][0] not in Authors:
                Authors[x['ids'][0]]=j
                j+=1

        #print (type[Authors])




        if i == 1000000: break
    #print(Authors)
    print(j, missing)
