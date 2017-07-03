miles_run = 0
running = True

while running:
    if miles_run <= 10:
        print("Still running! On mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False

print("Whew! I'm tired")
