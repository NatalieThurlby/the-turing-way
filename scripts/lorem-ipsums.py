#!/usr/bin/env python3
import os
import re
import sys

directory_to_check = '../book/content/'

def remove_comments(text_string):
	p = re.sub('(?s)<!--(.*?)-->','', text_string)
	return p

failed = []
for root_dir, _, file_names in os.walk(directory_to_check):
	for file_name in file_names:
		file = open(os.path.join(root_dir,file_name))
		text = file.read()
		text = remove_comments(text)
		print(file.name)
		if 'lorem ipsum' in text.lower():
			failed.append(file.name)

if len(failed)!=0:
	error_message = '"Lorem ipsum"s found in the following files:\n' + '\n'.join(failed)
	raise Exception(error_message)
