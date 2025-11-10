# write a program in python to create a menu-driven fast-food order system using the 'match case' feature.
    # -For example:
        # - Press 1 to order a Sandwich
        # - Press 2 to order a Pizza
        # - Press 3 to order a Burger
    # -Extend this program by adding a nested match case for each menu item's subtype selection by the user.
    # - For example:
        # - Press 1 for thin crust pizza
        # - Press 2 for cheese burst pizza
        # - Press 3 for fresh dough pizza
        
while True:
    print("Press 1 for sandwich : ")
    print("Press 2 to order a Pizza : ")
    print("Press 3 to order a Burger : ")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            print("=" * 30)
            print("you ordered a sandwich")
            print("=" * 30)
        case 2:
            print("Press 1 for thin crust pizza")
            print("Press 2 for cheese burst pizza")
            print("Press 3 for fresh dough pizza")
            type = int(input("Enter your pizza type: "))
             
            match type:
                case 1:
                    print("=" * 30)
                    print("you ordered a thin crust pizza")
                    print("=" * 30)
                    
                case 2:
                    print("=" * 30)
                    print("you ordered a cheese burst pizza")
                    print("=" * 30)
                    
                case 3:
                    print("=" * 30)
                    print("you ordered a fresh dough pizza")
                    print("=" * 30)
                    
                case _:
                    print("Invalid pizza type...")
        case 3:
            print("=" * 30)
            print("you ordered a Burger")
            print("=" * 30)
        case 0:
            break
        case _:
            print("Invalid choice...")