from rplidar import RPLidar
import msvcrt
import time
import math

lidar = RPLidar("\\\\.\\com4")
time.sleep(1)

#try:
info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)


for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurements' % (i,len(scan)))
    ar = [0]*6
    wFlag = False
    for j in scan:
        k = math.floor(j[1]/60)
        if (j[2]<1000):
            #print("Warning: object at %f degrees is too close" % (j[1]))
            ar[k]+= -math.inf
            wFlag =True
        else:
            ar[k]+=j[2]
        if(math.floor(j[1])%60 == 0):
            k+=1

    if(wFlag):
        print(ar)
        print("Object(s) are too close...")
        fre = max(ar)
        if(fre<1000):
            print("There is nowhere safe to venture, immediate landing to avoid damage...")
            break
        evac = (ar.index(fre)+1)*60 - 30
        print("Evacuate in the direction of %d degrees" % (evac))

    if(msvcrt.kbhit() and msvcrt.getch() == chr(27).encode()):
        break

# except:
#     print("You messed up somewhere")
#     lidar.stop()
#     lidar.stop_motor()
#     lidar.disconnect()
#     exit()


lidar.stop()
lidar.stop_motor()
lidar.disconnect()
