from math import e

def compound_invest(capital: float, annual_interest_rate: float, years: int) -> float:
    monthly_interest_rate: float = annual_interest_rate / 12
    months: int = years * 12
#    total: float = capital * ( ((1 + monthly_interest_rate) ** months - 1) / monthly_interest_rate )
    total: float = capital * (e ** (years * annual_interest_rate))
    return total


if __name__ == '__main__':
    monthly_investments: list[int] = [1_000]
    rates: float = [0.038, 0.07, 0.1]
    for r in rates:
        print(f"\n-------------- {r} % --------------")
        for number_years in range(0, 31, 6):
            if number_years == 0:
                number_years = 1
            print(f"\n------- {number_years} years -------")
            for monthly_investment in monthly_investments:
                total_investment = number_years * monthly_investment
                profit = compound_invest(
                    capital=monthly_investment, 
                    annual_interest_rate=r, 
                    years=number_years) # - total_investment
                print(f"Monthly Investment:\t\t{monthly_investment:.2f}€")
                print(f"Total Investment:\t\t{total_investment:.2f}€")
                print(f"Profit:\t\t\t\t\t{profit:.2f}€\n")