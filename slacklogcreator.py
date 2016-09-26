#slack log creator

# -*- coding: utf-8 -*-

import urllib
import re
import json

def convert_to_python(page):
	json_decoder = json.JSONDecoder()
	json_dict = json_decoder.decode(page.read())
	return json_dict


def get_page(latest):
	global base_url
	current_url = base_url + "&latest=" + latest
	return urllib.urlopen(current_url)


def get_all_pages(start, filename):
	current_timestamp = start
	current_page = convert_to_python(get_page(current_timestamp))

	page_counter = 0 #for funsies

	while current_page['messages'] != []:
		print(page_counter)
		page_counter += 1
		with open(filename, 'a') as file:
			for line in current_page['messages']:
				text = remove_links(line['text'])
				file.write(text.encode('utf-8') + '\n')
		current_timestamp = current_page['messages'][-1]['ts']
		current_page = convert_to_python(get_page(current_timestamp))
	print('done')


def remove_links(text):
	return re.sub('<.*>', '', text)


base_url = '{insert base url here}'

get_all_pages('0', 'thisisawesome.txt')
