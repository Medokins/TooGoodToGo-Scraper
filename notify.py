import requests
import json

def pushbullet_notify(title, body):
	TOKEN = "Access Token" # Pass your Access Token here
	msg = {"type": "note", "title": title, "body": body}
	resp = requests.post('https://api.pushbullet.com/v2/pushes',
						data=json.dumps(msg),
						headers={"Authorization": "Bearer " + TOKEN,
								"Content-Type": "application/json"})
	if resp.status_code != 200:
		raise Exception("Error", resp.status_code)
	else:
		print("Message sent")
