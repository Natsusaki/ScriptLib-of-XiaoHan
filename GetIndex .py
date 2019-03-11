################################################################################
#                 This script of geting edge atom index                        #
#                               XiaoHan                                        #
#                      xiaohan16@mails.ucas.ac.cn                              #
#                              2019.2.24                                       #
################################################################################
file1 = 'rcc.psf'
file2 = 'rcc.pdb'
first_num = 1
now_num = first_num
now_num2 = first_num
centerx = 28.340606689453125
centery = 49.08656311035156
centerz = 1.75

try:
    with open(file1) as f_obj:
        content1 = f_obj.read()
except FileNotFoundError:
    print("File don't exit")
else:
    psf = content1.split()

try:
    with open(file2) as f_obj:
        content1 = f_obj.read()
except FileNotFoundError:
    print("File don't exit")
else:
    pdb = content1.split()

pdb2 = []
pdbx = []
pdby = []
pdbz = []
pdb_name = []
atom_num = len(pdb)
i = 0
a = 1
while i <= (atom_num-1):
    if a == 1:
        pdb2.append(pdb[i])
        a= 2
    elif a == 2:
        pdb_name.append(pdb[i])
        a= 3
    elif a == 3:
        pdbx.append(pdb[i])
        a=4
    elif a == 4:
        pdby.append(pdb[i])
        a=5
    elif a==5:
        pdbz.append(pdb[i])
        a = 1
    i+=1
    
index = [first_num]
index2 = [(first_num-1)]
candidate = []
candidate2 = []
new_member = 0
psf_num = int(len(psf))
i = 0
yes = 0
active = 0
while True:
    while i <= (psf_num-1):
        if int(psf[i]) == now_num:
            if (i % 2) == 0:
                if pdb_name[int(psf[i+1])-1] == "C" or pdb_name[int(psf[i+1])-1] == "N":
                    yes = 0
                    for member in index:
                        if int(member) == int(psf[(i+1)]):
                            yes = 1
                    if yes == 0:
                            candidate.append(psf[(i+1)])
            else:
                if pdb_name[int(psf[i-1])-1] == "C" or pdb_name[int(psf[i-1])-1] == "N":
                    yes = 0
                    for member in index:
                        if int(member) == int(psf[(i-1)]):
                            yes = 1                 
                    if yes == 0:
                        candidate.append(psf[(i-1)])
        i +=1
    distance1 = 0.0
    distance2 = 0.0
    a = 0
    #print(candidate)
    if int(len(candidate)) == 0:
        break
    if now_num != first_num:
        for member in candidate:
            rx1 = float(pdbx[(int(now_num)-1)]) - float(pdbx[(int(now_num2)-1)])
            ry1 = float(pdby[(int(now_num)-1)]) - float(pdby[(int(now_num2)-1)])
            rx2 = float(pdbx[(int(member)-1)]) - float(pdbx[(int(now_num)-1)])
            ry2 = float(pdby[(int(member)-1)]) - float(pdby[(int(now_num)-1)])
            rr = rx1*ry2 - rx2*ry1
            if rr <= 0.0:
                candidate2.append(int(member))
    if len(candidate2) > 0:    
        for member in candidate2:
            distance2 = ((float(pdbx[(int(member)-1)]) - centerx)**2 + (float(pdby[(int(member)-1)]) - centery)**2 + (float(pdbz[(int(member)-1)]) - centerz)**2)**0.5
            if distance2 > distance1:
                distance1 = distance2
                a = member
    else:
        for member in candidate:
            distance2 = ((float(pdbx[(int(member)-1)]) - centerx)**2 + (float(pdby[(int(member)-1)]) - centery)**2 + (float(pdbz[(int(member)-1)]) - centerz)**2)**0.5
            if distance2 > distance1:
                distance1 = distance2
                a = member

        
    #print(a)
    index.append(int(a))
    index2.append(int(a)-1)
    #print(index2)
    #print(abandon)
    now_num2 = now_num
    now_num = int(a)
    candidate = []
    candidate2 = []
    i = 0
#print(len(index2))
print(index)
