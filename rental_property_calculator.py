class RentalProperty:
    def __init__(self, purchase_price, down_payment, loan_amount, interest_rate, loan_term, rental_income, expenses, vacancy_rate):
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100
        self.loan_term = loan_term
        self.rental_income = rental_income
        self.expenses = expenses
        self.vacancy_rate = vacancy_rate / 100

    def monthly_mortgage_payment(self):
        monthly_rate = self.interest_rate / 12
        num_payments = self.loan_term * 12
        payment = self.loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** -num_payments))
        return payment

    def net_operating_income(self):
        monthly_income = self.rental_income * (1 - self.vacancy_rate)
        monthly_expenses = self.expenses
        noi = (monthly_income - monthly_expenses) * 12
        return noi

    def cash_flow(self):
        return self.net_operating_income() - (self.monthly_mortgage_payment() * 12)

    def cash_on_cash_return(self):
        initial_investment = self.down_payment
        annual_cash_flow = self.cash_flow()
        coc_return = (annual_cash_flow / initial_investment) * 100
        return coc_return


property = RentalProperty(
    purchase_price=200000,
    down_payment=40000,
    loan_amount=160000,
    interest_rate=4.5,
    loan_term=30,
    rental_income=1500,
    expenses=500,
    vacancy_rate=5
)

print("Monthly Mortgage Payment:", property.monthly_mortgage_payment())
print("Net Operating Income:", property.net_operating_income())
print("Annual Cash Flow:", property.cash_flow())
print("Cash on Cash Return:", property.cash_on_cash_return(), "%")