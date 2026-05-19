import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_data(n: int = 5000, seed: int = 42) -> pd.DataFrame:
    """Generate realistic Dubai property transaction data."""
    np.random.seed(seed)
    random.seed(seed)

    areas = {
        "Downtown Dubai":      {"price_sqft": 2200, "types": ["Apartment", "Penthouse"]},
        "Dubai Marina":        {"price_sqft": 1800, "types": ["Apartment", "Penthouse"]},
        "Palm Jumeirah":       {"price_sqft": 3500, "types": ["Villa", "Apartment", "Penthouse"]},
        "Business Bay":        {"price_sqft": 1600, "types": ["Apartment"]},
        "JBR":                 {"price_sqft": 2000, "types": ["Apartment", "Penthouse"]},
        "JLT":                 {"price_sqft": 1200, "types": ["Apartment"]},
        "Dubai Hills":         {"price_sqft": 1500, "types": ["Villa", "Townhouse", "Apartment"]},
        "Arabian Ranches":     {"price_sqft": 1300, "types": ["Villa", "Townhouse"]},
        "Mirdif":              {"price_sqft":  900, "types": ["Villa", "Townhouse"]},
        "Deira":               {"price_sqft":  700, "types": ["Apartment"]},
        "Bur Dubai":           {"price_sqft":  750, "types": ["Apartment"]},
        "Dubai Creek Harbour": {"price_sqft": 1900, "types": ["Apartment", "Penthouse"]},
    }

    bedroom_map = {
        "Apartment":  [1, 2, 3],
        "Villa":      [3, 4, 5, 6],
        "Townhouse":  [3, 4, 5],
        "Penthouse":  [3, 4, 5],
    }

    base_size = {1: 700, 2: 1100, 3: 1600, 4: 2200, 5: 3000, 6: 4000}
    growth    = {2022: 1.00, 2023: 1.12, 2024: 1.22, 2025: 1.35}

    start_date = datetime(2022, 1, 1)
    date_range = (datetime(2025, 12, 31) - start_date).days

    records = []
    for _ in range(n):
        area_name  = random.choice(list(areas.keys()))
        area_data  = areas[area_name]
        prop_type  = random.choice(area_data["types"])
        bedrooms   = random.choice(bedroom_map[prop_type])

        date     = start_date + timedelta(days=random.randint(0, date_range))
        year     = date.year
        quarter  = (date.month - 1) // 3 + 1

        size_sqft   = int(base_size[bedrooms] * np.random.normal(1.0, 0.15))
        price_sqft  = area_data["price_sqft"] * growth[year] * np.random.normal(1.0, 0.12)
        price_aed   = int(size_sqft * price_sqft)

        records.append({
            "date":           date.strftime("%Y-%m-%d"),
            "year":           year,
            "quarter":        quarter,
            "area":           area_name,
            "property_type":  prop_type,
            "bedrooms":       bedrooms,
            "size_sqft":      size_sqft,
            "price_aed":      price_aed,
            "price_per_sqft": round(price_sqft, 2),
        })

    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])
    return df
