print("You come across a long winding path. You can make a choice to go left or right to find a destination.")
l = 3
while True:
    direction = input("Do you go left or right? ")
    if direction == "left":
        print("You turn left.")
        l += 1
    elif direction == "right":
        print("You turn right.")
        l -= 1
    else:
        print("Invalid input. Please try again.")
    if l == 6:
        print("You come across a river.")
        boo = True
        break
    elif l == 0:
        print("You come across a cave.")
        boo = False
        break
if boo == True:
    print("yayyyy river story")
elif boo == False:
    print("yayyyy cave story")
else:
    print("You borke the game ;-;")
    
# Path: Test.py