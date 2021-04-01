# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.style.use('seaborn-dark')
#matplotlib.style.available

# %%
def exp_plot(N0, array, rates):
    
    plt.figure(figsize = (12, 8))
    for rate in rates:
        plt.plot(array, N0*np.exp(rate*array), label = f"r = {rate}")
    plt.grid(True)
    plt.legend()
    plt.ylabel(r"$N_t$")
    plt.xlabel("time")
    plt.title("Exponential Model")
    plt.savefig("exp_plot.png")
def exp_plot_log(N0, array, rates):
    
    plt.figure(figsize = (12, 8))
    for rate in rates:
        plt.plot(array, np.log(N0*np.exp(rate*array)), label = f"r = {rate}")
    plt.grid(True)
    plt.legend()
    plt.ylabel(r"$\log _ e (N_t)$")
    plt.xlabel("time")
    plt.title("Exponential Model \n Log scale")
    plt.savefig("exp_log_plot.png")


# %%
array = np.linspace(0, 1, 1000)
rates = np.array([1, 2, 2.2, 2.5, 3])
exp_plot(8, array, rates)
exp_plot_log(8, array, rates)


# %%
def logistic(N0, K, rate, time):
    return (K * N0)/(N0 + (np.exp(-rate*time)*(K - N0)))


# %%
time = np.linspace(0, 15, 1000)
for K in np.array([100, 500, 1000]):
    plt.figure(figsize=(12*1.2, 8))
    for rate in [1, 2, 2.2, 2.5, 3, 3.2, 4]:
        plt.plot(time, logistic(8, K, rate, time), label = f"r = {rate}")
        plt.title(f"Logistic curve For Carrying Capacity = {K}")
        plt.legend(loc = 'lower right')
        plt.grid(True)
        plt.xlabel("Time")
        plt.ylabel("Population")
    plt.savefig(f"plot_carrying_{K}.png")


# %%
def robert_mayer(Nt, r, k):
    return Nt*np.exp(r*(1-(Nt/k)))

time = np.arange(0, 100, 1)

for k in np.array([100, 500, 1000]):
    plt.figure(figsize=[9*9, 6*6])
    for r in [1, 2, 2.2, 2.5, 3]:
        array = np.array([])
        Nt = 1
        for t in time:
            array = np.append(array, robert_mayer(Nt, r, k))
            Nt = array[-1]
        plt.plot(time, array, label = f"r = {r}")
        plt.title(f"Robert May For Carrying Capacity = {k}", fontsize = 50)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 40)
        plt.grid(True)
        plt.xlabel("Time", fontsize = 40)
        plt.ylabel("Population", fontsize = 40)
        plt.xticks(fontsize = 40)
        plt.yticks(fontsize = 40)
    plt.savefig(f"robert_plot_carrying_{k}.png")


# %%
def logistic(r, time, k = 100):
    
    x = np.zeros(len(time))
    x[:] = r
    y = np.array([])
    Nt = 1
    for _ in time:
        y = np.append(y, robert_mayer(Nt, r, k))
        Nt = y[-1]
    return x, y


# %%
plt.figure(figsize= np.array([3, 2])*5)
k = 500
for r in np.linspace(0, 5, 500):
    x, y = logistic(r, np.linspace(0, 1000, 1000), k= k)
    plt.scatter(x[900:], y[900:], color = "black", s = 0.05)

plt.grid(True)
plt.xlabel("r")
plt.ylabel("Population")
plt.title(f"Population v/s r after 900 time steps: k = {k}")
plt.savefig(f"Carrying Capacity_{k}.png")
