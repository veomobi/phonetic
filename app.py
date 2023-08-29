from phonetic import getWordPhonetic
import pyperclip
from time import perf_counter,sleep
from threading import Thread

lookup = {}
active = []

class T:
    def __init__(self, thread) -> None:
        self.thread = thread
    
    def run(self):
        self.thread.start()
        active.append(self)
#thread manager class to simplify checking thread lifetime

def task(word):
    req = getWordPhonetic(word)
    lookup[word] = req

def main(arg = None):
    sentence,tokens = "",""
    if arg == None:
        sentence = input("Input sentence: ")
    else:
        sentence = arg
    tokens = sentence.split(" ")
    final = ""

    print("SENDING REQUESTS: ")

    start = perf_counter()
    for token in tokens:
        if (not token in dict.keys(lookup)):
            newT = Thread(target=task,args=[token])
            tM = T(newT)
            tM.run()

    while len(active) != 0:
        for t in active:
            if not t.thread.is_alive():
                active.remove(t)
    #check if all threads are finished (in a very dumb way)
    sleep(0.1) #additional delay to be safe
    for token in tokens:
        req = lookup[token]
        phn = req[0]
        isValid = req[1]
        
        if isValid:
           phn = phn[1:-1]
        else:
            phn = token
        final += f'{phn} '

    stop = perf_counter()
    perf = stop-start
    pyperclip.copy(final)
    print(f"Finished in [{round(perf,2)}s]")
    print(final)
    return (sentence,final,perf)

main()