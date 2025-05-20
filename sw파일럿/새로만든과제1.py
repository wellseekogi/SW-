f = open("C:/Users/User/Desktop/2023-08-27 113500,INFO,Oxygen tank.txt", mode = 'r')
data = f.read()
print(data)
f.close()

fi = open('C:/Users/User/swpilot/sw파일럿/log_analysis.md', mode = 'w')
fi.write(data)

fi.close()

