from Bicycle import Bicycle

def main():
    b = Bicycle(8,25)
    print(b)
    b.applyBrake(3)
    print(b)
    
    b2 = Bicycle(8,25)
    if b==b2:
        print("equal")
    else:
        print("not equal")
    
main()