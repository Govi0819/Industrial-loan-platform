def calculate_revenue(production_tonnes,price_per_tonnes):
    revenue= production_tonnes * price_per_tonnes
    return revenue

def calculate_operating_cost(production_tonnes,variable_cost_per_tonne,fixed_costs):
    operating_cost= (production_tonnes * variable_cost_per_tonne) + fixed_costs
    return operating_cost

def calculate_cash_available(revenue,operating_cost):
    cash_available=revenue - operating_cost
    return cash_available

def calculate_DSCR(cash_available,annual_debt_payment):
    DSCR=cash_available / annual_debt_payment
    return DSCR

def assess_DSCR(DSCR,minimum_dscr):
    if (DSCR >= minimum_dscr + 0.25):
        return "Strong"
    elif (DSCR >= minimum_dscr):
        return "Meets Covenant"
    elif (DSCR >= 1.0):
       return "Below Covenant"
    else:
       return "Cannot Fully Cover Covenant"
    






production_tonnes = 1_000_000
price_per_tonne = 300
variable_cost_per_tonne = 180
fixed_costs = 50_000_000
annual_debt_payment = 40_000_000
minimum_dscr=1.25



annual_revenue=calculate_revenue(production_tonnes,price_per_tonne)
print(annual_revenue)
operating_cost=calculate_operating_cost(production_tonnes,variable_cost_per_tonne,fixed_costs)
print(operating_cost)
cash_available=calculate_cash_available(annual_revenue,operating_cost)
print(cash_available)
DSCR=calculate_DSCR(cash_available,annual_debt_payment)
print(DSCR)
risk_assessment = assess_DSCR(DSCR, minimum_dscr)
print(risk_assessment)
