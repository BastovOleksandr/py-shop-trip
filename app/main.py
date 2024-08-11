import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    path = os.getcwd()[:os.getcwd().rfind(os.sep) + 1] + "app" + os.sep

    with open(f"{path}config.json", "r") as file:
        trip_data = json.load(file)

    customers, shops = [], []
    fuel_price = trip_data["FUEL_PRICE"]

    for customer in trip_data["customers"]:
        customers.append(Customer(**customer))

    for shop in trip_data["shops"]:
        shops.append(Shop(**shop))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheap_shop, cheap_cost = customer.find_cheapest(shops, fuel_price)

        if customer.money < cheap_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        customer.ride_to(cheap_shop.location, cheap_shop.name)
        cheap_shop.prints_receipt(customer.product_cart, customer.name)
        customer.pay_and_back(cheap_cost)
