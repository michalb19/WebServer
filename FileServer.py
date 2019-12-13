import json
import os
import random

import config

# TODO: Add logging to access.log about every upload and download
class FileServer(object):
    def __init__(self):
        self._files_dict = self._load_json_file()

    def _generate_code(self):
        code = ''.join([random.choice(config.CODE_CHARACTERS_POOL) for i in range(6)])
        # Make sure we won't have a collision
        while code in self._files_dict.keys():
            code = ''.join([random.choice(config.CODE_CHARACTERS_POOL) for i in range(6)])

        return code

    def get_download_filepath(self, code):
        return self._get_file_from_code(code)

    def get_upload_filepath(self, filename):
        # TODO: Save with different filename, so that we could upload different files of the same name
        return os.path.join(config.SERVER_DIRECTORY, filename)

    def save_upload_file(self, uploaded_file):
        if uploaded_file.filename != '':
            code = self._generate_code()
            server_path = self.get_upload_filepath(uploaded_file.filename)
            uploaded_file.save(server_path)
            self._save_file_in_json(code, server_path)
            return code
        return ''

    def _load_json_file(self):
        if not os.path.exists(config.JSON_DB_FILE):
            return {}
        with open(config.JSON_DB_FILE, 'r') as json_file:
            return json.load(json_file)

    def _save_file_in_json(self, code, filename):
        # TODO: Save a counter of downloads to indicate if file was downloaded and show in status
        self._files_dict[code] = filename
        with open(config.JSON_DB_FILE, 'w') as json_file:
            json.dump(self._files_dict, json_file)

    def _get_file_from_code(self, code):
        if code in self._files_dict:
            return self._files_dict[code]
        return ''
