import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------

# PAGE CONFIG

# ---------------------------------------------------

st.set_page_config(
page_title="DHSS | Delivery Hotspot Suppression System",
layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("league_summary.csv")

df = load_data()

# ---------------------------------------------------

# TITLE

# ---------------------------------------------------

st.title("⚽ Delivery Hotspot Suppression System (DHSS)")

st.markdown("""

### Measuring How Effectively Teams Suppress Dangerous Corner Delivery Zones

DHSS evaluates where opponents are allowed to deliver corners, providing
a spatial view of set-piece defensive performance.
""")

# ---------------------------------------------------

# SIDEBAR FILTERS

# ---------------------------------------------------

st.sidebar.header("Dashboard Filters")

min_matches = st.sidebar.slider(
"Minimum Matches",
min_value=1,
max_value=int(df["Matches"].max()),
value=1
)

team_select = st.sidebar.selectbox(
"Select Team",
sorted(df["defending_team"].unique())
)

# ---------------------------------------------------

# FILTER DATA

# ---------------------------------------------------

df_filtered = df[df["Matches"] >= min_matches]

# ---------------------------------------------------

# KPI CARDS

# ---------------------------------------------------

st.subheader("📊 League Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
"Teams Analyzed",
df_filtered["defending_team"].nunique()
)

col2.metric(
"Total Matches",
int(df_filtered["Matches"].sum())
)

col3.metric(
"Average DHSS",
round(df_filtered["DHSS"].mean(), 2)
)

# ---------------------------------------------------

# LEAGUE RANKINGS

# ---------------------------------------------------

st.subheader("🏆 DHSS League Rankings")

df_ranked = df_filtered.sort_values(
"DHSS",
ascending=False
)

st.dataframe(
df_ranked,
use_container_width=True
)

# ---------------------------------------------------
# DHSS COMPARISON CHART
# ---------------------------------------------------
st.subheader("📈 DHSS Team Comparison")

fig = px.bar(
df_ranked,
x="DHSS",
y="defending_team",
orientation="h",
text="DHSS",
color="DHSS"
)

fig.update_layout(
xaxis_title="DHSS Score",
yaxis_title="Team"
)

st.plotly_chart(
fig,
use_container_width=True
)

# ---------------------------------------------------

# TEAM PROFILE

# ---------------------------------------------------

st.subheader("🔍 Team Profile")

team_data = df[
df["defending_team"] == team_select
]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
"DHSS",
round(team_data["DHSS"].iloc[0], 2)
)

col2.metric(
"Corners Faced",
int(team_data["Corners_Faced"].iloc[0])
)

col3.metric(
"Total Danger",
int(team_data["Total_Danger"].iloc[0])
)

col4.metric(
"Average Danger",
round(team_data["Avg_Danger"].iloc[0], 2)
)

# ---------------------------------------------------

# TACTICAL INSIGHT

# ---------------------------------------------------

st.subheader("🧠 Tactical Insight")

dhss = team_data["DHSS"].iloc[0]
avg_danger = team_data["Avg_Danger"].iloc[0]
corners_faced = team_data["Corners_Faced"].iloc[0]

st.markdown(f"""

### {team_select}

**DHSS Score:** {dhss:.2f}

**Corners Faced:** {corners_faced}

**Average Danger Allowed:** {avg_danger:.2f}

### What does this mean?

DHSS measures how effectively a team suppresses dangerous corner delivery locations.

🟢 Higher DHSS = Better suppression of dangerous zones

🔴 Lower DHSS = More access allowed to high-risk delivery areas

⚽ Lower Average Danger = Opponents forced into safer delivery locations

This model focuses on where danger is allowed to enter the penalty area rather than what happens after the delivery.
""")



# ---------------------------------------------------
# METHODOLOGY
# ---------------------------------------------------
with st.expander("📚 DHSS Methodology"):

    st.markdown("""
### Delivery Hotspot Suppression System (DHSS)

Corner deliveries are classified into four spatial risk zones:

| Zone | Risk Weight |
|------|-------------|
| 6Y_Box | 4 |
| Penalty_Spot | 3 |
| Wide_Delivery | 2 |
| Edge_Zone | 1 |

### Model Logic

Every corner delivery is assigned a danger score based on where the ball lands.

The model then calculates:

- Total Danger
- Average Danger per Corner Faced
- DHSS Score

### Interpretation

Higher DHSS values indicate stronger suppression of dangerous delivery zones.

Lower DHSS values indicate opponents are consistently reaching high-value attacking areas such as the penalty spot and six-yard box.
""")