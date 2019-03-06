from classes.telegram.phone_search import PhoneSearch
from classes.telegram.vin_search import VinSearch
from classes.telegram.number_search import NumberSearch


class Car:

    def find_by_phone(phone):
        return PhoneSearch.search_phone(phone)

    def find_by_vin(vin):
        return VinSearch.search_vin(vin)

    def find_by_number(number):
        return NumberSearch.search_number(number)
