import subprocess
import time

start = time.time()

list_of_dirs = []

for dir in list_of_dirs:
    print("Treating : {}".format(dir))
    try:
        subprocess.run(["python", "path/to/combine_mask.py", "-i", dir])
    except e as Exception:
        print(e)
    
end = time.time()
print("Execution time : {} seconds.".format(end-start))

