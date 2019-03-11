################################################################################
#            This script of writing fixed atom pdb file                        #
#                               XiaoHan                                        #
#                      xiaohan16@mails.ucas.ac.cn                              #
#                              2019.2.25                                       #
################################################################################
file = 'rc.pdb'
file2 = 'out.pdb'
fix = [1, 9, 3, 27, 46, 13, 17, 16, 14, 47, 28, 4, 12, 6, 8, 2, 26, 45, 20, 23, 77, 73, 101, 80, 53, 61, 55, 82, 103, 65, 69, 68, 66, 104, 83, 56, 64, 58, 60, 54, 81, 102, 72, 76, 122, 119, 132, 124, 112, 116, 113, 117, 114, 126, 133, 118, 121, 286, 283, 315, 295, 268, 270, 264, 272, 266, 293, 313, 276, 280, 277, 275, 312, 292, 265, 273, 267, 294, 314, 281, 285, 427, 426, 454, 436, 412, 414, 408, 416, 410, 434, 453, 420, 424, 421, 419, 452, 433, 409, 417, 411, 413, 407, 431, 451, 425, 430, 374, 366, 397, 376, 349, 357, 351, 378, 399, 361, 365, 362, 360, 398, 377, 350, 358, 352, 354, 348, 375, 396, 367, 373, 333, 328, 342, 334, 322, 326, 323, 327, 324, 336, 343, 329, 332, 159, 156, 189, 169, 142, 144, 138, 146, 140, 167, 187, 150, 154, 153, 151, 188, 168, 141, 149, 143, 170, 190, 158, 163, 21, 19, 48, 29, 5, 7]

try:
    with open(file) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    print("File don't exit")
else:
    pdb = content.split()


Atom = []
Num = []
AtomName = []
resname = []
resid = []
x = []
y = []
z = []
o = []
b = []
segid = []
i = 0
a = 1
number = len(pdb)/11
while i <= number*11-1:
    if a == 1:
        Atom.append(pdb[i])
        a= 2
    elif a == 2:
        Num.append(pdb[i])
        a= 3
    elif a == 3:
        AtomName.append(pdb[i])
        a=4
    elif a == 4:
        resname.append(pdb[i])
        a=5
    elif a==5:
        resid.append(pdb[i])
        a = 6
    elif a==6:
        x.append(pdb[i])
        a = 7
    elif a==7:
        y.append(pdb[i])
        a = 8
    elif a==8:
        z.append(pdb[i])
        a = 9
    elif a==9:
        o.append(pdb[i])
        a = 10
    elif a==10:
        b.append(pdb[i])
        a = 11
    elif a==11:
        segid.append(pdb[i])
        a = 1
    i+=1
print(len(Num))
i=0    
while i <= (number-1):
    for member in fix:
        if int(Num[i]) == member:
            o[i] = "1.00"
    i +=1
fixed = open(file2,'w')
i=0
while i <= (number-1):
    fixed.write(str(o[i])+"\n")
    i+=1
fixed.close()

print('finished')
