import json
with open('stratdict.json') as f:
    stratDict = json.load(f)
    GenKEYList = list(stratDict.keys())
    print(GenKEYList[0])
    GenVALList = list(stratDict.values())
    print(GenVALList[0])