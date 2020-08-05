HASH_DATA_SIZE = 8 

hash_data = [None] * HASH_DATA_SIZE


def hash_function(s):
    """Naive hashing function--do not use in production"""

    # O(n) over the key length
    # O(1) over the HASH_DATA_SIZE

    bytes_list = s.encode()

    total = 0

    for b in bytes_list:  # O(n) over the length of the key
        total += b

        # Optional (but correct) forcing the result to a certain number of bits
        total &= 0xffffffff  # 32 bit (8 f's)
        # total &= 0xffffffffffffffff  # 64 bit (16 f's)

    return total


def get_index(s):
    hash_value = hash_function(s)

    return hash_value % HASH_DATA_SIZE


def put(k, v):
    """For a given key, store a value in the hash table"""
    index = get_index(k)
    hash_data[index] = v


def get(k):
    index = get_index(k)

    return hash_data[index]


# print(hash_data)
put("Beej!", "Hello, world!")


# put("Goats", 3490)
print(get("Beej!"))
# print(get("Goats"))

# print(hash_data)

# print(get_index("Goats"))