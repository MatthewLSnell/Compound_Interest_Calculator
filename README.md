# Compound Interest Calculator with Streamlit

This is a Streamlit application that provides a visual representation of how compound interest works over time, considering both the principal amount and regular contributions.

## Features

- **Calculate the future value** of an investment with regular contributions.
- **Display an annual breakdown** of interest earned, contributions made, and end-of-year balances.
- **Visual representation** of the yearly investment breakdown using a bar chart.

## How it Works

This application is built using:
- [**Streamlit**](https://streamlit.io/) for the user interface.
- [**Pandas**](https://pandas.pydata.org/) for data manipulation and presentation.
- [**Plotly Express**](https://plotly.com/python/plotly-express/) for visual representation.

There are two main functions in the code:
- `compound_interest`: Calculates the future value of an investment considering regular contributions.
- `annual_breakdown`: Provides a yearly breakdown of interest earned, contributions made, and end-of-year balances.

## How to Use

1. **Input the required fields**:
    - Initial Investment ($)
    - Contribution Amount ($)
    - Investment Period (in years)
    - Interest Rate (in %)
    - Compound Times per Year
    - Contribution Periods per Year

2. **Click the `Calculate` button**.

3. **Observe the calculated results**:
    - Future value of the investment.
    - Total contributions made over the period.
    - Total interest collected over the period.
    - A table displaying an annual breakdown of balances.
    - A visual bar chart representing the yearly investment breakdown.

## Getting Started

1. Ensure you have Streamlit, Pandas, and Plotly Express installed.
2. Clone this repository or copy the code to a Python file.
3. Run the Streamlit application using:

```bash
streamlit run compound_interest_calc.py
```

4. Navigate to the provided URL to view and use the application.
