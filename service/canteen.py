from typing import Optional

from service.user.base import BaseUser, UserType


class Canteen:
    def __init__(self, name):
        self.name = name

    def order_food(self, user: BaseUser, foods: list[str]) -> Optional[float]:
        '''
        Students or teachers order lunch boxes in the meal ordering system
        :return:
        '''
        cookbook = None
        if user.is_student():
            cookbook = self.query_menu(user.type, discount=user.get_discount())
        elif user.is_teacher():
            cookbook = self.query_menu(user.type, discount=user.get_discount())
        if cookbook is None:
            return None

        price = 0.0
        for food in foods:
            if food in cookbook:
                price += cookbook[food]

        if user.card.balance_inquiry() >= price:
            user.card.deduction(price)
            return price

        return None

    def query_menu(self, customer_type: UserType, discount: float = 1.0):
        if customer_type == UserType.Student:
            return {
                'noodles with sesame paste & pea sprouts': 5 * discount,
                'cool braised noodles': 7 * discount,
                'steamed glutinous rice with eight treasures': 3 * discount,
            }
        elif customer_type == UserType.Teacher:
            return {
                'noodles with sesame paste & pea sprouts': 5 * discount,
                'steamed meat dumpling': 2 * discount,
                'lightly fried Chinese bread': 3 * discount,
            }
        else:
            return None
