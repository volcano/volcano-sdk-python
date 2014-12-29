from volcanosdk.service.Service import Service

seller = Service('Seller');
seller.baseUrl('https://billing-c9-cthos.c9.io/api')

print seller.get(1)['name']
print seller.listContacts(1)
print seller.getContact(1, 1)