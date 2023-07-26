customer_ids = [ 'C00001', 'C00004','C00010', 'C00004', 'C00011', 'C00004']
print(customer_ids)

print(customer_ids.count('C00004'))

print(len(customer_ids))

print(customer_ids.count('C00004')/ len(customer_ids))


vip_customers = []
customer_id = 'C00011'
if customer_ids.count(customer_id)/ len(customer_ids) > .2:
    vip_customers.append(customer.id)
print(vip_customers)

customer_ids.sort()
print(customer_ids)

print(customer_ids[-2:])


customer_ids.reverse()
print(customer_ids)

if customer_ids.index(customer_id) < 2:
    print('Enjoy this 10 % discount')
    

new_list = sorted(customer_ids)
