from __future__ import print_function
import aerospike
import logging


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Testig local Aerospike connectivity')

# Configure the client
config = {
  'hosts': [ ('db', 3000) ]
}

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config).connect()
except:
  import sys
  logging.error("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)

# Records are addressable via a tuple of (namespace, set, key)
key = ('test', 'otus', 'de')

try:
  # Write a record
  client.put(key, {
    'provider': 'otus',
    'class': 'data-engineering'
  })
except Exception as e:
  import sys
  print("error: {0}".format(e), file=sys.stderr)

# Read a record
(key, metadata, record) = client.get(key)
logging.debug(record)
assert(record['provider'] == 'otus')
assert(record['class'] == 'data-engineering')

# Close the connection to the Aerospike cluster
client.close()

logging.info("Local Aerospike works fine")


# Simple in-memory implementation of operational data store

store = {}

def add_customer(customer_id, phone_number, lifetime_value):
    store[customer_id] = {'phone': phone_number, 'ltv': lifetime_value}

def get_ltv_by_id(customer_id):
    item = store.get(customer_id, {})
    if (item == {}):
        logging.error('Requested non-existent customer ' + str(customer_id))
    else:
        return item.get('ltv')

def get_ltv_by_phone(phone_number):
    for v in store.values():
        if (v['phone'] == phone_number):
            return v['ltv']
    logging.error('Requested phone number is not found ' + str(phone_number))


logging.info('Starting some local tests against in-memory implementation')

for i in range(0,1000):
    add_customer(i,-i,i + 1)

        
for i in range(0,1000):
    assert (i + 1 == get_ltv_by_id(i)), "No LTV by ID " + str(i)
    assert (i + 1 == get_ltv_by_phone(-i)), "No LTV by phone " + str(-i)

logging.info('Local testing completed')

