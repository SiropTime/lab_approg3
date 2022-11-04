1. Добавление элементов
   1. Создать Customer
   2. Создать Sportobject
2. Вывод элементов
   1. Вывести там всех Customer
   2. Вывести все Sportobject
   3. Вывести все Order
3. Создание заказа. Алгоритм:
   1. Принимаешь в ввод id Customer, Sportobject
   2. Закидываешь их в make_order()
   3. Profit!
4. Удаление объектов -> Получить id -> По id удалить из словаря

```python
def create_customer():
    id = int(input())
    <...>
    customer = Customer(<...>)

def make_order(orm: OrdersManager):
    customer_id = int(input())
    sportobject_id = int(input())

    # Секция с обработкой ошибок
    <...>

    order = orm.make_order(customer_id, sportobject_id)

    pretty_print(order.__dict__.keys(), order.__dict__.values())
```