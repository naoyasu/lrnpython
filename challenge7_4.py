numner = [3, 4, 66, 894, 5789, 58990]

while True:
    answer = input("number or q to quit")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please value or q")
    if answer in numner:
        print("seikai")
    else:
        print("fuseikai")
    
        
    
    
