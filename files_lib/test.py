from pathlib import Path

# ROOT_DIR = Path(__file__).parent
# psub_file = ROOT_DIR / 'test.txt'


# with open("files_lib/test.txt") as f:
#     content = f.read()
#     content2 = f.readlines()
#     content3 = f.readline()
#     content4 = f.readline()
#     content5 = f.read(3)

    # size_to_read = 3
    # content = f.read(size_to_read)
    # while len(content) > 0:
    #     print(content,end='=')
    #     content = f.read(size_to_read)


# print(content3,end='')
# print(content4,end='')
# print(content5)


# ==============================
# seek example
# ==============================
# file = open(psub_file)

# content = file.read(5)
# print(content,end='')

# file.seek(0)

# content = file.read(5)
# print(content,end='')

# file.close()

# ==============================
# write example
# ==============================

with open('files_lib/text1.txt','w') as f:
     f.write("heloooooooooooooo\n")     
     f.write("world")


with open('files_lib/text1.txt','r') as rf:
    with open('files_lib/text1_copy.txt','w') as wf:
         for line in rf:
              wf.write(line)



# with open('files_lib/cat.jpg','rb') as rf:
#     with open('files_lib/cat2.jpg','wb') as wf:
#          for line in rf:
#               wf.write(line)

with open('files_lib/cat.jpg','rb') as rf:
    with open('files_lib/cat3.jpg','wb') as wf:
        chunk_size =4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
