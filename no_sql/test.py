import logging

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

for i in range(0,1000):
    add_customer(i,i,i + 1)

        
for i in range(0,1000):
    assert (i + 1 == get_ltv_by_id(i)), "No LTV by ID " + str(i)
    assert (i + 1 == get_ltv_by_phone(i)), "No LTV by phone " + str(i)
