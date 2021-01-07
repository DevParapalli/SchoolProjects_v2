import subprocess
import glob

for file in glob.glob('*.py'):
    proc = subprocess.run(f'carbon-now {file}', shell=True)
    print(proc.stdout)
