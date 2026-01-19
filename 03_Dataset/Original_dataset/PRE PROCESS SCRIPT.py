#PRE PROCESS SCRIPT
'''
The scripts does two things:
1.Gets the files from the directory
2.Converts the current format of c xc yc w h TO c x1 y1 x2 y2 x3 y3 x4 y4 and overwrites the file 
'''


#Changing to the directory
import os
path=r'D:\OneDrive - Universidade de Lisboa\01_Disciplinas\5º ano\1º SEMESTRE\PMec\Project\Code\Subset\V_2\labels'
os.chdir(path)
print (os.getcwd()) #confirming the path

#prints the number of .txt files in the folder and removes the classes.txt folder
num_txt = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(f"Number of images : {num_txt}")

f=os.listdir(path)
f=f[1:] # Testing in a smallsubset (excluding the first folder (classes.txt))
print(f"Subset of images'{f}'")

#Reading and editing the files
for file in f:
    with open(os.path.join(path, file) , "r" ) as txt:
        #reading the file & splitting the lines
        file_content=txt.read()
        lines = [line for line in file_content.split('\n') if line.strip() != '']
        #separating each line in its elements
        new_lines=[]
        for line in lines:
             c=line[0]
             params=line[1:].split()
             #print(c)
             #print(params)
             #print(len(c))
             #Calculating the new parameters
             xc=float(params[0]) 
             yc=float(params[1])
             w=float(params[2])
             h=float(params[3])
             x1,y1 = max(0.0, min(1.0, xc - w/2)) , max(0.0, min(1.0, yc - h/2))
             x2,y2 = max(0.0, min(1.0, xc + w/2)) , max(0.0, min(1.0, yc - h/2)) 
             x3,y3 = max(0.0, min(1.0, xc + w/2)) , max(0.0, min(1.0, yc + h/2))
             x4,y4 = max(0.0, min(1.0, xc - w/2)) , max(0.0, min(1.0, yc + h/2))
             new_params=[x1,y1,x2,y2,x3,y3,x4,y4] 
             print(new_params)
             new_line=[]
             new_line.append(f"{c}")
             for param in new_params:
                new_line.append(f" {param:.6f}")
             text_line="".join(new_line)    
             new_lines.append(text_line)
             #print(new_lines)
        with open(os.path.join(path,file), "w") as wrt:
            wrt.write("\n".join(new_lines) + "\n")
print("Conversion completed!")
