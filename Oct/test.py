import numpy as np
import pandas as pd

ti = np.arange(0.1, 5.1, 0.1)
w_cache = [0]


def f(t, h, w_previous):
    w = w_previous + h*((np.exp(t)*np.sin(t)) + ((h/2) * np.exp(t)*(np.cos(t) + np.sin(t)))
                           + (((h**2)/3)*np.exp(t) * np.cos(t))
                           + (((h**3)/12)*(np.exp(t)*np.cos(t) - np.exp(t*np.sin(t))))
                           )
    w_cache.append(w)
    print(f"t_i is {t}, H is {h}, W is {w}, W_Previous is {w_previous}\n")

for t in ti:
    f(t, 0.1, w_cache[-1])

data = {'t_i': ti,
        'w_i': w_cache[1:]}
df_pointone = pd.DataFrame(data)
df_pointone.to_csv('~/Desktop/Irene/data_pointone.csv', index = False)

  