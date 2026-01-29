# Core Server
# kilixkilik

import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from Byte.BytePacket import BytePacket
from Sf2Logic.Sf2LogicBuy import Sf2LogicBuy
from Sf2Logic.Sf2LogicMain import Sf2LogicMain
from Zones.ZonesLoad import ZonesLoad
from Zones.WanyaKek import WanyaKek

class SkyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Zones handling
        if self.path.endswith(".dz"):
            n = self.path.split('/')[-1]
            d = ZonesLoad.load(n)
            if d:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(d + WanyaKek.info())
                return
        
        # Config handling
        if "config_SF2.xml" in self.path:
            self.send_response(200)
            self.end_headers()
            c = Sf2LogicMain.cfg() # Raw XML
            self.wfile.write(BytePacket.wrap(c, True) + WanyaKek.info())
            return

        self.send_response(404); self.end_headers()

    def do_POST(self):
        self.send_response(200); self.end_headers()
        # Purchase
        if "verify" in self.path:
            res = Sf2LogicBuy.ok().encode()
            self.wfile.write(BytePacket.wrap(res) + WanyaKek.info())
        else:
            self.wfile.write(b"<ok/>" + WanyaKek.info())

def bk():
    # background connect simulation
    while True:
        print(f"[ALIVE] {WanyaKek.info().decode().strip()}")
        time.sleep(10)

def run():
    threading.Thread(target=bk, daemon=True).start()
    srv = HTTPServer(('0.0.0.0', 1344), SkyHandler)
    print("SkyShadow Server Live | kilixkilik")
    srv.serve_forever()

if __name__ == "__main__":
    run()
# kilixkilik
