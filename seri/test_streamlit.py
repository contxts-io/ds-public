#%%
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('pegaxy coin insight')

DATE_COLUMN = 'date/time'
DATA_URL = ('pegaxy_db.csv')

#%%

df = pd.read_csv(DATA_URL)
st.write(pd.DataFrame(df))
df = df.dropna()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.plot(df["date"], df["new_pega_cnt"])
