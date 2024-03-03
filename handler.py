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
        self.seedr = SeedrAPI(
            email="zincorecoc@gmail.com", password="Lasith@lasith@1998"
        )
        self.account = self.seedr.get_drive()

    def get_drive(self):
        space_max = self.account["space_max"]
        space_used = self.account["space_used"]

        return space_max, space_used

    def get_folders(self):
        folders = self.account["folders"]
        return folders

    def get_files(self):
        files = self.account["files"]
        return files

    def get_all(self):
        folders = self.get_folders()
        files = self.get_files()
        all = folders + files

        return all

    def get_folder(self, folder_id):
        folder = self.seedr.get_folder(folder_id)

        for folder in all:
            if "id" in folder and folder["id"] == folder_id:
                return folder["name"], folder["size"]

        return None

    def get_file(self, folder_file_id):
        all = self.get_all()

        for file in all:
            if "folder_file_id" in file and file["folder_file_id"] == folder_file_id:
                return file["name"], file["size"]

        return None

    def add_torrent(self, torrent_url):
        return self.seedr.add_torrent(torrent_url)

    def del_folder(self, folder_id):
        self.seedr.delete_folder(folder_id)

    def del_file(self, folder_file_id):
        self.seedr.delete_file(folder_file_id)


handler = Handler()