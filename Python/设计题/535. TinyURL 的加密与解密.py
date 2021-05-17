'''
转成hashcode，再转成16进制
'''

class Codec:
    def __init__(self):
        self.data = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hashcode = longUrl.__hash__()
        hashcode = hex(hashcode)
        while hashcode in self.data:
            hashcode = hashcode + 'a'
        self.data[hashcode] = longUrl
        return hashcode

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.data[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))