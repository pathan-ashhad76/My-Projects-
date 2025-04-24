total=0
while True:
    print("1.Ice-Cream")
    print("2.Noodles")
    print("3.Dinner")
    print("4.Chinese")
    print("5.Fruit & Salad")
    print("6.Exit")
    x=int(input("enter the choice"))
    if(x==1):
        while True:
            print("1.Venilla-75Rs")
            print("2.Strawberry-100Rs")
            print("3.Chocolate-80Rs")
            print("4.Butter Scotch-90Rs")
            print("5.Exit")
            c=int(input("enter the choice"))
            if(c==1):
                q=int(input("enter the quantity"))
                total=total+q*75
                print("Total amount=",total)
            elif(c==2):
                q=int(input("enter the quantity"))
                total=total+q*100
                print("Total amount=",total)
            elif(c==3):
                q=int(input("enter the quantity"))
                total=total+q*80
                print("Total amount=",total)
            elif(c==4):
                q=int(input("enter the quantity"))
                total=total+q*90
                print("Total amount=",total)
            elif(c==5):
                break
    elif(x==2):
        while True:
            print("1.Chiclen Noodles-110Rs")
            print("2.Veg Noodles-80Rs")
            print("3.Mixed Noodles-130Rs")
            print("4.Egg Noodles-90Rs")
            print("5.Exit")
            c=int(input("enter the choice"))
            if(c==1):
                q=int(input("enter the quantity"))
                total=total+q*110
                print("Total amount=",total)
            elif(c==2):
                q=int(input("enter the quantity"))
                total=total+q*80
                print("Total amount=",total)
            elif(c==3):
                q=int(input("enter the quantity"))
                total=total+q*130
                print("Total amount=",total)
            elif(c==4):
                q=int(input("enter the quantity"))
                total=total+q*90
                print("Total amount=",total)
            elif(c==5):
                break
    elif(x==3):
        while True:
             print("1.Chiclen Dosa-130Rs")
             print("2.Mutton Dosa-160Rs")
             print("3.Chicken Dum Paratha-300Rs")
             print("4.Egg Fried Rice-100Rs")
             print("5.Veg fried Rice-75Rs")
             print("6.Exit")
             c=int(input("enter the choice"))
             if(c==1):
                 q=int(input("enter the quantity"))
                 total=total+q*130
                 print("Total amount=",total)
             elif(c==2):
                q=int(input("enter the quantity"))
                total=total+q*160
                print("Total amount=",total)
             elif(c==3):
                 q=int(input("enter the quantity"))
                 total=total+q*300
                 print("Total amount=",total)
             elif(c==4):
                 q=int(input("enter the quantity"))
                 total=total+q*100
                 print("Total amount=",total)
             elif(c==5):
                 q=int(input("enter the quantity"))
             elif(c==6):
                 break
    elif(x==4):
        while True:
            print("1.shawarma Roll-60Rs")
            print("2.chilli chicken-120Rs")
            print("3.veg manchuriyan-100Rs")
            print("4.Gobi mancuriyan-90Rs")
            print("5.Exit")
            c=int(input("enter the choice"))
            if(c==1):
                q=int(input("enter the quantity"))
                total=total+q*60
                print("Total Amount=",total)
            elif(c==2):
                q=int(input("enter the quantity"))
                total=total+q*120
                print("Total Amount=",total)
            elif(c==3):
                q=int(input("enter the quantity"))
                total=total+q*100
                print("Total Amount=",total)
            elif(c==4):
                q=int(input("enter the quantity"))
                total=total+q*90
                print("Total Amount=",total)
            elif(c==5):
                break
    elif(x==5):
        while True:
            print("1.Fruits Salad-100Rs")
            print("2.Dry friut Salad-80Rs")
            print("3.Exit")
            c=int(input("enter the choice"))
            if(c==1):
                q=int(input("enter the quantity"))
                total=total+q*100
                print("Total Amount=",total)
            elif(c==2):
                q=int(input("enter the quantity"))
                total=total+q*100
                print("Total Amount=",total)
            elif(c==3):
                break
    elif(x==6):
        break
print("Total Amount=",total)
            
            
