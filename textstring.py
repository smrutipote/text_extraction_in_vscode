import pytesseract
import re
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text1=pytesseract.image_to_string('pan2.jpeg')
#print(text1)
def imgstr(text1):
    text=re.sub('\n+','\n',text1)
    print(text)
    dob=re.search('[0-9]{2}/[0-9]{2}/[0-9]{4}',text)
    pan_num=re.search('[A-Z]{5}[0-9]{4}[A-Z]',text)

    list_text=text.split('\n')
    for i,line in enumerate(list_text):
        if re.search('DEPARTMENT',line):
            name=list_text[i+1]
            
    data={'Name':[name],
        'DOB':[dob.group()],
        'PAN':[pan_num.group()]}
    return data

result=imgstr(text1)
print(result)