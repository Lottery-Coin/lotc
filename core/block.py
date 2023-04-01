

class Block:
    '''
    Storage container for the blockchain
    '''
    def __init__(self, BlockHeight, Blocksize, BlockHeader, TxCount, Txs):
        self.BlockHeight = BlockHeight
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.TxCount = TxCount
        self.Txs = Txs