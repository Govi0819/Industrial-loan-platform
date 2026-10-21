def calculate_revenue(production_tonnes, price_per_tonne):
    if production_tonnes < 0:
        raise ValueError("Production cannot be negative")

    if price_per_tonne < 0:
        raise ValueError("Price cannot be negative")

    return production_tonnes * price_per_tonne


def calculate_operating_cost(
    production_tonnes,
    variable_cost_per_tonne,
    fixed_costs
):
    if production_tonnes < 0:
        raise ValueError("Production cannot be negative")

    if variable_cost_per_tonne < 0:
        raise ValueError("Variable cost cannot be negative")

    if fixed_costs < 0:
        raise ValueError("Fixed costs cannot be negative")

    return (
        production_tonnes * variable_cost_per_tonne
    ) + fixed_costs


def calculate_cash_available(revenue, operating_cost):
    if revenue < 0:
        raise ValueError("Revenue cannot be negative")

    if operating_cost < 0:
        raise ValueError("Operating cost cannot be negative")

    return revenue - operating_cost


def calculate_annual_loan_payment(
    loan_amount,
    interest_rate,
    loan_term
):
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero")

    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")

    if loan_term <= 0:
        raise ValueError("Loan term must be greater than zero")

    if interest_rate == 0:
        return loan_amount / loan_term

    growth_factor = (1 + interest_rate) ** loan_term

    return (
        loan_amount * interest_rate * growth_factor
    ) / (growth_factor - 1)


def calculate_dscr(cash_available, annual_debt_payment):
    if annual_debt_payment <= 0:
        raise ValueError(
            "Annual debt payment must be greater than zero"
        )

    return cash_available / annual_debt_payment


def assess_dscr(dscr, minimum_dscr):
    if minimum_dscr <= 0:
        raise ValueError(
            "Minimum DSCR must be greater than zero"
        )

    if dscr >= minimum_dscr + 0.25:
        return "Strong"
    elif dscr >= minimum_dscr:
        return "Meets Covenant"
    elif dscr >= 1.0:
        return "Below Covenant"
    else:
        return "Cannot Fully Cover Debt"


def format_currency(value):
    return f"${value:,.2f}"




def analyze_loan(
    production_tonnes,
    price_per_tonne,
    variable_cost_per_tonne,
    fixed_costs,
    loan_amount,
    interest_rate,
    loan_term,
    minimum_dscr
):

   

    
    revenue = calculate_revenue(
        production_tonnes,
        price_per_tonne
    )

    operating_cost = calculate_operating_cost(
        production_tonnes,
        variable_cost_per_tonne,
        fixed_costs
    )

    cash_available = calculate_cash_available(
        revenue,
        operating_cost
    )

    annual_payment = calculate_annual_loan_payment(
        loan_amount,
        interest_rate,
        loan_term
    )

    dscr = calculate_dscr(
        cash_available,
        annual_payment
    )

    risk_assessment = assess_dscr(
        dscr,
        minimum_dscr
    )

    return {
        "revenue": revenue,
        "operating_cost": operating_cost,
        "cash_available": cash_available,
        "annual_payment": annual_payment,
        "dscr": dscr,
        "risk_assessment": risk_assessment
    }
    






production_tonnes = 1_000_000
price_per_tonne = 300
variable_cost_per_tonne = 180
fixed_costs = 50_000_000

minimum_dscr=1.25
loan_amount = 150_000_000
interest_rate = 0.06
loan_term = 5


results = analyze_loan(
    production_tonnes,
    price_per_tonne,
    variable_cost_per_tonne,
    fixed_costs,
    loan_amount,
    interest_rate,
    loan_term,
    minimum_dscr
)

print(format_currency(results["revenue"]))
print(format_currency(results["operating_cost"]))
print(format_currency(results["cash_available"]))
print(format_currency(results["annual_payment"]))
print(f'{results["dscr"]:.2f}')
print(results["risk_assessment"])
