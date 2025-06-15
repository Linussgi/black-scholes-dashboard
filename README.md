# black-scholes-dashboard

Basic dashboard app for European options pricing using the Black-Scholes equation. Built and hosted with Streamlit and plotted using Plotly. Current version supports put and call options pricing, with varying:

- Stock Price, $S$
- Stock Volatility, $\sigma$
- Strike Price, $K$
- Time to Maturity, $T$
- Risk Free Rate, $r$

The stock price and volatility are fixed ranges shown on the heatmap, whilst the other variables can be manipulated using value sliders. The app is currently hosted on Streamlit [here](https://options-bsp.streamlit.app/).

## Background

The Black-Scholes partial differential equation describes how the value $V$ of an option is determined from various parameters:

$$\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$$

The equation arises from a random walk (similar to heat diffusion in the heat equation). With a series of substitutions, the black-scholes PDE can be transformed into a familliar heat equation with well known solutions. 

### Boundary Conditions

- At maturity $t = T$:

$$V(S, T) = \max(S - K, 0) \quad \text{(call option payoff)}$$
$$V(S, T) = \max(K - S, 0) \quad \text{(put option payoff)}$$

- As $S \to 0$:

$$V(0, t) = 0 \quad \text{(call)}, \quad V(0, t) = K e^{-r(T-t)} \quad \text{(put)}$$

- As $S \to \infty$:

$$V(S, t) \to S - K e^{-r(T-t)} \quad \text{(call)}, \quad V(S, t) \to 0 \quad \text{(put)}$$

### Pricing Equations

Applying the boundary conditons for call and put option types:

European call:
$$C(S, t) = S N(d_1) - K e^{-r (T - t)} N(d_2)$$

European put:
$$P(S, t) = K e^{-r (T - t)} N(-d_2) - S N(-d_1)$$

### Definitions:

$$d_1 = \frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{1}{2} \sigma^2 \right)(T - t)}{\sigma \sqrt{T - t}}$$

$$d_2 = \frac{\ln\left(\frac{S}{K}\right) + \left(r - \frac{1}{2} \sigma^2\right)(T - t)}{\sigma \sqrt{T - t}}$$

The function $N(x)$ is defined as the CDF of a standard normal distribution (standard deviation of 1 and mean of 0):

$$N(x) = \int \limits^{x}_{-\infty} \frac{1}{\sqrt{2 \pi}} \exp \left ( -\frac{t^2}{2} \right )$$