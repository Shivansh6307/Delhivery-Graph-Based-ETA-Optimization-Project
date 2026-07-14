# Delhivery Graph-Based ETA Optimization

A consulting-style logistics analytics project built for **Summer Analytics 2026** (IIT Guwahati Consulting & Analytics Club). It models a Delhivery-style logistics network as a graph, identifies operational bottleneck hubs, and shows that network-topology features meaningfully improve delivery ETA prediction over a pure distance/time baseline.

## Problem

Logistics networks lose money to SLA breaches and inflated delivery times, but standard ETA models (e.g. OSRM road-time estimates) ignore *where* a hub sits in the network — whether it's a chronic bottleneck, how central it is, or its historical delay pattern. This project tests whether adding graph-derived features (betweenness centrality, PageRank, in-degree, edge-level delay history) improves ETA prediction and can pinpoint which hubs to fix first.

## Approach

1. **Synthetic data generation** — 20 facilities (6 tier-1 gateways, 8 tier-2 regional hubs, 6 tier-3 DCs) across India, and 15,000 trips with realistic delay behavior driven by route type (FTL vs. Carting), tier pairing, known bottleneck facilities, festive-season seasonality, and time-of-day congestion.
2. **Graph construction & bottleneck analysis** — builds a directed `networkx` graph of the network, computes betweenness centrality, degree, clustering, and a composite bottleneck score per hub, and renders a delay-heatmap network map.
3. **ETA modeling** — compares a baseline Ridge/Gradient Boosting model (trip-level features only) against graph-enhanced GBM/Random Forest models (adding hub centrality + edge delay history).
4. **FTL vs. Carting classifier** — predicts optimal route type using graph and trip features.
5. **Strategy memo** — auto-generates a one-page executive memo (KPIs, top bottleneck hubs, recommendations) as a rendered PNG.

## Results

| Model | MAE (hrs) | R² | Within 15% of actual |
|---|---|---|---|
| Baseline Ridge | 7.88 | 0.756 | 43.4% |
| Baseline GBM | 6.48 | 0.824 | 54.0% |
| **Graph-Enhanced GBM** | **5.64** | **0.857** | **62.4%** |
| Graph-Enhanced RF | 5.84 | 0.853 | 59.3% |

Graph features (betweenness, PageRank, edge-level delay history) cut MAE by ~13% over the best baseline and identified **Delhi (DEL-GW)**, **Nagpur (NGP-RH)**, and **Lucknow (LKO-RH)** as the top bottleneck hubs driving SLA breaches.

FTL vs. Carting routing classifier: **ROC-AUC = 0.73**.

## Project Structure

```
delhivery-eta-optimization/
├── main.py                  # Runs the full pipeline end-to-end
├── requirements.txt
├── src/
│   ├── data_generator.py    # Synthetic facility/trip data generation
│   ├── graph_analysis.py    # Network graph, centrality, bottleneck scoring
│   ├── eta_model.py         # Baseline vs graph-enhanced ETA models
│   ├── ftl_carting.py       # FTL vs Carting routing classifier
│   └── strategy_memo.py     # Executive strategy memo renderer
├── data/                    # Generated CSVs (gitignored, regenerate via main.py)
└── outputs/                 # Generated charts & CSVs (gitignored, regenerate via main.py)
```

## Usage

```bash
pip install -r requirements.txt
python main.py
```

This regenerates all data and produces the following in `outputs/`:
- `network_map.png` — network delay heatmap + top-10 bottleneck hubs
- `model_comparison.png` / `model_comparison.csv` — ETA model benchmarks
- `ftl_carting_analysis.png` — ROC curve + feature importance for routing classifier
- `hub_bottleneck_scores.csv` — per-hub bottleneck scores
- `strategy_memo.png` — one-page executive strategy memo

## Tech Stack

Python, NetworkX, scikit-learn, Matplotlib, Pandas, NumPy.

## Author

Shivansh Verma — Summer Analytics 2026, IIT Guwahati Consulting & Analytics Club.
