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

def calculate_fccr(
    cash_available,
    cash_taxes,
    capital_expenditure,
    annual_loan_payment,
    lease_payments
):
    total_fixed_payments = annual_loan_payment + lease_payments

    if cash_taxes < 0:
        raise ValueError("Cash taxes cannot be negative")

    if capital_expenditure < 0:
        raise ValueError("Capital expenditure cannot be negative")

    if lease_payments < 0:
        raise ValueError("Lease payments cannot be negative")

    if total_fixed_payments <= 0:
        raise ValueError("Total fixed payments must be greater than zero")

    cash_after_required_spending = (
        cash_available
        - cash_taxes
        - capital_expenditure
    )

    return cash_after_required_spending / total_fixed_payments


def calculate_max_affordable_payment(
    cash_available,
    cash_taxes,
    capital_expenditure,
    lease_payments,
    minimum_dscr,
    minimum_fccr
):
    if minimum_dscr <= 0:
        raise ValueError("Minimum DSCR must be greater than zero")

    if minimum_fccr <= 0:
        raise ValueError("Minimum FCCR must be greater than zero")

    if cash_taxes < 0:
        raise ValueError("Cash taxes cannot be negative")

    if capital_expenditure < 0:
        raise ValueError("Capital expenditure cannot be negative")

    if lease_payments < 0:
        raise ValueError("Lease payments cannot be negative")

    max_payment_dscr = cash_available / minimum_dscr

    max_payment_fccr = (
        cash_available
        - cash_taxes
        - capital_expenditure
    ) / minimum_fccr - lease_payments

    strictest_payment_limit = min(
        max_payment_dscr,
        max_payment_fccr
    )

    return max(0, strictest_payment_limit)


def calculate_maximum_loan(
    max_annual_payment,
    interest_rate,
    loan_term
):
    if max_annual_payment <= 0:
        return 0

    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")

    if loan_term <= 0:
        raise ValueError("Loan term must be greater than zero")

    if interest_rate == 0:
        return max_annual_payment * loan_term

    growth_factor = (1 + interest_rate) ** loan_term

    maximum_loan = (
        max_annual_payment * (growth_factor - 1)
    ) / (interest_rate * growth_factor)

    return maximum_loan


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
    minimum_dscr,
    cash_taxes,
    capital_expenditure,
    lease_payments,
    minimum_fccr
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

    fccr = calculate_fccr(
        cash_available,
        cash_taxes,
        capital_expenditure,
        annual_payment,
        lease_payments
    )

    risk_assessment = assess_dscr(
        dscr,
        minimum_dscr
    )

    max_affordable_payment = calculate_max_affordable_payment(
        cash_available,
        cash_taxes,
        capital_expenditure,
        lease_payments,
        minimum_dscr,
        minimum_fccr
    )

    maximum_loan = calculate_maximum_loan(
        max_affordable_payment,
        interest_rate,
        loan_term
    )

    return {
        "revenue": revenue,
        "operating_cost": operating_cost,
        "cash_available": cash_available,
        "annual_payment": annual_payment,
        "dscr": dscr,
        "fccr": fccr,
        "risk_assessment": risk_assessment,
        "max_affordable_payment": max_affordable_payment,
        "maximum_loan": maximum_loan
    }



production_tonnes = 1_000_000
price_per_tonne = 300
variable_cost_per_tonne = 180
fixed_costs = 50_000_000

loan_amount = 150_000_000
interest_rate = 0.06
loan_term = 5

cash_taxes = 5_000_000
capital_expenditure = 8_000_000
lease_payments = 2_000_000

minimum_dscr = 1.25
minimum_fccr = 1.20


results = analyze_loan(
    production_tonnes,
    price_per_tonne,
    variable_cost_per_tonne,
    fixed_costs,
    loan_amount,
    interest_rate,
    loan_term,
    minimum_dscr,
    cash_taxes,
    capital_expenditure,
    lease_payments,
    minimum_fccr
)


print("Revenue:", format_currency(results["revenue"]))
print("Operating cost:", format_currency(results["operating_cost"]))
print("Cash available:", format_currency(results["cash_available"]))
print("Annual payment:", format_currency(results["annual_payment"]))
print(f'DSCR: {results["dscr"]:.2f}')
print(f'FCCR: {results["fccr"]:.2f}')
print("Risk assessment:", results["risk_assessment"])
print(
    "Maximum affordable annual payment:",
    format_currency(results["max_affordable_payment"])
)
print(
    "Maximum affordable loan:",
    format_currency(results["maximum_loan"])
)





