

class Blockheader:
    def __init__(self, version, prevBlockHash, timestamp, bits):
        self.version = version
        self.prevBlockHash = prevBlockHash
        self.timestamp= timestamp
        self.bits = bits
        self.nounce = 0
        self.BlockHash = ""