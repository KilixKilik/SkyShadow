# Entry point
# kilixkilik

from http.server import HTTPServer, BaseHTTPRequestHandler
from Byte.ByteLogic import wrap_8hj
from Sf2Logic.Sf2LogicBuy import Sf2LogicBuy
from Sf2Logic.Sf2LogicMain import Sf2LogicMain

class SkyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Route config
        if "config_SF2.xml" in self.path:
            self.send_response(200)
            self.end_headers()
            data = Sf2LogicMain.get_config()
            self.wfile.write(wrap_8hj(data))

    def do_POST(self):
        # Route buy
        if "verifyReceipt" in self.path:
            self.send_response(200)
            self.end_headers()
            res = Sf2LogicBuy.verify()
            self.wfile.write(res.encode())

def run():
    addr = ('0.0.0.0', 1344)
    server = HTTPServer(addr, SkyHandler)
    print(f"SkyShadow Server Live on {addr[1]}")
    print("Project by kilixkilik")
    server.serve_forever()

if __name__ == "__main__":
    run()
