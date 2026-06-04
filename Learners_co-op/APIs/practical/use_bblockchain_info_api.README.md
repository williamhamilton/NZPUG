# Bitcoin Market Trend Analyser

An interactive data visualisation tool built with **Python 3.14** and **Plotly**. This project was developed as a teaching resource for the **Python Learners Co-op** to demonstrate real-time API integration, data transformation, and professional-grade financial charting.

## Overview

This script fetches historical market data from the Blockchain.com API and generates an interactive HTML dashboard. It is designed to be used in a workshop setting, where features can be toggled on to show the progression from a basic line plot to a sophisticated analytical tool.

### Key Learning Objectives

* **API Interaction:** Handling GET requests and query parameters using `requests`.
* **Data Wrangling:** Converting Unix timestamps to human-readable New Zealand date formats.
* **Visualisation:** Implementing technical indicators like Simple Moving Averages (SMA) and automated annotations in Plotly.

---

## Usage

Run the script from your terminal:

```bash
python blockchain_analysis.py

```

Upon successful execution, the script will:

1. Fetch the last 60 days of Bitcoin market price data.
2. Generate a file named `blockchain_analysis.html`.
3. Automatically open the chart in your default web browser.

---

## Workshop Layers

The `create_chart` function is structured in sections to allow for a step-by-step presentation:

* **Core:** The basic price line (The "Minimum Viable Product").
* **Feature 1:** Adds a **Range Slider** for timeline navigation.
* **Feature 2:** Calculates and plots a **7-Day Moving Average** to smooth out volatility.
* **Feature 3:** Automatically identifies and labels the **Period High**.
* **Feature 4:** Displays a **KPI Indicator** showing the current price and percentage change.

---

## Technical Details

* **Language:** Python 3.14+
* **Visualisation:** Plotly Graph Objects
* **Data Source:** [Blockchain.com Charts API](https://www.blockchain.com/explorer/api/charts_api)

---

## Contributing

This is a learning-focused project. If you are part of the Co-op and have an idea for a new feature (like RSI indicators or multi-currency support), feel free to fork the repo and submit a Pull Request!

