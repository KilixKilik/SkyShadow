# Purchase handling
# kilixkilik

class Sf2LogicBuy:
    @staticmethod
    def verify():
        # Fake success receipt
        return """<?xml version="1.0" encoding="UTF-8" ?>
        <data><result>0</result><status>success</status></data>"""
