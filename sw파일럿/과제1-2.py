with open("C:/Users/User/Desktop/timestamp,event,message.txt", mode='r') as f:
    lines = f.readlines()
di = {}
for i in range(35,0,-1):
    li = lines[i].split(',')
    di[li[0]] = li[2]


fi = open('C:/Users/User/swpilot/sw파일럿/mission_computer_main.json', mode = 'w')
fi.write(str(di))


f.close()




