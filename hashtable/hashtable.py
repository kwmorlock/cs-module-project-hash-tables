class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # Has to have a key and value pair (kind of like an object) self.next = none we are trying to implement a linked list, but thats for day 2


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
# min capacity can be any number, but set to 8 for the min capacity in our hash table


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = [None] * capacity
        self.length = 0 #acts as our counter, so we can keep track of what we are adding so we dont have to traverse through whole hash table to find keyvalue pair


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code heres
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.length/self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # self.capacity[self.hash_index(key)] = value
        index = self.hash_index(key)
        #with put we want to update value unlike get that grabs key value
        
        if self.capacity[index] is not None: #checking to make sure slot isnt none
            if self.capacity[index].value is not None: #if value in slot isnt empty
                cur = self.capacity[index] #setting current pointer to the slot its pointing to first
                self.capacity[index] = HashTableEntry(key, value) #using class from start to make it a linkedlist, key and value are parameters from define init to link it
                self.capacity[index].next = cur #making sure the next pointer will be updated to the new current value
                
                self.length += 1 
                if self.get_load_factor() >= 0.7: #if load factor is greater or equal to .7 we will double the slots
                    self.resize(MIN_CAPACITY * 2)
                return 
        self.capacity[index] = HashTableEntry(key, value)

        self.length += 1

        if self.get_load_factor() >= 0.7:
            self.resize(MIN_CAPACITY * 2)




        # we are trying to store value with given key, so we get from the hash
        # table, and we are getting from the slot the key value and we are
        # reassigning the key value into our put method


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.capacity[self.hash_index(key)] = None

        self.put(key, None) #calling put method we made, we are grabbingkey value pair and assigning value to None



        # when we delete we remove the value from the keyvalue and setting it to None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.capacity[self.hash_index(key)]

        index = self.hash_index(key)
        hash_entry = self.capacity[index] #getting keyvalue pair from hashtable, stored as index variable, index from previous line
        if self.capacity[index] is not None: #two conditions (two ifs) if slot isnt empty
            while hash_entry.next is not None: #if the next entry slot is not none
                if hash_entry.key == key: #if has the key then we return value thats paired with the key
                    return hash_entry.value
        return None
        #     cur = self.capacity[index]

        #     while cur is not None:
        #         if cur.key == key:
        #             return cur.value
        #         cur = cur.next
        # else:
        #     return None

        # just getting the value with the given key


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



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


# singly linked lists more effecient than doubly linked lists even though doubley is easier 
# to delete from


# trade off of memory for speed

# array of linked lists to store multiple things by index

# shorter the linked lists are the better

# same key again in dictionary it overwrites previous value

# everytime you do put or get you have to search it