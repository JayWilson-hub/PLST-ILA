import os

folder = " "

files = [f for f in os.listdir(folder) if f.endswith(".tif")]
files.sort()

start_num = 1

for idx, filename in enumerate(files, start=start_num):
    old_path = os.path.join(folder, filename)
    temp_path = os.path.join(folder, f"temp_{idx:03d}.tif")
    os.rename(old_path, temp_path)

temp_files = [f for f in os.listdir(folder) if f.startswith("temp_")]
temp_files.sort()

for temp_file in temp_files:
    number = int(temp_file.split("_")[1].split(".")[0])
    new_path = os.path.join(folder, f"{number:03d}.tif")
    print(temp_path)
    print(new_path)
    os.rename(os.path.join(folder, temp_file), new_path)

