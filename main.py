from deluge_client import DelugeRPCClient
from qbittorrent import Client
import json
import requests
import time
import pathlib
import os


def grabMagnet(url):
	response = requests.get(url)
	page = response.text

	lines = page.split("\n")
	for line in lines:
		if "magnet" in line:
			start = line.find("magnet")
			end = line.find('>')
			magnet = line[start:end - 1]
			print(magnet)
			return magnet
	return None


def unfuckifyA(code, prefix, spaced):
	snum = ''
	if spaced:
		snum += '"+'
	if code < 10 and prefix:
		snum += '0'
	snum += str(code)
	if spaced:
		snum += '"'
		if code >= 10:
			for i in range(0, 10):
				snum += '-"' + str(code) + str(i) + '"'
	return snum


def dumpNomicon(nomi):
	try:
		with open("data.json", mode="w") as file:
			json.dump(nomi, file, indent=4)
	except KeyboardInterrupt:  # ctrl-c protection while writing
		print("Please don't kill me while i'm writing")
		with open("data.json", mode="w") as file:
			json.dump(nomi, file, indent=4)
		exit(0)


def loadNomicon():
	with open("data.json", mode="r") as file:
		raw = json.load(file)
		return raw


def addMagnet(client, magnet):
	if isinstance(client, Client):
		client.download_from_link(magnet)
	if isinstance(client, DelugeRPCClient):
		try:
			client.core.add_torrent_magnet(magnet, None)
		except:
			pass


def loopNomicon(client, nomicon):
	to_remove = []
	for key in nomicon:
		nomi = nomicon[key]
		snum = ""
		if nomi["episode"] != -1:
			snum = unfuckifyA(nomi["episode"], nomi["prefix_0_before_10"], nomi["space_episode_number"])
		keys = str(key).replace(" ", "+")
		search = keys + "+" + nomi["group"] + "+" + str(nomi["resolution"]) + snum
		if nomi["except"] != "":
			search += "+-" + nomi["except"]
		type_string = "0_0"
		if nomi["english_translated"]:
			type_string = "1_2"
		url = 'https://nyaa.si/?f=0&c=' + type_string + '&q=' + search
		magnet = grabMagnet(url)
		if magnet is not None:
			addMagnet(client, magnet)
			print("'" + key + "' episode " + str(nomi["episode"]) + " found")
			if nomi["episode"] >= 0:
				nomi["episode"] = nomi["episode"] + 1
			else:
				to_remove += [key]
			if nomi["episode"] > nomi["max_episode"]:
				to_remove += [key]
		else:
			print("'" + key + "' episode " + str(nomi["episode"]) + " not found")
	for key in to_remove:
		nomicon.pop(key)


if __name__ == "__main__":
	client = None

	with open("config.json", mode="r") as file:
		config = json.load(file)
		try:
			client = Client("http://" + config["qbit"]["qbit_ip"] + ":" + config["qbit"]["qbit_port"] + "/")
			client.login(config["qbit"]["qbit_user"], config["qbit"]["qbit_pass"])
		except:
			try:
				print("QB not found, trying deluge")
				if config["deluge"]["deluge_pass"] == "":
					with open(os.getenv('APPDATA') + r'\deluge\auth', mode="r") as file:
						auth = file.read()
						password = auth.split(":")[1]
						with open("config.json", mode="w") as file2:
							config["deluge"]["deluge_pass"] = password
							json.dump(config, file2, indent=4)
				client = DelugeRPCClient(config["deluge"]["deluge_ip"], config["deluge"]["deluge_port"],
										 config["deluge"]["deluge_user"], config["deluge"]["deluge_pass"])
				client.connect()
				print("Connected to Deluge")
			except ConnectionRefusedError:
				print("Deluge not found")
				exit(0)

	while True:
		nomicon = loadNomicon()
		loopNomicon(client, nomicon)
		dumpNomicon(nomicon)
		time.sleep(1500)
