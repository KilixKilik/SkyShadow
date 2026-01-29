# General logic
# kilixkilik

import os

class Sf2LogicMain:
    @staticmethod
    def get_config():
        path = "XmlFile/config_SF2.xml"
        if os.path.exists(path):
            with open(path, "rb") as f:
                return f.read()
        return b"<data></data>"
