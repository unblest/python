# exercise 39 part two: that hashmap/dictionary module

# define a function to add stuff to a list for the range of the number bucket
# doesn't look like we're really adding anything to the list unless we're actually adding the integers 1 - 256
# I'm also not sure what the 'return' thing is doing
def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

# define function that, given a key, will create a number and convert it to an index for the aMap buckets
# I don't fully know what that means
# looks like you pass it the key and it returns a hash and the length where you can find it (hence the index?)
def hash_key(aMap, key):
    """Given a key, this will create a number and then convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)

# define a function that finds the bucket a key goes to
# uses function above to define variable with index to check against the aMap list
# so it's returning a lookup of the aMap list using the index it figures out
# just not sure why we want to do that yet
def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

# define a function to return the index, key and value of a slot found in a bucket
# so it looks like the reverse of the above kind of?
def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)

    # so bucket will be the bucket value returned from the get_bucket function
    # this for loop then enumerates that and checks to see if key equals k value in bucket
    # when it finds the correct k value, it returns it and the corresponding i and v values? I think?
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    # have it return -1, the key and the None default if it runs through the whole for loop without finding the key provided
    return -1, key, default

# define function to return the value in a bucket for a given key
# looks like it basically just defines the three variables (i, k, v) by running the get_slot function and then returns just the v variable
def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

# define a function to set the key to the value
# i'm losing track of what these variables actually stand for
# from this function, it looks kind of like both i and k stand for key
# presumably i stands for index?
def set(aMap, key, value):
    """Sets the key to the vlaue, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # they key does not, append to create it
        # not sure why you need the double parenthases here
        bucket.append((key, value))

# define a function to delete a given key from the Map
# I think this deletes the associated value and index with the key
def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    # ok, so xrange pulls the range of numbers we ask for (the length of buckets retrieved, which, by the way, why isn't that just one?)
    # anyway, it takes that range and essentially uses it just for this function, but doesn't store it in memory like 'range' does
    # also, break just stops the loop from running once the if statement is true and it finds they key it's looking for
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

# define a function to print out what's in the map
# i don't know why we need the if statement in here or what it's doing?
# i guess it's making sure that a bucket is returned and 'True'?
def list(aMap):
    """Prints out what's in the Map"""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v
