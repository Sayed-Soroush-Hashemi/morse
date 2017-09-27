import json


def get_config():
	with open('config.json', 'r') as config_file:
		config = json.loads(config_file.read())
	return config


def to_morse(text):
	ret = ""
	config = get_config()
	for ch in text:
		ret += config['dictionary'][ch]
		if ch != ' ':
			ret += config['letter_gap']
	return ret


print(to_morse("hello world"))
