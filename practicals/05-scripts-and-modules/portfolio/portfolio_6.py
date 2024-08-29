if __name__ == "__main__":
	import shutil
	import sys

	if len(sys.argv) < 2:
    		print(f"usage: python {sys.argv[0]} <file to backup>")

	file_to_backup = sys.argv[1]
	backed_up_file = file_to_backup.replace('.txt', '-backedup.txt')

	print("copying filename:", file_to_backup)
	shutil.copy(file_to_backup, backed_up_file)

	print("file has been backed up....")