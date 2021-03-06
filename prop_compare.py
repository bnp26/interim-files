#!/usr/bin/env python

import json
import pandas as pd

def load_json(file_path):
	# open JSON file and parse contents
	fh = open(file_path,'r')
	data = json.load(fh)
	fh.close()

	return data

def compare_json_data(source_data_a,source_data_b):

	def compare(data_a,data_b):
		# type: list
		if (type(data_a) is list):
			# is [data_b] a list and of same length as [data_a]?
			if (
				(type(data_b) != list) or
				(len(data_a) != len(data_b))
		):
				return False

			# iterate over list items
			for list_index,list_item in enumerate(data_a):
				# compare [data_a] list item against [data_b] at index
				if (not compare(list_item,data_b[list_index])):
					return False

			# list identical
			return True

		# type: dictionary
		if (type(data_a) is dict):
			# is [data_b] a dictionary?
			if (type(data_b) != dict):
				return False

			# iterate over dictionary keys
			for dict_key,dict_value in data_a.items():
				# key exists in [data_b] dictionary, and same value?
				if (
					(dict_key not in data_b) or
					(not compare(dict_value,data_b[dict_key]))
				):
					return False

			# dictionary identical
			return True

		# simple value - compare both value and type for equality
		return (
			(data_a == data_b) and
			(type(data_a) is type(data_b))
		)

	# compare a to b, then b to a
	return (
		compare(source_data_a,source_data_b) and
		compare(source_data_b,source_data_a)
	)

def main():
	# import testing JSON files to Python structures
	a_json = load_json('menu.json')
	b_json = load_json('edited_menu.json')
        
        print a_json
        
        a_df = pd.read_json('menu.json')
        b_df = pd.read_json('edited_menu.json')

        print a_df.columns
        print b_df.columns
        a_schema = pd.io.json.build_table_schema(a_df)
        b_schema = pd.io.json.build_table_schema(b_df)

        print a_schema['fields']
        print b_schema['fields']

	# compare first struct against second
	print('Compare JSON result is: {0}'.format(
		compare_json_data(a_json,b_json)
	))


if (__name__ == '__main__'):
	main()
