if __name__ == "__main__":	
	import sys
	def arguments(*arg):
		if len(sys.argv) > 1:
			print(sys.argv[1:])
		else:
			print("no arguments were passed.")

arguments()