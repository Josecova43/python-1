def hello():
    print('hello World')


def pack():
    return[1,2,3]


def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)










    hello()
    eat_lunch(["sandwich", "chips", "apple"])
    eat_lunch(["pizza"])
    eat_lunch([])