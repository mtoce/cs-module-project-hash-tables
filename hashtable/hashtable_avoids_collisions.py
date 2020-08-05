class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        
        self.storage = [None for x in range(self.capacity)]
        self.count = 0
        self.loadfactor = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.loadfactor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        h = 5381

        for char in key:
            h = ((h << 5) + h) + ord(char)

        return h

    def hash_idx(self, key):
        """
        Take an arbitrary key and return a valid integer idx
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        idx = self.hash_idx(key)
        # self.storage[idx] = value

        # Case 1: no node at idx
        if self.storage[idx] is None:
            self.storage[idx] = HashTableEntry(key, value)
            self.count += 1
            self.loadfactor = self.count / self.capacity
            # resize hashtable by 2x if 70%+ full
            if self.loadfactor > 0.7:
                self.resize(self.capacity * 2)
        # Case 2: node is already at idx
        else:
            cur = self.storage[idx]
            while cur is not None:
                # if the keys are the same, overwrite value
                if cur.key == key:
                    cur.value = value
                    return
                # break so we don't lose position in LL
                if cur.next is None:
                    break
            # Node not found, add to tail of LL
            cur.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_idx(key)
        # If the key DNE in hash table, raise error
        if self.storage[idx] is None:
            raise LookupError('Key does not exist in hash table')
        
        # key does exist
        else:
            # if no key exists next after this key
            if self.storage[idx].next is None:
                self.storage[loc] = None
                self.count -= 1
                self.loadfactor = self.count / self.capacity
                # Divide hashtable size by 2x if 20%- full
                if self.loadfactor < 0.2:
                    self.resize(self.capacity / 2)
            
            # if key exists after current key
            else:
                # go down LL to delete correct node
                cur = self.storage[idx]
                if cur.key == key:
                    # remove headd and stop
                    cur = cur.next
                    self.count -= 1
                    self.loadfactor = self.count / self.capacity
                    # Divide hashtable size by 2x if 20%- full
                    if self.loadfactor < 0.2:
                        self.resize(self.capacity / 2)
                    return
                # if node is not first node, start traversing down LL
                while cur.next is not None:
                    # if next node matches, remove it
                    if cur.next.key == key:
                        cur.next = cur.next.next
                        self.count -= 1
                        self.loadfactor = self.count / self.capacity
                        if self.loadfactor < 0.2:
                            self.resize(self.capacity / 2)
                    cur = cur.next
                # if the node wasn't found
                raise LookupError('key was not found at location')
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_idx(key)

        return self.storage[idx]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
