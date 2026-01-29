# Packet wrapper
# kilixkilik

class BytePacket:
    @staticmethod
    def wrap(d, s=False):
        # Add 8hj if needed
        r = b'8hj' + d if s else d
        return r
# kilixkilik
