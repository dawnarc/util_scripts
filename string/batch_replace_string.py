
#batch replace string in a directory recursively

import os
import glob
import io

dir = 'D:/test'

dic = { "src": "dest", "aaa": "bbb"}
        
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
        
for file in glob.iglob(dir + '/**/*.txt', recursive=True):
    print(file)
    new_text = ''
    with io.open(file,'r',encoding='utf8') as f:
        text = f.read()
    
        new_text = replace_all(text, dic);
        
    with io.open(file,'w',encoding='utf8') as f:
        f.write(new_text)