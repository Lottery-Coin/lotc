# Import statements here
from core.block import Block
from core.blockheader import Blockheader

# Defined constants
ZERO_HASH = "703e4bb330aac6db232a516a5ba8b6e16f968e5bfb2e1e4dbfa1e00e297b95e7"
VERSION = 0.1
EPOC = ""


class Blockchain:
    def __init__(self):
        pass
    
    
    def GenesisBlock(self):
        BlockHeight = 0
        Epoc = EPOC
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash, Epoc)
        
        
    def addBlock(self, BlockHeight, prevBlockHash, Epoc):
        pass
        