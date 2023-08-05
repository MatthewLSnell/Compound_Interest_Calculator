# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set the layout to 'wide'
st.set_page_config(page_title="Compound Interest Calculator", page_icon="🧮", layout="wide")


def compound_interest(
    principal: float,
    contribution: float,
    years: int,
    rate: float,
    compound_frequency: int,
    contribution_periods_per_year: int,
) -> tuple:
    """
    Calculate the future value of an investment with regular contributions.

    Parameters:
    - principal (float): Initial investment amount.
    - contribution (float): Regular contribution amount.
    - years (int): Investment duration in years.
    - rate (float): Annual interest rate in percentage.
    - compound_frequency (int): Number of times the interest is compounded per year.
    - contribution_periods_per_year (int): Number of contributions made per year.

    Returns:
    - tuple: Total future value, total contributions, and total interest earned.
    """
    rate_decimal = rate / 100.0
    future_value_principal = principal * (
        (1 + rate_decimal / compound_frequency) ** (compound_frequency * years)
    )

    future_value_contributions = 0.0
    for period in range(1, years * contribution_periods_per_year + 1):
        periods_left = years * contribution_periods_per_year - period
        future_value_contributions += contribution * (
            (1 + rate_decimal / compound_frequency)
            ** (periods_left / contribution_periods_per_year * compound_frequency)
        )

    total_future_value = round(future_value_principal + future_value_contributions, 2)
    total_contributions = round(contribution * years * contribution_periods_per_year, 2)
    total_interest = round(total_future_value - total_contributions, 2)

    return total_future_value, total_contributions, total_interest


def annual_breakdown(
    principal,
    contribution,
    years,
    rate,
    compound_frequency,
    contribution_periods_per_year,
):
    """
    Get a yearly breakdown of interest earned, contributions made, and balances.

    Parameters are similar to the `compound_interest` function.

    Returns:
    - list: List of dictionaries with a breakdown for each year.
    """
    rate_decimal = rate / 100.0
    data = []

    for year in range(1, years + 1):
        start_balance = principal
        start_principal = principal
        # start_principal = principal
        total_interest_earned = 0
        for compounding_period in range(compound_frequency):
            interest_for_period = principal * (rate_decimal / compound_frequency)
            total_interest_earned += interest_for_period
            principal += interest_for_period
            principal += contribution

        data.append(
            {
                "Year": year,
                "Start Balance ($)": round(
                    start_balance, 2
                ),  # This is the same as "End Principal ($)
                "Interest ($)": round(total_interest_earned, 2),
                "Contributions ($)": contribution * contribution_periods_per_year,
                "End Balance ($)": round(principal, 2),
            }
        )

    return data


# Streamlit UI
st.title("Compound Interest Calculator")

# Create sidebar for input widgets
with st.sidebar:

    # Streamlit UI widgets for user input
    initial_investment = st.number_input(
        "Initial Investment ($)", min_value=0.0, value=1000.0, step=0.1
    )
    contribution_amount = st.number_input(
        "Contribution Amount ($)", min_value=0.0, value=50.0, step=0.1
    )
    investment_period = st.number_input(
        "Investment Period (years)", min_value=1, max_value=50, value=10, step=1
    )
    if investment_period > 50:
        st.warning('The investment period is too high. Please enter a value less than or equal to 50.')
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=5.0, step=0.1)
    compound_times = st.number_input(
        "Compound Times per Year", min_value=1, value=12, step=1
    )
    contrib_periods_per_year = st.number_input(
        "Contribution Periods per Year", min_value=1, value=12, step=1
    )
    
    calculate = st.button("Calculate")

# Calculation and result display when the "Calculate" button is pressed
if calculate:
    result = compound_interest(
        initial_investment,
        contribution_amount,
        investment_period,
        interest_rate,
        compound_times,
        contrib_periods_per_year,
    )
    st.write(
        f"The future value of the investment after {investment_period} years with monthly contributions is: ${result[0]:,.2f}"
    )
    st.write(f"Total contributions made over the period: ${result[1]:,.2f}")
    st.write(f"Total interest collected over the period: ${result[2]:,.2f}")

    # Display the annual breakdown
    breakdown_data = annual_breakdown(
        initial_investment,
        contribution_amount,
        investment_period,
        interest_rate,
        compound_times,
        contrib_periods_per_year,
    )
    df_breakdown = pd.DataFrame(breakdown_data)

    # Cumulative calculations for contributions and interest
    df_breakdown["Total Contributions ($)"] = df_breakdown["Contributions ($)"].cumsum()
    df_breakdown["Total Interest ($)"] = df_breakdown["Interest ($)"].cumsum()
    
    # Visual representation of the investment breakdown
    bar_fig = px.bar(
        df_breakdown,
        x="Year",
        y=["Total Contributions ($)", "Total Interest ($)"],
        title="Yearly Investment Breakdown",
        labels={"value": "Amount ($)", "variable": "Type"},
    )

    # st.plotly_chart(fig,use_container_width=True,height=1500)
    st.plotly_chart(bar_fig, use_container_width=True, height=1500)

    # Format for Streamlit Display
    styled_df = df_breakdown.style.format(
        {
            "Year": "{:.0f}",
            "Start Principal ($)": "${:,.2f}",
            "Start Balance ($)": "${:,.2f}",
            "Interest ($)": "${:,.2f}",
            "Contributions ($)": "${:,.2f}",
            "Total Interest ($)": "${:,.2f}",
            "End Balance ($)": "${:,.2f}",
            "End Principal ($)": "${:,.2f}",
            "Total Contributions ($)": "${:,.2f}",
        }
    )

    st.table(styled_df)
