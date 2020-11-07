from Cat_main import Cat

cats = [
    dict(name="Барон", gender="мальчик", age="2 года"),
    dict(name="Сэм", gender="мальчик", age="2 года"),
]

for cat in cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print(cat_obj.name, cat_obj.gender, cat_obj.age)