import sys
import os

unpacker_path = sys.argv[1]
directory = sys.argv[2]
find_string = sys.argv[3]
replace_string = sys.argv[4]

os.chdir(directory)
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	decoded_filename = filename.replace(".s", ".")
	decoded_filepath = os.path.join(directory, decoded_filename)
	
	os.system("\"" + unpacker_path + "\" /d " + filename)
	os.remove(filename)
	
	with open(decoded_filepath, mode='rb') as file:
		data = file.read()
	data = data.replace(find_string.strip().encode("ascii"), replace_string.strip().encode("ascii"))
	with open(decoded_filepath, mode='wb') as file:
		file.write(data)

	os.system("\"" + unpacker_path + "\" /e " + decoded_filename)
	os.remove(decoded_filename)
	
	os.rename(filename, filename.replace(find_string, replace_string))