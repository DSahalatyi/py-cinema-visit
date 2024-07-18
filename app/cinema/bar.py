from __future__ import annotations

from app.people.customer import Customer


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: str | Customer) -> None:
        if isinstance(customer, str):
            print(f"Cinema bar sold {product} to {customer}.")
        else:
            print(f"Cinema bar sold {product} to {customer.name}.")
