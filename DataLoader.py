"""
Module handling the loading of data frm the json.
"""
import json


class DataLoader:
    """
    Singleton for loading data, recreating the object containing the file data multiple times
    is pointless in our code, since the data won't change during the run time of the script.
    """
    _instance = None
    _device_data = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def load_device_data(self, filename):
        if self._device_data is None:
            with open(filename, 'r') as file:
                self._device_data = json.load(file)
        return self._device_data
