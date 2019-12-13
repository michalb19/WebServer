import os
import string

SERVER_DIRECTORY = r'C:\Temp\Files'
JSON_DB_FILE = os.path.join(SERVER_DIRECTORY, 'db.json')
ACCESS_LOG = os.path.join(SERVER_DIRECTORY, 'access.log')
CODE_CHARACTERS_POOL = string.digits