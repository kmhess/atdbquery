# ATDBquery: modules to query ATDB for survey status (ARTS or imaging)
# V.A. Moss 16/01/2019 (vmoss.astro@gmail.com)

__author__ = "V.A. Moss"
__date__ = "$16-jan-2019 17:00:00$"
__version__ = "0.1"

import os
import sys
import requests
import json

###################################################################
# Query the ATDB database

def query_database(obs_mode):

	# Define the URL for quert
	url = 'http://atdb.astron.nl/atdb/observations/?my_status__in=completed,completing,archived,removed,on%%20hold&observing_mode__icontains=%s' % obs_mode

	# First, determine how many results there are
	# Do the query
	try: 
		response = requests.get(url)
	except Exception as e:
		print(e)
		sys.exit()	

	# Can only do 100 per page
	result_num = json.loads(response.text)['count']
	print('Total number of results found in ATDB for %s: %s' % (obs_mode.upper(),result_num))
	pagenum = result_num // 100 + 1

	# Define the observation dictionary
	# Get only the field_name,field_ra,field_dec,status
	obs_list = []

	for page in range(1,pagenum+1):

		url = 'http://atdb.astron.nl/atdb/observations/?my_status__in=completed,completing,archived,removed,on%%20hold&observing_mode__icontains=%s&page=%s' % (obs_mode,page)

		# Do the query
		try: 
			response = requests.get(url)
		except Exception as e:
			print(e)
			sys.exit()

		# Parse the data
		metadata = json.loads(response.text)['results']

		# Return all information
		for i in range(0,len(metadata)):
			obs_list.append(metadata[i])

		# # Loop
		# for i in range(0,len(metadata)):
		# 	obs = metadata[i]
		# 	name = obs['field_name']
		# 	tid = obs['taskID']
		# 	ra = obs['field_ra']
		# 	dec = obs['field_dec']
		# 	status = obs['my_status']

		# 	obs_dict[tid] = {'field_name':name, 'field_ra':ra, 'field_dec':dec, 'status':status}

	return obs_list