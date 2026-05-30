# -Delivery-Hotspot-Suppression-System-DHSS-
A spatial analytics model quantifying how teams suppress dangerous corner delivery zones using event-level football data.
# Project Overview

This project introduces a spatial analytics framework that evaluates how effectively football teams suppress dangerous corner delivery zones.

Instead of focusing on traditional metrics like possession or goals conceded, this model asks:

🧠 Where are opponents allowed to deliver dangerous set-pieces from?

The result is a novel metric:

DHSS (Delivery Hotspot Suppression System) — a zone-weighted measure of defensive control over corner delivery locations.

# Problem Statement

Traditional football analysis overlooks a critical phase of set-pieces:

Shot outcomes are analyzed extensively
First contact is sometimes studied
BUT corner delivery quality is rarely quantified spatially

This project solves:

How can we measure the quality of space allowed during corner deliveries?

# Methodology
1. Event Filtering

Extract all corner events from match event data:

Event Type: Pass
Subtype: Corner
2. Spatial Feature Engineering

Each corner delivery is mapped using:

end_x, end_y coordinates
Pitch location transformation
Spatial zone classification
3. Zone Classification System

Each delivery is assigned a risk zone:

🔴 6Y_BOX → highest danger
🟠 PENALTY_SPOT → high danger
🟡 EDGE_ZONE → medium danger
🟢 WIDE_DELIVERY → low danger
4. Weighted Risk Model

Each zone is assigned a weight:

Zone	Weight
6Y_BOX	4
PENALTY_SPOT	3
EDGE_ZONE	2
WIDE_DELIVERY	1
5. DHSS Formula
Avg_Danger = Total_Danger / Corners_Faced
DHSS = ((4 - Avg_Danger) / 4) × 100

Higher DHSS = better suppression of dangerous delivery zones

📊 Output Metrics

For each team:

Total Corners Faced
Total Danger Accumulated
Average Delivery Risk
DHSS Score (Defensive Control Index)
📈 Sample Results (35-match dataset)
Team	DHSS	Interpretation
Elche	45.8	Strong suppression
Huesca	42.9	Good control
Barcelona	32.9	Moderate control
Atlético Madrid	19.2	Weak suppression
# Key Insight

This model reframes set-piece analysis:

Instead of analyzing outcomes, we analyze space control before the outcome occurs

This shifts focus from:

❌ “Did they concede?”
to:
✔ “Did they allow dangerous entry zones?”
# Tech Stack
Python 🐍
Pandas
NumPy
Streamlit (dashboard layer)
Plotly (visualisation)
Event-level football data (StatsBomb format)
# Streamlit Dashboard

The project includes an interactive dashboard featuring:

🏆 League DHSS rankings
📊 Zone risk visualisation
🔎 Team filtering
📉 Performance comparison
# Project Structure
DHSS-Project/
│
├── data/
│   └── processed_match_events.csv
│
├── notebooks/
│   ├── DHSS_single_match.ipynb
│   ├── DHSS_multi_match.ipynb
│
├── app.py
│   └── Streamlit dashboard
│
├── src/
│   ├── zone_classification.py
│   ├── dhss_model.py
│
└── README.md
# What I Learned
How spatial event data can be transformed into analytical features
How to build weighted risk models from raw coordinates
Importance of aggregation logic in sports analytics pipelines
Why sample size matters in performance models
# Limitations
Current dataset is a sample (35 matches), not full season coverage
Model does not yet include opponent strength adjustments
Future work will integrate FCCI (First Contact Control Index)
# Future Improvements
Full-season league-scale DHSS computation
FCCI integration (first-contact defensive control)
Combined metric: Set-Piece Defensive Control Index (SPDCI)
Expected Goals (xG) weighting for delivery zones
Automated scouting dashboard
# Author

Built by Stephen Yaw Ayamah
Football Data Analyst | Python | Sports Analytics | Data Storytelling
Data Source Statsbomo
