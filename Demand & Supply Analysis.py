# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:16:18 2023

@author: Fatemeh
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
#pio.templates.default = "plotly_white"
pio.renderers.default = 'browser'

#______________________________________________________________________________
data = pd.read_csv('rides.csv')
print(data.head())

#______________________________________________________________________________
print(data.isnull().sum())

data = data.dropna()
print(data)

#______________________________________________________________________________
demand = data["Riders Active Per Hour"]
print("demand",demand)
supply = data["Drivers Active Per Hour"]
print("supply",supply)

figure = px.scatter(data, x = "Drivers Active Per Hour",
                    y = "Riders Active Per Hour", trendline="ols", 
                    title="Demand and Supply Analysis")
figure.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)")
figure.show()

#______________________________________________________________________________
# Calculate elasticity
avg_demand = data['Riders Active Per Hour'].mean()
print("avg_demand",avg_demand)
avg_supply = data['Drivers Active Per Hour'].mean()
print("avg_supply",avg_supply)
pct_change_demand = (max(data['Riders Active Per Hour']) - min(data['Riders Active Per Hour'])) / avg_demand * 100
print("pct_change_demand",pct_change_demand)
pct_change_supply = (max(data['Drivers Active Per Hour']) - min(data['Drivers Active Per Hour'])) / avg_supply * 100
print("pct_change_supply",pct_change_supply)
elasticity = pct_change_demand / pct_change_supply

print("Elasticity of demand with respect to the number of active drivers per hour: {:.2f}".format(elasticity))

#______________________________________________________________________________
# Calculate the supply ratio for each level of driver activity
data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']
print(data.head())

#______________________________________________________________________________
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], 
                         y=data['Supply Ratio'], mode='markers'))
fig.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active Per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)')
fig.show()