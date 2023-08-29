from phonetic import getWordPhonetic
import pyperclip
from time import perf_counter

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
        req = getWordPhonetic(token)
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