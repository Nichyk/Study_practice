# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium
# for your store(30 percent)
# set_discount(identifier, percent, identifier_type='name') - adds a discount for all products specified
# by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
class Product:
    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = list()
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError('Not a valid product')
        if len(self.products) == 0:
            self.products.append({'product': product, 'amount': amount})
        else:
            for item in self.products:
                if item['product'].name == product.name:
                    item['amount'] += amount
                else:
                    self.products.append({'product': product, 'amount': amount})
                    return self.products

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type not in ['name', 'type']:
            raise ValueError('Invalid identifier type')
        if identifier_type == 'type':
            for item in self.products:
                if item['product'].product_type == identifier:
                    item['product'].price = item['product'].price * ((100 - percent) / 100)
        if identifier_type == 'name':
            for item in self.products:
                if item['product'].name == identifier:
                    item['product'].price = item['product'].price * ((100 - percent) / 100)

    def sell(self, product_name, amount):
        for item in self.products:
            if item['product'].name == product_name:
                if item['amount'] >= amount:
                    item['amount'] -= amount
                else:
                    raise ValueError('Not enough items')
                self.income += item['product'].price * amount
                return self.products

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        for item in self.products:
            if item['product'].name == product_name:
                product_info = (item['product'].name, item['amount'])
                return product_info


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Food', 'Pasta', 4)
s = ProductStore()
s.add(p, 10)
s.add(p, 20)
s.add(p2, 300)
s.sell('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
