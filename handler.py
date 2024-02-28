import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

import requests
import json
from seedr import SeedrAPI


class Handler:
    def __init__(self):
        self.seedr = SeedrAPI(email="zincorecoc@gmail.com", password="Lasith@lasith@1998")
        self.account = self.seedr.get_drive()
        
    def get_drive(self):
        space_max = self.account['space_max']
        space_used = self.account['space_used']
        
        return space_max, space_used
    
    def get_folders(self):
        folders = self.account['folders']
        return folders
    
    def get_files(self):
        files = self.account['files']
        return files
    
    def get_all(self):
        folders = self.get_folders()
        files = self.get_files()
        all = folders + files
        
        return all
        
        
handler = Handler()
print(handler.get_all())