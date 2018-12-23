import numpy as np
import time
import warnings

warnings.filterwarnings("ignore")

hat = ['sam', 'gary', 'tibbsy', 'neil', 'stu', 'drew']
hat2 = ['gary', 'tibbsy', 'iain']

choose = np.random.randint(len(hat), size = 1000000)
x, y = np.histogram(choose, bins=len(hat))
a = np.argmax(x)
print('The book is to be choosen by:')
time.sleep(1)
print(hat[a])

if hat[a] in hat2:
    hat2.remove(hat[a])

choose2 = np.random.randint(len(hat2), size = 1000000)
x2, y2 = np.histogram(choose2, bins=len(hat2))
a2 = np.argmax(x2)
print('The film is to be choosen by:')
time.sleep(1)
print(hat2[a2])
