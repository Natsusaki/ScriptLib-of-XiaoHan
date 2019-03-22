file = "a"

try:
    with open(file) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    print("File don't exit")
else:
    atomlist = content.split()

N = len(atomlist)
i = 0
while i <= (N-1):
    swap = int(atomlist[i]) + 1
    atomlist[i] = swap
    i +=1

fo = open("atomselect","w")

for i in atomlist:
    fo.write(str(i))
    fo.write(" ")

fo.close()


