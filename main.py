# Author: Lasith Manujitha
# Github: @z1nc0r3
# Description: Manage your Seedr.cc account through Flow Launcher
# Date: 2024-02-23

import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

from flowlauncher import FlowLauncher
from handler import Handler
import requests


class Seedr(FlowLauncher):

    def query(self, query):
        seedr = Handler()
        output = []
        if len(query.strip()) == 0:
            output.append(
                {"Title": "Enter a URL to shorten", "IcoPath": "Images/app.png"}
            )

        else:
            output.append(
                {
                    "Title": "Click to copy",
                    "SubTitle": f"{tiny}",
                    "IcoPath": "Images/copy.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [f"{tiny}"]},
                }
            )

            output.append(
                {
                    "Title": "Click to open in browser",
                    "SubTitle": f"{tiny}",
                    "IcoPath": "Images/open.png",
                    "JsonRPCAction": {"method": "open_url", "parameters": [f"{tiny}"]},
                }
            )

        return output


if __name__ == "__main__":
    Seedr()
