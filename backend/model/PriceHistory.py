from datetime import date

class PriceHistory:
    def __init__(self, id_price_history, start_date, end_date, price_actual):
        self.id_price_history = id_price_history
        self.start_date = start_date
        self.end_date = end_date
        self.price_actual = price_actual

    def display_price_history(self):
        print(f"ID: {self.id_price_history}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Price Actual: {self.price_actual}")

# Ejemplo de cómo usar la clase PriceHistory
if __name__ == "__main__":
    ph = PriceHistory(1, date(2023, 1, 1), date(2023, 12, 31), 100.5)
    ph.display_price_history()
