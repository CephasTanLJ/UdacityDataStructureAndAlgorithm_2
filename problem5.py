import hashlib
from datetime import datetime


class Block:
    def __init__(self, data, timestamp=datetime.now(), previous_hash=0):
        self.timestamp = timestamp.strftime('%H:%M %d/%m/%Y')
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.previous_block = None

    def calc_hash(self, data):
        '''Hash function'''
        sha = hashlib.sha256()
        hash_str = f'{self.timestamp}'.encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()

    def get_data(self):
        'Return the data (message) of the current block.'
        return self.data

    def get_block_hash(self):
        '''Return the hash code of the current block.'''
        return self.hash

    def get_previous_hash(self):
        '''Return the previous hash code.'''
        return self.previous_hash

    def get_previous_block(self):
        '''Return the block unit/entry of the blockchain.'''
        return self.previous_block

    def set_previous_block(self, previous_block):
        '''Assign the previous block unit to the current block unit.'''
        self.previous_block = previous_block
        self._set_previous_hash(previous_block.get_block_hash())

    def _set_previous_hash(self, previous_hash):
        self.previous_hash = previous_hash

    def __str__(self):
        block_spacing = '---------------'
        return f'{block_spacing}\nTimestamp: {self.timestamp}\nData: {self.data}\nBlock Hash: {self.hash}\nPrevious Hash: {self.previous_hash}\n{block_spacing}\n'


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, next_block):
        '''Append from the head. The last data entered is probably more important than old block(tail).'''
        if type(next_block) is not Block:
            raise TypeError(
                'next_block should be a Block class, please generate your block with Block() class before appending into the blockchain.')
        if self.head is None:
            self.head = next_block
            self.tail = self.head
        else:
            next_block.set_previous_block(self.head)
            self.head = next_block

    def find_block(self, data_message):
        '''Search the blockchain for the block with the data (message) and return the entire block unit.'''
        tracker_node = self.head
        while tracker_node is not None:
            if tracker_node.get_data() == data_message:
                return tracker_node
            tracker_node = tracker_node.get_previous_block()
        return None

    def __str__(self):
        if self.head is None:
            return str(None)
        representation = str()
        tracing_node = self.head
        while tracing_node.get_previous_hash():
            representation = f'{representation}\n{tracing_node}'
            tracing_node = tracing_node.get_previous_block()
        representation = f'{representation}\n{tracing_node}'
        return representation


def test():
    first = Block('Block1')
    first2 = Block('Block2')
    first3 = Block('Block3')
    first4 = Block('Block4')
    BC = BlockChain()

    BC.append(first)
    BC.append(first2)
    BC.append(first3)
    BC.append(first4)

    trace_node = BC.head
    # Assert the oldest block does not have a previous hash
    assert BC.tail.get_previous_hash() == 0, f"The oldest/first block of the block chain should have a hash code of 0 not {BC.tail.get_previous_hash()}"
    assert BC.tail.get_previous_block() is None, f"The oldest/first block of the block chain should have a hash code of 0 not {BC.tail.get_previous_block()}"

    # Assert all other blocks (after the tail block) of the block chain has a hash number, a previous block and a previous block hash
    while trace_node is not None:
        if trace_node is not BC.tail:  # To exclude the tail block
            assert trace_node.get_block_hash() is not None, "Block does not have Hash."
            assert trace_node.get_previous_block() is not None, f"{trace_node} is not linked to a previous block."
            assert trace_node.get_previous_hash() != 0, "Block of the block chain does not have a previous hash info!"
        trace_node = trace_node.get_previous_block()

    assert BC.find_block('Block3') is not None, "Block exists in Blockchain but was not found."
    assert BC.find_block('Block10') is None, "Block does not exists in Blockchain but find_block() did not return None."
    print('test1 blockchain: ')
    print(BC)
    print('End of test1 blockchain\n')


def test2():
    '''Edge Case: Check if a TypeError is raised when none Block class object is append to blockchain. '''
    try:
        BC = BlockChain()
        BC.append('a')
        raise NotImplementedError('Should not be able to proceed as BlockChain appended data/obj is not a Block class.')
    except TypeError:
        print(
            'TypeError was successfully/correctly raised when none Block class object was appended into the BlockChain.')


def test3():
    '''Edge Case: Chech that there should not be any thing printed/returned for an empty Blockchain.'''
    empty_BC = BlockChain()
    assert empty_BC.__str__() == 'None', f'No blockchain should be printed for an empty blockchain, but {empty_BC} if printed.'
    assert empty_BC.find_block(
        'Block10') is None, "Block does not exists in Blockchain but find_block() did not return None."


if __name__ == '__main__':
    test()
    test2()
    test3()
    print('Done')
