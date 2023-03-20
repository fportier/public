from seq import seq

def inCommon(seq1,seq2):
    list1 = seq1.getSeq()
    match = False
    for x in seq2.getSeq():
        if x in list1:
            match = True
            break
    if match:
        return True,x
    else:
        return False, None

def main():
    test1 = seq(1,3,12)
    print(test1)
    test2 = seq(5,5,10)
    print(test2)
    found, val = inCommon(test1,test2)
    if found:
        print("First in common is",val)
    else:
        print("no match")
    
main()
