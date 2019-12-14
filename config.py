import os
import string

# SERVER_DIRECTORY = r'C:\Temp\Files'
SERVER_DIRECTORY = '/home/michal/file_server'

# json file format:
# {'<code>': ('<server_path>', '<original_filename>', <download_counter>)}
JSON_DB_FILE = os.path.join(SERVER_DIRECTORY, 'db.json')

ACCESS_LOG = os.path.join(SERVER_DIRECTORY, 'access.log')
CODE_CHARACTERS_POOL = string.digits
