import os
from datetime import datetime

print('=========== output ==============')

# print(os.getcwd())
# os.chdir('/var/www/maen/Python/os_lib')
# print(os.getcwd())

# os.rmdir('deletethisdir')
# os.removedirs('testdir/test2')


# os.mkdir('deletethisdir')
# os.makedirs('testdir/test2')
# print(os.listdir())

# time = os.stat('README.md').st_atime
# print(datetime.fromtimestamp(time))


# print(os.getcwd())
# for dirpath, dirname , filename in os.walk('/var/www/maen/Python'):
#     print(dirpath)
#     print(dirname)
#     print(filename)
#     print()

home_path = os.environ.get('HOME')
file_path = 'test_python_DELETE.txt'

full_path = os.path.join(home_path,file_path)

with open(full_path,'w') as f:
    f.write('')


# ================================

print(os.path.exists('maen/maen.txt'))
print(os.path.isfile('maen/maen.txt'))
    
