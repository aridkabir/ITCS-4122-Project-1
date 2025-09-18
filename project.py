import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

# Load & clean data
df = pd.read_csv("car_sales_data.csv")
df = df.drop_duplicates()
df = df.dropna(subset=["Price", "Mileage", "Manufacturer", "Year of manufacture"])
df = df[(df["Price"].between(500, 150000)) & (df["Mileage"] <= 300000)]

brands = df["Manufacturer"].value_counts().nlargest(10).index
df = df[df["Manufacturer"].isin(brands)]

# Brand colors
brand_colors = {
    "Ford": "#2e659d",
    "Toyota": "#eb081e",
    "BMW": "#1997d8",
    "Porsche": "#e1be85",
    "VW": "#082456",
}

# Chart 1: Median Price by Year
year_price = df.groupby("Year of manufacture")["Price"].median().reset_index()
year_price.columns = ["Year", "Median Price (£)"]
fig_year = px.line(
    year_price,
    x="Year",
    y="Median Price (£)",
    title="Median Car Price by Year of Manufacture",
    labels={"Year": "Year of Manufacture", "Median Price (£)": "Median Price (£)"}
)
fig_year.update_traces(name="Median Price by Year", showlegend=False)

# Chart 2: Median Price by Mileage
df["Mileage_bin"] = (df["Mileage"] // 10000) * 10000
mileage_price = df.groupby("Mileage_bin")["Price"].median().reset_index()
mileage_price.columns = ["Mileage (10k bins)", "Median Price (£)"]
fig_mileage = px.line(
    mileage_price,
    x="Mileage (10k bins)",
    y="Median Price (£)",
    title="Median Car Price by Mileage (10k bins)",
    labels={"Mileage (10k bins)": "Mileage (miles, grouped in 10k)", "Median Price (£)": "Median Price (£)"}
)
fig_mileage.update_traces(name="Median Price by Mileage", showlegend=False)

# Chart 3: Price by Brand 
fig_brand = px.violin(
    df,
    x="Manufacturer",
    y="Price",
    color="Manufacturer",
    box=True,
    points="all",
    title="Car Prices by Brand (Distribution)",
    labels={"Manufacturer": "Car Brand", "Price": "Price (£)"},
    color_discrete_map=brand_colors
)
fig_brand.update_xaxes(tickangle=45)

# Chart 4: Quantity of Cars by Brand
brand_counts = df["Manufacturer"].value_counts().loc[brands].reset_index()
brand_counts.columns = ["Manufacturer", "Number of Listings"]
fig_quantity = px.bar(
    brand_counts,
    x="Manufacturer",
    y="Number of Listings",
    color="Manufacturer",
    title="Quantity Available per Brand",
    labels={"Manufacturer": "Car Brand", "Number of Listings": "Number of Listings"},
    color_discrete_map=brand_colors
)

# Dashboard Layout
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Median Car Price by Year of Manufacture",
        "Median Car Price by Mileage (10k bins)",
        "Car Prices by Brand (Distribution)",
        "Quantity Available per Brand"
    ),
    specs=[[{"type": "xy"}, {"type": "xy"}],
           [{"type": "xy"}, {"type": "xy"}]] 
)

# Dashboard
for trace in fig_year.data:
    trace.showlegend = False
    fig.add_trace(trace, row=1, col=1)

for trace in fig_mileage.data:
    trace.showlegend = False
    fig.add_trace(trace, row=1, col=2)

for trace in fig_brand.data:
    trace.legendgroup = trace.name
    trace.showlegend = True
    fig.add_trace(trace, row=2, col=1)

for trace in fig_quantity.data:
    trace.legendgroup = trace.name
    trace.showlegend = True 
    fig.add_trace(trace, row=2, col=2)

# Final layout
fig.update_layout(
    title_text="UK Second-hand Car Market Sale Analysis",
    title_x=0.5,
    height=900,
    showlegend=True,
    legend_title_text="Brand"
)

fig.show()

# Export
fig.write_html("dashboard.html")
fig_year.write_html("fig_year.html", auto_open=False)
fig_brand.write_html("fig_brand.html", auto_open=False)
fig_mileage.write_html("fig_mileage.html", auto_open=False)
fig_quantity.write_html("fig_quantity.html", auto_open=False)

