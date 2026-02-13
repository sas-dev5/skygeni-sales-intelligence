# SkyGeni — Sales Intelligence Challenge

**Dataset:** 5,000 B2B SaaS deals (Jan 2023 – Jul 2024) | 25 reps | 5 industries | 4 regions

**Problem:** The CRO says win rate is dropping but pipeline looks healthy — needs to understand what's going wrong and where to focus.

---

## Repo Structure

```
├── README.md
├── data/skygeni_sales_data.csv
├── notebooks/eda.ipynb
├── src/decision_engine.py
├── outputs/
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/skygeni-sales-intelligence.git
cd skygeni-sales-intelligence
pip install -r requirements.txt
```

---

## Part 1 — Problem Framing

### 1.1 The Real Problem

The CRO sees a symptom (dropping win rate), but the actual problem is threefold:

- **Diagnosis gap** — No visibility into *which* segments, reps, or deal types are underperforming
- **Action gap** — No system telling the team *what to change*
- **Timing gap** — Quarterly trends are spotted too late to act on

In short: **"We can't detect, diagnose, and act on revenue risks in real time."**

### 1.2 Questions the AI System Should Answer

| Layer | Questions |
|-------|-----------|
| **What's happening?** | Which segments are losing more? Which reps are slipping? At what funnel stage are deals dying? |
| **Why?** | Are sales cycles getting longer? Are we chasing the wrong deal sizes? Are low-quality lead sources growing? |
| **What to do?** | Which open deals are at risk? What rep/segment changes would move the needle most? |

### 1.3 Key Metrics

**Standard:**
- Win rate (overall + by segment)
- Average sales cycle length
- Stage conversion rates
- Average deal size (won vs. lost)

**Custom (invented for this analysis):**

| Metric | Formula | Why It Matters |
|--------|---------|----------------|
| **Deal Velocity Score** | `deal_amount / sales_cycle_days` | Measures how efficiently pipeline converts to revenue. High pipeline + low velocity = stuck capital. |
| **Rep Consistency Index** | `std_dev(rep's quarterly win rates)` | A rep swinging between 60% and 20% needs different coaching than one steady at 40%. |

### 1.4 Assumptions

1. All deals have a final outcome — no truly open deals in the dataset
2. `deal_stage` = last stage reached before close, not current stage
3. Deal amount is ACV only — no upsells or multi-year values
4. External factors (competitors, pricing, market shifts) are not captured
5. Data is synthetic and uniformly distributed — methodology matters more than specific findings

---

## Part 2 — EDA & Insights

> Run: `python notebooks/eda_analysis.py` — generates 9 charts in `outputs/`

### Dataset Overview

| Metric | Value |
|--------|-------|
| Total Deals | 5,000 |
| Win Rate | 45.3% (2,263 won / 2,737 lost) |
| Avg Deal Size | $26,286 (median $14,172) |
| Avg Sales Cycle | 64 days (range: 7–120 days) |
| Sales Reps | 25 |
| Time Period | Jan 2023 – Jul 2024 |

### Key Finding: Win Rate Is Flat, Not Crashing

The CRO said win rate is "dropping" — but the data shows it's relatively **flat** across quarters (42–48%). The real story is hidden inside specific segments.

![Quarterly Overview](outputs/01_quarterly_overview.png)

---

### Insight 1: EdTech Win Rate Is Collapsing

EdTech dropped from **50.7% → 39.5%** over 5 quarters — the steepest decline of any industry. Meanwhile, FinTech peaked at 51% before falling back.

![Industry Trend](outputs/02_industry_trend.png)

**Why it matters:** EdTech alone accounts for ~20% of all deals. An 11-point drop here drags the entire company's win rate down.

**Action:** Investigate EdTech losses — are competitors winning? Is product-market fit weakening? Consider pausing EdTech outbound spend until diagnosed.

---

### Insight 2: Fast Deals Win More Often

Deals closed within 30 days have a **49.1%** win rate. Deals taking 30–60 days drop to **43.2%**. That's a 6-point gap.

![Cycle vs Win Rate](outputs/03_cycle_vs_winrate.png)

**Why it matters:** The average sales cycle spiked to **81 days in Q2 2024** (up from 63 days). Deals are getting stuck, and stuck deals lose.

**Action:** Set a "deal staleness" alert at 45 days. If a deal hasn't moved stages by then, escalate it or de-prioritize it.

---

### Insight 3: 11-Point Gap Between Best and Worst Reps

rep_21 wins **51%** of deals. rep_22 wins only **40%**. With ~200 deals per rep, that 11-point gap translates to ~20 extra lost deals per underperforming rep.

![Rep Performance](outputs/04_rep_performance.png)

**Why it matters:** The bottom 5 reps collectively lost ~50 more deals than the top 5. Closing this gap is the single highest-leverage action for the CRO.

**Action:** Pair bottom reps with top performers for coaching. Analyze what top reps do differently — faster cycles? better lead sources? specific industries?

---

### Custom Metric 1: Deal Velocity Score

**Formula:** `deal_amount / sales_cycle_days` (revenue generated per day in pipeline)

| Outcome | Avg Velocity |
|---------|-------------|
| Won | $690/day |
| Lost | $631/day |

Q2 2024 velocity crashed to **$396/day** — meaning deals are stuck in the pipeline longer without converting.

![Deal Velocity](outputs/05_deal_velocity.png)

**Why it matters:** Pipeline dollar value can look "healthy" while velocity collapses. This metric is an early warning signal the CRO doesn't currently have.

**Action:** Track velocity weekly. A sustained drop below $500/day should trigger a pipeline review.

---

### Custom Metric 2: Rep Consistency Index

**Formula:** `std_dev(rep's quarterly win rates)` — lower = more consistent

![Rep Consistency](outputs/06_rep_consistency.png)

The scatter plot creates 4 quadrants:

| Quadrant | Meaning | Example |
|----------|---------|---------|
| High WR + Consistent | ★ Ideal performer | rep_21 |
| High WR + Inconsistent | Talented but unpredictable | rep_11 |
| Low WR + Consistent | Consistently underperforming | rep_18 |
| Low WR + Inconsistent | Priority coaching target | rep_22 |

**Action:** Reps in the "Low WR + Inconsistent" quadrant need immediate intervention — they're both underperforming and unpredictable.

---

### Bonus: Lead Source Trends

Inbound leads dropped from **47.9% → 40.5%** win rate (biggest decline). Referral improved from **43.9% → 50.6%** (best recent source).

![Lead Source](outputs/07_lead_source_trend.png)

**Action:** Shift budget toward Referral programs. Audit what changed with Inbound lead quality.

---

### Bonus: Region × Industry Heatmap

![Heatmap](outputs/08_heatmap_region_industry.png)

---

### Summary Dashboard

![Summary Dashboard](outputs/09_summary_dashboard.png)

---