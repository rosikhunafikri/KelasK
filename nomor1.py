# main.py
import sys

def split(word): 
    return [char for char in word]  

def process(sentence):
    kalimat = sentence.split()
    kalimat_baru = ""
    for kata in kalimat:
        kata = split(kata)
        kata.reverse()
        if (kalimat_baru != ""):
            kalimat_baru += " "
        kalimat_baru += "".join(kata)
    print(kalimat_baru)

if __name__ == "__main__":
    if len(sys.argv)<2 or sys.argv[1] is None:
        process("italem irad irigayaj")
        process("iadab itsap ulalreb")
        process("nalub kusutret gnalali")
    else:
        process(sys.argv[1])
