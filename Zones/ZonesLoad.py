# zone loader
# kilixkilik
import os

class ZonesLoad:
    @staticmethod
    def load(n):
        p = f"Zones/{n}"
        if os.path.exists(p):
            with open(p, "rb") as f: return f.read()
        return None
# kilixkilik
