# print ntwork and next hop of stuff that has got metric equal to two, in the given output
print("Network"+"\t\t\t"+"Next Hop"+"\n")
flag=0
with open("network_output.txt") as fh:
    text=fh.read()
    lines=text.splitlines()

    for line in lines:
        if line:
            
            words_in_line=line.split()
            #print(words_in_line)
            if flag==1:
                if words_in_line[2]=="2":
                    print(words_in_line[0].replace("*>","")+"\t:\t"+words_in_line[1])

            if flag==2:
                if words_in_line[3]=="2":
                    print(words_in_line[1]+"\t:\t"+words_in_line[2])
                    
                
            if words_in_line[0]=="Network":
                flag=1
            if words_in_line[0]=="*>":
                flag=2
            
        
