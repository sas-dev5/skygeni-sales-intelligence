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

*Next: Part 2 — EDA & Insights*