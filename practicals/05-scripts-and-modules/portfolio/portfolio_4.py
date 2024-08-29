if __name__ == "__main__":
	import sys
	import requests

	if len(sys.argv) < 2:
		print("Please enter a website")
		exit()
	
	url = str(sys.argv[1])
	resp = requests.get(url).status_code
	
	if resp == 200:
		print("Connected successfully")
		print(f"Http status code is {resp}.")

	else:
		print("Connection failed")
		print(f"Http status code is {resp}.")