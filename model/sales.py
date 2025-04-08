from dataclasses import dataclass
from datetime import date


@dataclass
class Sales:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: date
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __eq__(self, other):
        if not isinstance(other, Sales):
            return False
        return (
                self.Retailer_code == other.Retailer_code and
                self.Product_number == other.Product_number and
                self.Order_method_code == other.Order_method_code and
                self.Date == other.Date and
                self.Quantity == other.Quantity and
                self.Unit_price == other.Unit_price and
                self.Unit_sale_price == other.Unit_sale_price
        )

    def __hash__(self):
        return hash((
            self.Retailer_code,
            self.Product_number,
            self.Order_method_code,
            self.Date,
            self.Quantity,
            self.Unit_price,
            self.Unit_sale_price
        ))