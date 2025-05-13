from service.canteen import Canteen
from service.user.student import Student
from service.user.teacher import Teacher


def main():
    canteens = [Canteen('Canteen No.1'), Canteen('Canteen No.2'), Canteen('Canteen No.4')]
    users = [Student(10001), Teacher(1)]

    while True:
        for user in users:
            for canteen in canteens:
                if canteen.order_food(user, ['noodles with sesame paste & pea sprouts']) is None:
                    print(f'user {user.id} order food failed, balance {user.card.balance_inquiry()}')
                    return


if __name__ == '__main__':
    main()
