import easyocr
import os
import pandas as pd

reader = easyocr.Reader(['en'])
# direct = 'plates'
Files = os.listdir('plates')

lst = []  #list to be updated in loop
# for showing images from plates folder :
for file in Files:
    imgPath = os.path.join('plates', file)
    result = reader.readtext(imgPath)
    text = result[0][1]
    lst.append(text)

df = pd.DataFrame(lst, columns=['Numbers'])
df.to_csv('Numbers.csv',index = False)
# df.toexcel('Numbers.xls', index = False)   #For exporting to excel
