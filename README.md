# ⚽ Delivery Hotspot Suppression System (DHSS)

### A Spatial Analytics Framework for Measuring Defensive Control of Corner Delivery Zones

![Python](https://img.shields.io/badge/Python-Analytics-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Football Analytics](https://img.shields.io/badge/Football-Analytics-green)
![StatsBomb](https://img.shields.io/badge/Data-StatsBomb-orange)

---

# 📌 Project Overview

The **Delivery Hotspot Suppression System (DHSS)** is a football analytics framework designed to quantify how effectively teams suppress dangerous corner delivery locations.

While most set-piece analysis focuses on outcomes such as shots, goals, or expected goals (xG), DHSS evaluates an earlier phase of the defensive process:

> **Where are opponents allowed to deliver the ball during corner situations?**

The model transforms event-level football data into a spatial defensive intelligence metric that measures a team's ability to restrict access to high-value delivery zones.

---

# 🎯 Business Problem

Traditional football analytics often evaluates what happens after a corner is delivered:

* Shots
* Goals
* xG
* First Contacts

However, the quality of the delivery location itself is rarely measured.

This project addresses the question:

> **How effectively does a team prevent opponents from delivering corners into dangerous areas of the penalty box?**

By focusing on spatial control, DHSS provides a new perspective on set-piece defensive performance.

---

# 🧠 Methodology

## #️⃣ 1. Event Extraction

Corner events are isolated from event-level match data.

**Filters Applied**

* Event Type = Pass
* Pass Type = Corner

---

## #️⃣ 2. Spatial Feature Engineering

Each delivery is mapped using:

* End X Coordinate
* End Y Coordinate
* Delivery Location
* Defensive Context

The resulting coordinates are transformed into tactical delivery zones.

---

## #️⃣ 3. Zone Classification Framework

Corner deliveries are classified into four spatial risk zones.

| Zone             | Tactical Risk |
| ---------------- | ------------- |
| 🔴 6Y_BOX        | Very High     |
| 🟠 PENALTY_SPOT  | High          |
| 🟡 EDGE_ZONE     | Medium        |
| 🟢 WIDE_DELIVERY | Low           |

---

## #️⃣ 4. Weighted Danger Model

Each zone is assigned a risk weight.

| Zone          | Weight |
| ------------- | ------ |
| 6Y_BOX        | 4      |
| PENALTY_SPOT  | 3      |
| EDGE_ZONE     | 2      |
| WIDE_DELIVERY | 1      |

This converts spatial locations into quantifiable danger values.

---

## #️⃣ 5. DHSS Calculation

Average danger is calculated as:

```python
Avg_Danger = Total_Danger / Corners_Faced
```

DHSS is then computed as:

```python
DHSS = ((4 - Avg_Danger) / 4) * 100
```

### Interpretation

* Higher DHSS = Better suppression of dangerous delivery zones
* Lower DHSS = Greater exposure to high-risk deliveries

---

# 📊 Output Metrics

For every team, the model generates:

* Matches Analysed
* Corners Faced
* Total Danger Accumulated
* Average Delivery Danger
* DHSS Score

---

# 📈 Sample Results

| Team            | DHSS  | Interpretation     |
| --------------- | ----- | ------------------ |
| Elche           | 45.83 | Strong Suppression |
| Huesca          | 42.86 | Good Control       |
| Barcelona       | 32.87 | Moderate Control   |
| Atlético Madrid | 19.23 | Weak Suppression   |

---

# 🔍 Key Insight

DHSS shifts defensive evaluation from outcome analysis to spatial control analysis.

Traditional Question:

❌ Did the team concede?

DHSS Question:

✅ Did the team allow dangerous delivery locations?

This provides a more proactive measure of defensive set-piece performance.

---

# 📊 Interactive Dashboard

The project includes a Streamlit dashboard featuring:

* 🏆 DHSS League Rankings
* 📈 Team Comparison Visualisations
* 🔎 Team-Level Profiles
* 📊 Defensive Performance Metrics
* 🧠 Tactical Interpretation Layer

---

# 🛠️ Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Visualisation

* Plotly
* Matplotlib

### Dashboard

* Streamlit

### Data Source

* StatsBomb Open Data

---

# 📂 Project Structure

```text
DHSS/
│
├── data/
│   ├── league_summary.csv
│
├── notebooks/
│   ├── DHSS_Single_Match.ipynb
│   ├── DHSS_Multi_Match.ipynb
│
├── dashboards/
│   ├── app.py
│
├── src/
│   ├── zone_classification.py
│   ├── dhss_model.py
│
├── images/
│   ├── dashboard_preview.png
│
└── README.md
```

---

# 🚀 Future Development

Planned enhancements include:

### FCCI Integration

Combine DHSS with the **First Contact Control Index (FCCI)**.

### SPDCI Development

Create a composite model:

**Set-Piece Defensive Control Index (SPDCI)**

combining:

* Delivery Suppression
* First Contact Dominance
* Overall Defensive Control

### Advanced Modelling

* Full Season Analysis
* Opponent Strength Adjustments
* xG-Based Zone Weighting
* Automated Scouting Reports

---

# 📚 Key Learnings

Through this project I developed experience in:

* Spatial Feature Engineering
* Event-Level Football Analytics
* Risk Scoring Frameworks
* Defensive Performance Modelling
* Streamlit Dashboard Development
* Sports Data Storytelling

---

# ⚠️ Limitations

* Current analysis is based on a 35-match sample rather than a full season.
* Zone weights are rule-based and not yet derived from empirical xG values.
* Opponent quality adjustments are not currently included.

---

# 👨‍💻 Author

**Stephen Yaw Ayamah**

Football Data Analyst | Python | Sports Analytics | Data Storytelling

### Connect

* LinkedIn
* GitHub

---

## ⭐ If you found this project interesting, consider giving the repository a star.
