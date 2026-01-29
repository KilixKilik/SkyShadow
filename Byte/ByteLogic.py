# Byte operations
# kilixkilik

def strip_8hj(data):
    # Remove junk prefix
    return data[3:] if data.startswith(b'8hj') else data

def wrap_8hj(data):
    # Add junk prefix
    return b'8hj' + data
