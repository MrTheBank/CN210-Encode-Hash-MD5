# Import necessary libraries.
import timeit
import hashlib

# Define start time.
start = timeit.default_timer()

md5_list = []

# Opening '5000words.txt' file.
with open("5000words.txt", "r") as f:
    lines = f.read().split()
    for word in lines:
        md5 = hashlib.md5(word.encode()).hexdigest()
        md5_list.append(md5)

# Writing 5,000 MD5 words to file.
md5_file = open("5000md5.txt", "w")
for word in md5_list:
    md5_file.write(word + "\n")
md5_file.close()

# Define stop time.
stop = timeit.default_timer()

# Calculate run time and output as milliseconds
run_time = (stop-start)*1000

# Print results and runtime.
print(f"Hashing {len(md5_list)} words into MD5 and save file to '5000md5.txt'")
print("Run Time:", run_time ," ms")
