import subprocess
import glob

__glob = [

    "*.txt",
    "*.py",
    "*.csv"
]


for _glob in __glob:
    for file in glob.glob(_glob):
        print(file)
        #proc = subprocess.run(f'carbon-now {file}', shell=True)
        #print(proc.stdout)

#19_linear_search_plus.py is very large lmao

__lines = [
    (1, 21),
    (22, 30),
    (31, 67),
    (67, 135),
    (135, 151)
]

for line in __lines:
    subprocess.run(f"carbon-now 19_linear_search_plus.py -s {line[0]} -e {line[1]} -t 19_linear_search_plus.py-{line[0]}-{line[1]}.png", shell=True)
    
    