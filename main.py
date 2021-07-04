from bitcoin import *
#Generate private key
my_private_key = random_key()

#display private key
print("Private Key: %s\n" % my_private_key)

#Generate public key
my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)

#Create a bitcoin address
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %s\n" % my_bitcoin_address)

from hashlib import sha256
sha256("ABC".encode("ascii")).hexdigest()

from hashlib import sha256
def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()

# MAX_NONCE=10000000
def mine(block_number,transaction,previous_hash,prefix_zeros):
  prefix_str='0'*prefix_zeros
  nonce=0
  while(1):
    text= str(block_number) + transaction + previous_hash + str(nonce)
    hash = SHA256(text)
    # print(hash)
    nonce=nonce+1
    if hash.startswith(prefix_str):
      print("Bitcoin mined with nonce value :",nonce)
      return hash
  print("Could not find a hash in the given range of upto", MAX_NONCE)

transactions='''
A->B->10
B->c->5
'''
difficulty = 5
import time as t
begin=t.time()
new_hash = mine(684260,transactions,"000000000000000000006bd3d6ef94d8a01de84e171d3553534783b128f06aad",difficulty)
print("Hash value : ",new_hash)
time_taken=t.time()- begin
print("The mining process took ",time_taken,"seconds")
