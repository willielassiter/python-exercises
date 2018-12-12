
import zlib

blob = open ("blob", "rb").read ()

print (blob)

content = zlib.decompress (blob)

print (content)

f = open ("content", "wb")

f.write (content)
