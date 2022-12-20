from views import CreateMixin, RetrieveMixin, UpdateMixin, DestroyMixin


class Product(CreateMixin, RetrieveMixin, UpdateMixin, DestroyMixin):  
    def save(self):
        import json
        with open('data_v2.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'


class Order:
    _discount = 5

    def __init__(self, object_) -> None:
        self.orders = []
        self.id = 0
        self.object_ = object_
    
    def create_order(self, objects):
        ls = []
        for item in objects:
            for product in self.object_.objects:
                if item['id'] == product['id']:
                    obj = {'title': product['title'], 'qty': item['qty'], 'price': product['price'] * item['qty']}
                    self._subtrack_qty(item, product)
                    ls. append(obj)
        self.id += 1  
        price = self._total_price(ls)
        self.orders.append({'id': self.id, 'Order': {'Order': ls, 'Price': price}})
        return {'Order': ls, 'Price': price}

    def _total_price(self, objects_):
        prices = [x['price'] for x in objects_]
        total_price = self._make_discount(sum(prices))
        return {'price': sum(prices), 'final_price': total_price}

    def _subtrack_qty(self, item, product):
        result = product['qty'] - item['qty']
        if result < 0:
            raise ValueError('Too many qty of product!')
        product['qty'] = result

    def _make_discount(self, price):
        return price - (price / 100 * self._discount)
    
    def show_all_orders(self):
        return {'All orders': self.orders}


smartphones = Product()
print(smartphones.post(title='Redmi Note 10', description='The best phone for own price!', qty=10, price=200))
print(smartphones.post(title='Redmi Note 20', description='The Flagman of redmi phones!', qty=5, price=500))
print(smartphones.post(title='Iphone 14 Pro Max', description='New phone, cool and best!', qty=15, price=1300))
print(smartphones.post(title='Samsing S22 Ultra', description='The best phone for android lovers!', qty=8, price=1000))
print(smartphones.post(title='Poco Phone 19', description='Flagman of Poco phones!', qty=5, price=400))
print()

print(smartphones.list())

orders = Order(smartphones)
print()
print('Before Order: ---------')
print(smartphones.detail(3))
print(smartphones.detail(4))
print('Order: ')
products_for_order = [{'id': 3, 'qty': 2}, {'id': 4, 'qty': 1}]
print(orders.create_order(products_for_order))
print('After Order: ---------')
print(smartphones.detail(3))
print(smartphones.detail(4))
print()
print()
products_for_order = [{'id': 1, 'qty': 5}]
print(orders.create_order(products_for_order))
products_for_order = [{'id': 4, 'qty': 5}, {'id': 2, 'qty': 3}, {'id': 3, 'qty': 7}]
print(orders.create_order(products_for_order))
print(orders.show_all_orders())
