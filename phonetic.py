import requests
import json

def getRequestData(query):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{query}"
    page = requests.get(url)
    stcode = page.status_code

    if (stcode == "404" or stcode == 404):
        print(f"Query rejected: [{query}] - [{stcode}]")
        return 404
    else:
        print(f"Query successful: [{query}] - [{stcode}]")
        return page.text

def getWordPhonetic(word):
    req = getRequestData(word)
    data = ""
    if (req != 404):
        data = json.loads(req)
    else:
        return (word,False)
    
    phn = ""
    try:
        phn = data[0]["phonetic"]
    except:
        try:
            phn = data[0]["phonetics"][0]["text"]
        except:
            try:
                phn = data[0]["phonetics"][1]["text"]
            except:
                return (word,False)

    return (phn,True)