import pytest

from src.loan_model import (
    calculate_annual_loan_payment,
    calculate_max_affordable_payment
)


def test_normal_loan_payment():
    payment = calculate_annual_loan_payment(
        150_000_000,
        0.06,
        5
    )

    assert payment == pytest.approx(35_609_460.06)


def test_zero_interest_loan():
    payment = calculate_annual_loan_payment(
        150_000_000,
        0,
        5
    )

    assert payment == 30_000_000


def test_invalid_loan_term():
    with pytest.raises(
        ValueError,
        match="Loan term must be greater than zero"
    ):
        calculate_annual_loan_payment(
            150_000_000,
            0.06,
            0
        )


def test_struggling_company_cannot_afford_loan():
    payment = calculate_max_affordable_payment(
        cash_available=10_000_000,
        cash_taxes=5_000_000,
        capital_expenditure=8_000_000,
        lease_payments=2_000_000,
        minimum_dscr=1.25,
        minimum_fccr=1.20
    )

    assert payment == 0