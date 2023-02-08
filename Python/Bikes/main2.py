from MountainBike import MountainBike

def main():
    rb = MountainBike(12,23,12)
    
    print(rb)
    print()
    rb.setHeight(100)
    rb.speedUp(12)
    
    print(rb)
    
    myMBike = MountainBike(12,23,12)
    
    if rb == myMBike:
        print("Equal")
    else:
        print("Not equal")
    
main()