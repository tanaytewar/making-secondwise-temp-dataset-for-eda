from datetime import datetime, timedelta
import random

def datafunc():
    now = datetime(2020, 10, 12, 0, 0, 0)
    last = datetime(2020, 10, 13, 0, 0, 0)
    delta = timedelta(seconds=60)
    times = []
    count = 0
    def randc():
        random_number = random.randint(20,41)
        return random_number
    def ctof():
        farh = (randc() * 9/5) + 32
        return farh
    def vibr():
        vibs=random.randint(20,50)
        return vibs

    while now < last:
        times.append(now.strftime('%H:%M:%S'))
        now += delta
        count+=1
        print(count," ",now," ", randc()," ", ctof()," ", vibr())
    print(count)
#x=datafunc()
print("data for A:",datafunc())
print("data for B:",datafunc())


#filter(datafunc(), datetime(2020,10,12,23,55,00))

