from __future__ import print_function
import aerospike
from aerospike import predicates as p
import logging


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Testing local Aerospike connectivity')

# Configure the client
config = {
  'hosts': [ ('db', 3000) ]
}
# 'hosts': [ ('db', 3000) ]

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config).connect()
except:
  import sys
  logging.error("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)


# check if a set 'customers' contains a least 1000 rows:
n_objects = 0
found = False
sets_dict = client.info("sets")
for key, value in sets_dict.items():
    sets = [x for x in value[1].split(";") if x!='\n']
    for x in sets:
        d = dict(t.split("=") for t in x.split(":"))
        if (d['ns'] == 'test' and d['set'] == 'customer'):
            n_objects = int(d['objects'])
            found = True
        if (found):
            break

n = 1000

if ((found and n_objects < n) or not found):
    print ('forced insert of %i fake customers' % n)
    for i in range(0,n):
        key = ('test', 'customer', i)
        add_customer(client, key, -i, i+1)

def add_customer(client, key, phone_number, lifetime_value):
    client.put(key, {
        'phone_number': phone_number,
        'ltv': lifetime_value
      }
     )

def get_ltv_by_id(client, key):
    bins = dict()
    try:
        (key, metadata, bins) = client.get(key)
    except:
        pass
    if (bins == {}):
        logging.error('Requested non-existent customer ' + str(key))
    else:
        return bins.get('ltv')


def get_ltv_by_phone(client, phone_number):
    query = client.query('test','customer')
    query.select('ltv')
    query.where( p.equals('phone_number', phone_number) )
    records = query.results()
    for record in records:
    	return(record[2]['ltv'])
    logging.error('Requested phone number %s is not found in (\'test\',\'customer\')' % str(phone_number))


# create a secondary index
try:
    client.index_integer_create('test', 'customer', 'phone_number', 'index_phone')
except:
    pass


# Close the connection to the Aerospike cluster

logging.info('Starting some local tests')
logging.info('query non-existent customer:')

assert get_ltv_by_id(client, ('test', 'customer', -1)) == None
assert get_ltv_by_phone(client, 1) == None


for i in range(0,n):
    assert (i + 1 == get_ltv_by_id(client, ('test', 'customer', i))), "No LTV by ID " + str(i)
    assert (i + 1 == get_ltv_by_phone(client, -i)), "No LTV by phone " + str(-i)

logging.info('Local testing completed')

client.close()

logging.info("Local Aerospike works fine")




