# 2023 UK Used Car Price Analysis

An exploration of what factors most influence second-hand car prices in the UK, particularly car age, mileage, and brand.

---

## Project Overview

**Question:**  
What factors influence second-hand car prices the most in the UK?

**Why:**  
Cars are always something that I've enjoyed, and I know many people who are searching for used cars who are all too aware of the struggle of finding a good deal.

**Key factors examined:**
- Car **age** (year of manufacture)  
- **Mileage**  
- **Brand / Manufacturer**
I thought these factors would most likely have the greatest impact based on previous knowledge, so I chose them.

---

## Dataset Description

- **Source:** Kaggle — a dataset of used car listings in the UK  
- **Rows:** ~ 30,000–40,000 listings (after filtering)  
- **Columns used:**  
  - `Price` — sale price of the car  
  - `Mileage` — how many miles the car has travelled  
  - `Manufacturer` — brand of the car (e.g., Ford, BMW, Toyota, etc.)  
  - `Year of manufacture` — the year car was built  

---

## Preprocessing / Cleaning

Here are some steps taken to make the data analysis reliable:

1. **Drop duplicate listings:** to avoid counting the same car twice.  
2. **Remove missingness** in essential fields (Price, Mileage, Manufacturer, Year) — missing data in these makes charts misleading.  
3. **Filter price bounds**: keep listings with Price between **£500 and £150,000** — removes likely outliers or data errors.  
4. **Filter mileage:** cap at **300,000 miles** — beyond this often data-entry errors or extremely worn cars.

---

## Visualizations / Design Choices

| Chart | Purpose | Design / Reasoning |
|-------|---------|----------------------|
| **Median Price by Year** (Line) | Shows how price drops with age. helps see whether newer car models keep value better | Used a line chart for trend clarity. Only median to reduce noise / excess data |
| **Median Price by Mileage** (Line, 10k‑mile bins) | Captures depreciation due to usage. More interpretable when mileage is grouped | Easily illustrates the trend data |
| **Price by Brand (Distribution)** (Violin + Box) | Highlights how brand affects price volatility and median values | Violin plot helps visualize distribution + outliers across brands |
| **Quantity by Brand** (Bar) | Shows popularity of brands on used market — supply of market | Bar chart is intuitive. Ties into brand popularity / availability |

**Color / Layout Choices:**
- I made sure to give each brand its own brand-specific color to make it easy to track them, as well as to maintain consistency across charts  
- Responsive layout (2×2 dashboard) but also separate charts for embedding purposes.

---

## Reflection

**What worked well:**
- Cleaning strategy made charts much more interpretable  
- Interactive / embedded charts (individual HTML exports) nicely integrate into portfolio post.  
- Violin plot was especially helpful to see price spread per brand

**What was challenging / didn’t work as planned:**
- I was trying to figure out how to get the data for Chart 1 / Chart 2 to change when you disabled / enabled a brand from the legend, but I gave up.
- Originally wanted to use Pie Chart to represent Brand Marketshare, but I couldn't figure out how to get the legend to fully integrate with all charts.

**If I had more time, I’d…**
- Reintroduce an interactive median line for Chart 1 / Chart 2 which would change the median based on the selected brands in the legend.
- Make the dashboard more clean / visually appealing.

[Portfolio Post](https://aridkabir.github.io/itcs4122/project1/)
