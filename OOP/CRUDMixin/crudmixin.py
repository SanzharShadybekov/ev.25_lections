from search import searc_object


class CRUDMixin:
    def _get_or_set_objects_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self):
        self._get_or_set_objects_and_id()

    def create(self, **kwargs):
        self.id += 1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}
    
    def list(self):
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'],'title': obj['title'], 'price': obj['price']})
        return {'status': 200, 'msg': res}

    @searc_object
    def detail(self, id, **kwrags):
        obj = kwrags['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found!'}
    
    @searc_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found!'}
    
    @searc_object
    def delete(self, id, **kwargs):
        obj = kwargs.get('object_')
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'msg': 'Deleted!'}
        return {'status': 404, 'msg': 'Not Found!'}
    
    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'


smartphones = CRUDMixin()
print(smartphones.create(title='Redmi Note 10', description='The best phone for own price!', qty=10, price=200))
print(smartphones.create(title='Redmi Note 20', description='The Flagman of redmi phones!', qty=5, price=500))
print(smartphones.create(title='Iphone 14 Pro Max', description='New phone, cool and best!', qty=15, price=1300))
print()
print(smartphones.list())
print()
print(smartphones.detail(3))
print(smartphones.detail(5))
print()
print(smartphones.update(3, title='Iphone 14'))
print(smartphones.update(10, title='Iphone 100'))
print(smartphones.list())
print(smartphones.delete(1))
print(smartphones.list())
print(smartphones.create(title='Samsing S22 Ultra', description='The best phone for android lovers!', qty=8, price=1000))
print(smartphones.create(title='Poco Phone 19', description='Flagman of Poco phones!', qty=5, price=400))
print(smartphones.save())