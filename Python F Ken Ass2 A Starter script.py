####
### AT2 starter file
###

import hashlib

# Function to produce hash as required
def produce_hash(string_to_hash):
    hashed_object = hashlib.sha256(string_to_hash.encode('utf-8'))
    return hashed_object.hexdigest()

user_wants_to_continue = True

# Main loop
while user_wants_to_continue:
    print(produce_hash("Nobody expects the spammish repetition"))
    
