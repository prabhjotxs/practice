s_score = input("Enter score (must between 0.0 to 1.0): ")

try:
    i_score = float(s_score)
    if i_score < 0.0 or i_score >1.0:
        quit()
except:
    print("Check score! must be a value between 0.0 to 1.0")
    quit()

if i_score >= 0.9:
    print ('A')
elif i_score >= 0.8:
    print('B')
elif i_score >= 0.7:
    print('C')
elif i_score >= 0.6:
    print('D')
else:
    print('F')
