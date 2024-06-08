import subprocess

subprocess.run('clear')

# with open('subprocess_lib/output.txt','w') as f:
#     file = subprocess.run(['ls','-la'],stdout=f,text=True)
    

output = subprocess.run(['ls','-la'],capture_output = True,text=True)
print(output.stdout)