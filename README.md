volcano-sdk-python
===============

Python SDK for VolcanoCRM

## Purpose
The attempt here is to make a simple to use Python SDK for @volcano.
From the same people (person) who brought you the PHP SDK!

## Example

```python
from volcanosdk.service.Service import Service

seller = Service('Seller');
seller.baseUrl('https://volcano')

print seller.get(1)['name']
print seller.listContacts(1)
print seller.getContact(1, 1)
```