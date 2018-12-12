# File: zlib-example-1.py

import zlib

MESSAGE = "life of brian"

compressed_message = zlib.compress (MESSAGE.encode ())
decompressed_message = zlib.decompress (compressed_message)

print ("original:", repr (MESSAGE))
print ("compressed message:", repr (compressed_message))
print ("decompressed message:", decompressed_message.decode ())

print (type (MESSAGE.encode ()))