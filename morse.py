import json
import os
from time import sleep


def get_config():
	with open('config.json', 'r') as config_file:
		config = json.loads(config_file.read())
	return config


def to_morse(text):
	text = text.lower()
	ret = ""
	config = get_config()
	for ch in text:
		if ch == ' ':
			ret += config['word_gap']
		else:
			ret += config['dictionary'][ch]
			ret += config['letter_gap']
	return ret


def play(morse_text):
	config = get_config()
	durations = []
	for morse_element in morse_text:
		if morse_element == config['letter_gap']:
			durations.append((config['audio']['letter_gap'], 'off'))
		elif morse_element == config['word_gap']:
			durations.append((config['audio']['word_gap'], 'off'))
		elif morse_element == '.':
			durations.append((config['audio']['.'], 'on'))
			durations.append((config['audio']['inter_letter_gap'], 'off'))
		elif morse_element == '-':
			durations.append((config['audio']['-'], 'on'))
			durations.append((config['audio']['inter_letter_gap'], 'off'))

	play_command = "play -n synth {0} sine 750 2> /dev/null"
	unit_duration = config['audio']['unit']
	for duration in durations:
		duration, on = duration
		duration *= unit_duration
		if on == 'on':
			os.system(play_command.format(duration))
		else:
			sleep(duration)


print(to_morse("hello world"))
play(to_morse('hello world'))