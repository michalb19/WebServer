import json
import logging
import os
import random

import config

class FileServer(object):
    def __init__(self):
        self._files_dict = self._load_json_file()
        self._initialize_logger()

    def _initialize_logger(self):
        logging.basicConfig(filename=config.ACCESS_LOG, level=logging.DEBUG)

    def _generate_code(self):
        code = ''.join([random.choice(config.CODE_CHARACTERS_POOL) for i in range(config.CODE_LENGTH)])
        # Make sure we won't have a collision
        while code in self._files_dict.keys():
            code = ''.join([random.choice(config.CODE_CHARACTERS_POOL) for i in range(config.CODE_LENGTH)])
        return code

    def get_download_filepath(self, code):
        file_data = self._get_file_from_code(code)
        # Update the download counter
        self._files_dict[code] = (file_data[config.SERVER_PATH_INDEX], 
            file_data[config.ORIGINAL_FILENAME_INDEX], 
            file_data[config.DOWNLOAD_COUNTER_INDEX] + 1)
        self._update_json_file()
        logging.info('File %s was downloaded %d times', code, self._files_dict[code][config.DOWNLOAD_COUNTER_INDEX])
        return file_data

    def get_upload_filepath(self, code, filename):
        return os.path.join(config.SERVER_DIRECTORY, '%s_%s' % (code, filename))

    def save_upload_file(self, uploaded_file):
        if uploaded_file.filename != '':
            code = self._generate_code()
            server_path = self.get_upload_filepath(code, uploaded_file.filename)
            uploaded_file.save(server_path)
            self._save_file_in_json(code, server_path, uploaded_file.filename)
            logging.info('File %s was uploaded', code)
            return code
        return ''

    def get_file_status(self, code):
        return self._get_file_from_code(code)[config.DOWNLOAD_COUNTER_INDEX]

    def _load_json_file(self):
        if not os.path.exists(config.JSON_DB_FILE):
            return {}
        with open(config.JSON_DB_FILE, 'r') as json_file:
            return json.load(json_file)

    def _update_json_file(self):
        with open(config.JSON_DB_FILE, 'w') as json_file:
            json.dump(self._files_dict, json_file)

    def _save_file_in_json(self, code, server_path, filename):
        # Download counter is intialized with 0
        self._files_dict[code] = (server_path, filename, 0)
        self._update_json_file()

    def _get_file_from_code(self, code):
        if code in self._files_dict:
            return self._files_dict[code]
        return None
