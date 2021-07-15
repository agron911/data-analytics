import file as f1

my_f = f1.File('ag')
print(my_f.get_info())


f = open('new_file.txt','w')
f.write("some text...")
f.close()

with open('new_file2.txt','w') as f:
    f.writelines(["嗨some text for f2 \n"," 2nd lines\n"])

fr = open('new_file.txt','r')
print(fr.read())
fr.close()

with open('new_file2.txt','r') as fr2:
    print('read:\n ', fr2.read())
    # print('\nreadlines:\n ', fr2.readline())
with open('new_file2.txt','r') as fr2:
    while True:
        line = fr2.readline()
        print(line)
        if not line:
            break


print("="*80)
with open('new_file2.txt','r+') as fr2:
    fr2.write('text has been replace')
    fr2.seek(0)
    print(fr2.read())
print("="*80)

with open('new_file2.txt','a+') as fr2:
    fr2.write("\n add new line")
    fr2.seek(0)
    print(fr2.read())


