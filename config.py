import os
import string

# Root folder for server files uploads
SERVER_DIRECTORY = '/home/michal/file_server'
ACCESS_LOG = os.path.join(SERVER_DIRECTORY, 'access.log')

# This would have been better saved in some sort of DB, but due to my poor resources,
# I chose to save the info in a json file in the following format:
# {'<code>': ('<server_path>', '<original_filename>', <download_counter>), ...}
JSON_DB_FILE = os.path.join(SERVER_DIRECTORY, 'db.json')
SERVER_PATH_INDEX = 0
ORIGINAL_FILENAME_INDEX = 1
DOWNLOAD_COUNTER_INDEX = 2

CODE_CHARACTERS_POOL = string.digits
CODE_LENGTH = 6
