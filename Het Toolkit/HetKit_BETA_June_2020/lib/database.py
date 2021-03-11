import os
import numpy as np
import json

def create_database():

	DB = {}
	return DB

def load_database():

	dict_file = "HetKit_Database.json"
	with open(dict_file, 'r') as in_file:
		DB = json.load(in_file)

	return DB

def save_database(DB):
		
	dict_file = "HetKit_Database.json"
	with open(dict_file, 'w') as out_file:
		json.dump(DB, out_file)

def create_entry(ID, DB):

	DB[str(ID)] = {}
	return DB

def search_entry(self, ID, DB):

	if DB[str(ID)] == True:
		return True
	else:
		return False


