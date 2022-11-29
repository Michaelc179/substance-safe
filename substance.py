def weed():
    amount = float(input("How much did you put in? (g): "))
    if amount > 0:
        print("If you had taken marijuana, you would have experienced changes in mood, impaired body movements, an altered sense of time and more.")
        print("Any more, and you may have experienced hallucinations and delusions.")

def edibles():
    amount = float(input("How much did you put in? (THC mg): "))
    if 0<amount<5:
        print("If you had taken this amount, you would have experienced a mild high. You will feel less coordinated and frankly silly")
    elif 5<=amount<20:
        print("If you had taken this amount, you would have experienced a moderate high. You will feel more relaxed and less coordinated")
    elif 20<=amount<50:
        print("If you had taken this amount, you would have experienced a strong high. Expect strong euphoria and impaired coordination")
    elif amount>=50:
        print("If you had taken this amount, you would have experienced an extreme high. Expect extreme euphoria and impaired coordination. There could be very adverse consequence to taking this much, thank you for being cautious and considerate of your health.")
    else:
        print("Invalid input")
        edibles()

def alcohol():
    drink = input("What drink did you put in? (Beer, Wine, Liquor): ")
    if drink == "Beer":
        print("Beer is a rather mild drink, and moderate drinking has some benefits such as heart health and prevention of blood clots. However, too much, and you risk liver disease")
    elif drink == "Wine":
        print("Wine is a rather mild drink, and moderate drinking has some benefits such as heart health and prevention of blood clots. However, too much, and you risk liver disease")
    elif drink == "Liquor":
        print("Liquor such as Vodka or Rum is a fairly strong dirnk, and you risk liver disease, stroke, sleep disorders, and depression if you take too much")

def nicotine():
    print("Nicotine is a very addictive substance, and is known to cause cancer, heart disease, and more. Do your best to refrain from taking any!")

def cigarettes():
    print("Cigarettes are very addictive, and are known to cause cancer, heart disease, and more. Do your best to refrain from taking any!")

def cocaine():
    print("DON'T DO COCAINE")
    print("COCAINE CAN EASILY CAUSE OVERDOSES AND ILLNESSES")
    print("COCAINE IS VERY ADDICTIVE")
    print("COCAINE IS VERY DANGEROUS")
    print("COCAINE IS VERY BAD")
    print("DISPOSE OF COCAINE IMMEDIATELY")