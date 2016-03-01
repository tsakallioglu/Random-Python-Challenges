'''
Take the plaintext version of your resume (or linkedin profile) and 
create a bar chart of character frequency. (Bonus: programmatically 
strip out punctuation and whitespace.)
'''

import collections
import re
import matplotlib.pyplot as plt

#Read the plain text Resume document and count the values
#of every character using "Counter" function and store the results
#in a dictionary called "letters"
f = open('C:\Users\Tuna\Desktop\Mehmet_Tuna_Sakallioglu_Resume.txt')
resume = f.read()
letters = collections.Counter(resume)

#Remove the special characters from the dictionary
for i in letters.keys():
    if not re.match('[a-zA-Z0-9_]',i):
        del letters[i]

#Plot the bar chart and save it to the working directory
D = {u'Label1':26, u'Label2': 17, u'Label3':30}
plt.figure()
plt.bar(range(len(letters)), letters.values(),width = 0.5,align='center')
plt.xticks(range(len(letters)), sorted(letters.keys()),size=5)
plt.grid(True)
plt.xlim(-0.5,60.5)
plt.savefig('bar.jpg',dpi=1500)