

for Girl in Girls:
    Girl.GetDrink += 1
    while not Girl.IsDrunk():
        try:
            Boy.SleepWith(Girl)
            break
        except NoSexError:
            if Girl.IsDrunk():
                break
            Girl.GetDrink += 1