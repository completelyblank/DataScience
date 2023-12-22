#%%
import arviz as az
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
az.style.use("arviz-doc")

#Energy Plot
data = az.load_arviz_data("centered_eight")
ax = az.plot_energy(data, fill_color=("C8", "C9"))

ax.set_title("Energy Plot")

plt.show()

#Forest Plot
centered_data = az.load_arviz_data("centered_eight")
ax = az.plot_forest(
    centered_data,
    var_names=["theta"],
    figsize=(8.5, 4),
    colors="C0",
    ess=True,
    # r_hat=True,
)

plt.show()

#TracePlot
az.style.use("arviz-doc")

data = az.load_arviz_data("non_centered_eight")
az.plot_trace(data, var_names=("tau", "mu"))

plt.show()