def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value

    else:
        for item in items:
            result_item = {}
            has_valid_fields = False

            for key in args:
                value = item.get(key)
                if value is not None:
                    result_item[key] = value
                    has_valid_fields = True

            if has_valid_fields:
                yield result_item

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стул', 'price': 1300, 'color': 'pink', 'made':'Бразилия'},
        {'title': 'Кухня', 'price': 25300, 'color': 'white', },
        {'title': 'Гамак', 'price': 3300, 'color': 'grey'}
    ]
    print(list(field(goods, 'title', 'price')))

if __name__ == "__main__":
    main()