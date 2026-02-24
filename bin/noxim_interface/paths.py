import os

this_dir = os.path.dirname(__file__)

PROJECT_DIR = os.path.abspath(os.path.join(this_dir, '..')) + '/'

NOXIM_OUTPUT = PROJECT_DIR + 'outputs/'
TRAFFIC_TABLES = PROJECT_DIR + 'traffic_tables/'