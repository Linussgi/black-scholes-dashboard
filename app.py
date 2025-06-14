import numpy as np
import streamlit as st
import plotly.express as px

from utils import black_scholes
from constants import TICK_FONT

st.set_page_config(layout="wide")
st.title("Black-Scholes Options Pricing")
st.sidebar.markdown("# Parameters")

# Parameters
strike_price = st.sidebar.slider("Strike Price", min_value=50.0, max_value=150.0, value=100.0, step=1.0)
t_mature = st.sidebar.slider("Time to Maturity (months)", min_value=1, max_value=24, value=12) / 12
risk_free = st.sidebar.slider("Annual Risk Free Rate", 0.0, 10.0, 5.0, step=0.5) / 100
option_type = st.sidebar.radio("Option Type", ["Call", "Put"])

# Grid values
S_vals = np.linspace(50, 150, 100)
sigma_vals = np.linspace(0.05, 1.0, 100)
S_grid, sigma_grid = np.meshgrid(S_vals, sigma_vals)

price_grid = black_scholes(S_grid, strike_price, t_mature, risk_free, sigma_grid, option_type=option_type.lower())

# Plot heatmap 
fig = px.imshow(
    price_grid,
    x=S_vals,
    y=sigma_vals,
    color_continuous_scale="YlGnBu",
    labels={"x": "Stock Price", "y": "Volatility", "color": "Option Price"},
    aspect="auto",
    origin="lower",
    zmin=0,
    zmax=strike_price
)

fig.update_layout(
    width=400,
    height=733,
    title=f"{option_type} Option Price Heatmap",
    xaxis=dict(
        title="Stock Price",
        title_font=dict(size=TICK_FONT),
        tickfont=dict(size=TICK_FONT)
    ),
    yaxis=dict(
        title="Volatility",
        title_font=dict(size=TICK_FONT),
        tickfont=dict(size=TICK_FONT)
    ),
    coloraxis_colorbar=dict(
        title="Option Price",
        title_side="right",
        y=0.5,
        thickness=30,
        len=1.0,
        title_font=dict(size=TICK_FONT),
        tickfont=dict(size=TICK_FONT)
    )
)

st.plotly_chart(fig, use_container_width=True)