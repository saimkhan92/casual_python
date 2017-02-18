# convert abcabcabcc into a3b3c4

text="abcabcabcc"
dic={}
final_text=[]

for i in text:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)

for k,v in dic.items():
    final_text.append(str(k))
    final_text.append(str(v))
print("".join(final_text))
    
