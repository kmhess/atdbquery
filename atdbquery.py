# ATDBquery: query ATDB for survey status (ARTS or imaging)
# V.A. Moss 16/01/2019 (vmoss.astro@gmail.com)

__author__ = "V.A. Moss"
__date__ = "$16-jan-2019 17:00:00$"
__version__ = "0.1"

import os
import sys
from argparse import ArgumentParser, RawTextHelpFormatter
from modules.functions import *
import time

# Function version
def atdbquery(obs_mode):
	"""
    The main program to be run.
    :return:
    """

    # Time the total process length
	start = time.time()

	# Send the query
	obs_list = query_database(obs_mode)
	print('Total number of results returned for %s: %s' % (obs_mode.upper(),len(obs_list)))

	# End timing
	end = time.time()
	total = end-start
	print('Total time to run query: %.2f sec' % (total))

	return obs_list


# System call version
if __name__ == '__main__':

	# Parse the relevant arguments
	parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
	parser.add_argument('-m', '--mode',
			default='sc4',
			help='Specify whether mode is imaging/sc1/sc4 (default: %(default)s)')

	# Parse the arguments above
	args = parser.parse_args()

	# Send the query
	obs_list = atdbquery(args.mode)
	print(obs_list)