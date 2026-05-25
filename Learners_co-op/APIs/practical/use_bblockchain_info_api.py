"""
Blockchain Market Analysis Tool
-------------------------------
A layered script for a Python Learners Co-op workshop.
Standardised to New Zealand English (NZ-en).

Layers:
1. Core Data Fetch & Plot
2. Range Selectors
3. Trend Analysis (Moving Average)
4. Peak Annotations
5. KPI Indicators
"""
# ---------------------------------------------------------------------------------------------------------------------
__author__ = "William Hamilton"
__python__ = ""
__created__ = "25/05/2026"
__copyright__ = "Copyright © 2026~"
__license__ = ""
__ToDo__ = """

"""

import requests
import plotly.graph_objects as go
from datetime import datetime
from typing import Any

# API Configuration
BASE_URL = "https://api.blockchain.info/charts"


def fetch_blockchain_data(chart_name: str = "market-price", days: int = 60) -> list[dict[str, float]]:
    """Fetches time-series data from Blockchain.com."""
    url = f"{BASE_URL}/{chart_name}"
    params = {"timespan": f"{days}days", "format": "json", "sampled": "true"}

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json().get("values", [])
    print(data)


    return data


def create_chart(data: list[dict[str, float]], title: str) -> None:
    """
    Renders an interactive visualisation.
    Layered for live-coding: Uncomment sections to add features.
    """
    # --- CORE DATA PROCESSING ---
    dates = [datetime.fromtimestamp(item["x"]) for item in data]
    prices = [item["y"] for item in data]

    # Initialise the base Figure
    fig = go.Figure()

    # Add the primary Data Trace
    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode='lines',
        name='Market Price',
        line=dict(color='#1f77b4', width=2),
        hovertemplate='<b>Date</b>: %{x|%d %b %Y}<br><b>Price</b>: $%{y:,.2f}<extra></extra>'
    ))

    # Base Layout configuration
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=22)),
        xaxis_title="Timeline",
        yaxis_title="USD Value",
        template="plotly_white",
        margin=dict(t=120)
    )

    # ============================================================
    # FEATURE 1: RANGE SLIDER & SELECTOR BUTTONS
    # ============================================================
    # fig.update_xaxes(
    #     rangeslider_visible=True,
    #     rangeselector=dict(
    #         buttons=list([
    #             dict(count=7, label="1w", step="day", stepmode="backward"),
    #             dict(count=1, label="1m", step="month", stepmode="backward"),
    #             dict(step="all")
    #         ])
    #     )
    # )

    # ============================================================
    # FEATURE 2: 7-DAY MOVING AVERAGE (Trend Analysis)
    # ============================================================
    # window = 7
    # moving_avg = [
    #     sum(prices[i - window:i]) / window if i >= window else None
    #     for i in range(len(prices))
    # ]
    # fig.add_trace(go.Scatter(
    #     x=dates, y=moving_avg,
    #     name=f"{window}-Day SMA",
    #     line=dict(dash='dash', color='orange')
    # ))

    # ============================================================
    # FEATURE 3: AUTOMATED "PEAK" ANNOTATIONS
    # ============================================================
    # max_p = max(prices)
    # max_d = dates[prices.index(max_p)]
    # fig.add_annotation(
    #     x=max_d, y=max_p,
    #     text=f"Period High: ${max_p:,.0f}",
    #     showarrow=True, arrowhead=1, bgcolor="gold", bordercolor="black"
    # )

    # ============================================================
    # FEATURE 4: KPI INDICATORS (Top Metric)
    # ============================================================
    # fig.add_trace(go.Indicator(
    #     mode="number+delta",
    #     value=prices[-1],
    #     title={"text": "Current Price"},
    #     delta={'reference': prices[0], 'relative': True},
    #     domain={'x': [0, 0.3], 'y': [0.8, 0.95]}
    # ))

    # ============================================================
    # FINAL UI POLISH (Unified Hover & Legend Position)
    # ============================================================
    # fig.update_layout(
    #     hovermode="x unified",
    #     legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    # )

    output_file = "blockchain_analysis.html"
    fig.write_html(output_file)
    print(f"[SUCCESS] Interactive chart generated: {output_file}")
    fig.show()


def main() -> int:
    """Orchestrates the data pipeline for the co-op session."""
    print(f"[{datetime.now():%H:%M:%S}] Initialising data fetch...")

    try:
        raw_data = fetch_blockchain_data("market-price", days=60)

        if not raw_data:
            print("[WARNING] API returned an empty dataset.")
            return 1

        create_chart(raw_data, "Bitcoin Market Trend Analysis")
        return 0

    except Exception as err:
        print(f"[ERROR] An unexpected error occurred: {err}")
        return 1


if __name__ == "__main__":
    main()