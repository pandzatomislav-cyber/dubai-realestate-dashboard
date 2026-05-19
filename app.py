import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_generator import generate_data

st.set_page_config(
    page_title="Dubai Real Estate Analytics",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    return generate_data()

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
st.sidebar.title("🏙️ Filters")

years          = sorted(df["year"].unique())
areas          = sorted(df["area"].unique())
property_types = sorted(df["property_type"].unique())
bedrooms       = sorted(df["bedrooms"].unique())

selected_years    = st.sidebar.multiselect("Year",          years,          default=years)
selected_areas    = st.sidebar.multiselect("Area",          areas,          default=areas)
selected_types    = st.sidebar.multiselect("Property Type", property_types, default=property_types)
selected_bedrooms = st.sidebar.multiselect("Bedrooms",      bedrooms,       default=bedrooms)

filtered = df[
    df["year"].isin(selected_years) &
    df["area"].isin(selected_areas) &
    df["property_type"].isin(selected_types) &
    df["bedrooms"].isin(selected_bedrooms)
]

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🏙️ Dubai Real Estate Market Analytics")
st.markdown("**Tracking property transaction trends across Dubai's key districts — 2022 to 2025**")
st.divider()

# ── KPIs ──────────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Transactions", f"{len(filtered):,}")
with col2:
    avg_price = filtered["price_aed"].mean() if len(filtered) > 0 else 0
    st.metric("Avg. Sale Price", f"AED {avg_price / 1_000_000:.2f}M")
with col3:
    avg_sqft = filtered["price_per_sqft"].mean() if len(filtered) > 0 else 0
    st.metric("Avg. Price / sqft", f"AED {avg_sqft:,.0f}")
with col4:
    top_area = filtered["area"].value_counts().index[0] if len(filtered) > 0 else "N/A"
    st.metric("Most Active Area", top_area)

st.divider()

# ── Row 1: Trend + Pie ────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Average Price Trend")
    trend = (
        filtered.groupby(["year", "quarter"])["price_aed"]
        .mean()
        .reset_index()
    )
    trend["period"] = trend["year"].astype(str) + " Q" + trend["quarter"].astype(str)
    fig = px.line(
        trend, x="period", y="price_aed",
        labels={"price_aed": "Avg Price (AED)", "period": ""},
        template="plotly_white"
    )
    fig.update_traces(line_color="#0078D4", line_width=3)
    fig.update_layout(yaxis_tickformat=",.0f")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🏠 Property Type Mix")
    type_counts = filtered["property_type"].value_counts().reset_index()
    type_counts.columns = ["Type", "Count"]
    fig2 = px.pie(
        type_counts, values="Count", names="Type",
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: Bar + Histogram ────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Price by Area")
    area_price = (
        filtered.groupby("area")["price_aed"]
        .mean()
        .sort_values(ascending=True)
        .reset_index()
    )
    fig3 = px.bar(
        area_price, x="price_aed", y="area", orientation="h",
        template="plotly_white",
        color="price_aed",
        color_continuous_scale="Blues",
        labels={"price_aed": "Avg Price (AED)", "area": ""}
    )
    fig3.update_layout(xaxis_tickformat=",.0f", coloraxis_showscale=False)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("📉 Price Distribution")
    fig4 = px.histogram(
        filtered, x="price_aed", nbins=40,
        template="plotly_white",
        labels={"price_aed": "Price (AED)"},
        color_discrete_sequence=["#0078D4"]
    )
    fig4.update_layout(xaxis_tickformat=",.0f")
    st.plotly_chart(fig4, use_container_width=True)

# ── Transaction volume ────────────────────────────────────────────────────────
st.subheader("📅 Transaction Volume by Quarter")
vol = filtered.groupby(["year", "quarter"]).size().reset_index(name="transactions")
vol["period"] = vol["year"].astype(str) + " Q" + vol["quarter"].astype(str)
fig5 = px.bar(
    vol, x="period", y="transactions",
    template="plotly_white",
    color="transactions",
    color_continuous_scale="Blues",
    labels={"transactions": "Number of Transactions", "period": ""}
)
fig5.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig5, use_container_width=True)

# ── Raw data ──────────────────────────────────────────────────────────────────
with st.expander("📋 View Raw Transaction Data"):
    st.dataframe(
        filtered[["date", "area", "property_type", "bedrooms", "size_sqft", "price_aed", "price_per_sqft"]]
        .sort_values("date", ascending=False)
        .head(500),
        use_container_width=True
    )

st.divider()
st.caption("Data represents simulated Dubai property transactions based on DLD market patterns. Built by Tomislav Pandza.")
