# 🏙️ Dubai Real Estate Market Analytics Dashboard

An interactive analytics dashboard tracking property transaction trends across Dubai's key districts from 2022 to 2025. Built with Python and Streamlit, deployed to the web.

**[🚀 Live Demo →](https://your-app-url.streamlit.app)** *(link added after deployment)*

---

## Overview

This project analyses 5,000 simulated property transactions across 12 Dubai districts, modelled on Dubai Land Department (DLD) market patterns. It demonstrates end-to-end data analytics skills: data generation, transformation, aggregation, and interactive visualisation.

**Business question answered:** *Which Dubai districts offer the best value per square foot, how has the market trended since 2022, and where is transaction volume growing fastest?*

---

## Features

| Feature | Description |
|---|---|
| KPI Cards | Total transactions, average price, price/sqft, most active area |
| Price Trend | Quarterly average price trend across 2022–2025 |
| Property Type Mix | Breakdown of Apartments, Villas, Townhouses, Penthouses |
| Area Comparison | Average price by district ranked horizontally |
| Price Distribution | Histogram of all transaction values |
| Transaction Volume | Quarterly deal count over time |
| Dynamic Filters | Filter by year, area, property type, and bedrooms |
| Raw Data Table | Full sortable transaction log |

---

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.11 |
| Dashboard | Streamlit |
| Data manipulation | Pandas |
| Visualisation | Plotly Express |
| Data generation | NumPy |
| Deployment | Streamlit Community Cloud |

---

## Project Structure

```
dubai-realestate-dashboard/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── src/
│   ├── __init__.py
│   └── data_generator.py   # Synthetic data generation logic
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/pandzatomislav-cyber/dubai-realestate-dashboard
cd dubai-realestate-dashboard

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
python -m streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## Data Methodology

The dataset is synthetically generated using realistic parameters derived from DLD transaction records:

- **12 districts** with historically accurate price-per-sqft baselines
- **Market growth factors** of +12% (2023), +22% (2024), +35% (2025) reflecting Dubai's actual price appreciation
- **Property type mix** and bedroom distributions matched to each district's real profile
- **5,000 transactions** across a 4-year window (2022–2025)

---

## Key Insights

- **Palm Jumeirah** commands the highest average price per sqft (AED 3,500+)
- **Deira and Bur Dubai** offer the most affordable entry points for investors
- Market-wide prices grew approximately **35% from 2022 to 2025**, consistent with actual DLD data
- **Apartments** account for ~55% of all transactions, reflecting Dubai's rental market demand

---

## Author

**Tomislav Pandza**
Dubai, UAE | [pandza.tomislav@gmail.com](mailto:pandza.tomislav@gmail.com) | [GitHub](https://github.com/pandzatomislav-cyber)

*Studying Microsoft Azure (AZ-900) and Google Cloud Associate Cloud Engineer certifications.*
