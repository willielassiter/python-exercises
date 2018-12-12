
import zlib

blob = open ("content.blob", "rb").read ()

print (blob)

content = zlib.decompress (blob)

print (content)

f = open ("content.txt", "wb")

f.write (content)
