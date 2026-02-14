"""
SkyGeni Sales Intelligence Challenge — Part 4: System Design
==============================================================
Sales Insight & Alert System — Lightweight Architecture

This file defines the system design for a productized version of
the analysis built in Parts 2 & 3.

Run: python src/system_design.py (generates architecture diagram)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

OUTPUT_DIR = 'outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ══════════════════════════════════════════════════════════════════════
# 1. ARCHITECTURE DIAGRAM
# ══════════════════════════════════════════════════════════════════════

def draw_architecture():
    """Generate a clean system architecture diagram."""
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Colors
    C_SOURCE = '#E0F2FE'    # light blue
    C_INGEST = '#FEF3C7'    # light yellow
    C_ENGINE = '#D1FAE5'    # light green
    C_OUTPUT = '#FEE2E2'    # light red
    C_STORE  = '#EDE9FE'    # light purple
    C_BORDER = '#374151'    # dark gray
    FONT = 'DejaVu Sans'

    def draw_box(x, y, w, h, label, sublabel, color, bold=False):
        rect = mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.15",
            facecolor=color, edgecolor=C_BORDER, linewidth=1.5
        )
        ax.add_patch(rect)
        weight = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2 + 0.15, label, ha='center', va='center',
                fontsize=10, fontweight='bold', fontfamily=FONT)
        if sublabel:
            ax.text(x + w/2, y + h/2 - 0.25, sublabel, ha='center', va='center',
                    fontsize=7.5, fontfamily=FONT, color='#4B5563', style='italic')

    def draw_arrow(x1, y1, x2, y2, label=''):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=C_BORDER, lw=1.5))
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx, my + 0.15, label, ha='center', va='bottom',
                    fontsize=7, color='#6B7280', fontfamily=FONT)

    # ── Title ──
    ax.text(9, 11.5, 'SkyGeni Sales Insight & Alert System', ha='center',
            fontsize=18, fontweight='bold', fontfamily=FONT, color='#111827')
    ax.text(9, 11.05, 'Lightweight Production Architecture', ha='center',
            fontsize=11, fontfamily=FONT, color='#6B7280')

    # ── Layer 1: Data Sources (top) ──
    ax.text(1.5, 10.2, '① DATA SOURCES', fontsize=9, fontweight='bold',
            fontfamily=FONT, color='#1E40AF')
    draw_box(0.5, 9.0, 2.5, 0.9, 'CRM', '(Salesforce / HubSpot)', C_SOURCE)
    draw_box(3.5, 9.0, 2.5, 0.9, 'Calendar / Email', '(Activity Data)', C_SOURCE)
    draw_box(6.5, 9.0, 2.5, 0.9, 'Finance', '(Billing / ACV)', C_SOURCE)
    draw_box(9.5, 9.0, 2.5, 0.9, 'Marketing', '(Lead Source Data)', C_SOURCE)
    draw_box(12.5, 9.0, 2.5, 0.9, 'Historical', '(Past Deal Outcomes)', C_SOURCE)

    # ── Layer 2: Ingestion ──
    ax.text(1.5, 8.2, '② INGESTION & PROCESSING', fontsize=9, fontweight='bold',
            fontfamily=FONT, color='#92400E')
    draw_box(2, 7.0, 5.5, 0.9, 'Data Pipeline (Daily)', 'Extract → Clean → Validate → Load', C_INGEST)
    draw_box(9, 7.0, 5.5, 0.9, 'Feature Engineering', 'Velocity Score, Cycle Bucket, Rep Stats', C_INGEST)

    # Arrows from sources to ingestion
    for x in [1.75, 4.75, 7.75, 10.75, 13.75]:
        draw_arrow(x, 9.0, 4.75 if x < 9 else 11.75, 7.9)

    draw_arrow(7.5, 7.45, 9, 7.45)  # pipeline → feature eng

    # ── Layer 3: Engines ──
    ax.text(1.5, 6.2, '③ ANALYSIS ENGINES', fontsize=9, fontweight='bold',
            fontfamily=FONT, color='#065F46')
    draw_box(0.5, 4.8, 3.5, 1.1, 'Win Rate Driver', 'Chi-square tests\nCombo analysis', C_ENGINE)
    draw_box(4.5, 4.8, 3.5, 1.1, 'Deal Risk Scorer', 'Weighted empirical\nwin rate model', C_ENGINE)
    draw_box(8.5, 4.8, 3.5, 1.1, 'Trend Detector', 'Quarter-over-quarter\nmoving averages', C_ENGINE)
    draw_box(12.5, 4.8, 3.5, 1.1, 'Alert Generator', 'Threshold-based\nrule engine', C_ENGINE)

    # Arrows from feature eng to engines
    for x in [2.25, 6.25, 10.25, 14.25]:
        draw_arrow(11.75, 7.0, x, 5.9)

    # ── Layer 4: Storage ──
    draw_box(6.5, 3.3, 5, 0.9, 'Results Store (PostgreSQL)', 'Scores, alerts, driver reports, audit log', C_STORE)

    for x in [2.25, 6.25, 10.25, 14.25]:
        draw_arrow(x, 4.8, 9, 4.2)

    # ── Layer 5: Outputs ──
    ax.text(1.5, 2.7, '④ DELIVERY', fontsize=9, fontweight='bold',
            fontfamily=FONT, color='#991B1B')
    draw_box(0.5, 1.3, 3.2, 1.1, 'CRO Dashboard', 'Win rate trends\nPipeline risk view', C_OUTPUT)
    draw_box(4.2, 1.3, 3.2, 1.1, 'Weekly Email Alerts', 'At-risk deals\nDriver changes', C_OUTPUT)
    draw_box(7.9, 1.3, 3.2, 1.1, 'Rep Scorecards', 'Win rate, velocity\nConsistency index', C_OUTPUT)
    draw_box(11.6, 1.3, 3.2, 1.1, 'Slack Notifications', 'Real-time alerts\nDeal stage changes', C_OUTPUT)

    for x in [2.1, 5.8, 9.5, 13.2]:
        draw_arrow(9, 3.3, x, 2.4)

    # ── Scheduling note ──
    ax.text(16.5, 7.4, 'SCHEDULE', fontsize=8, fontweight='bold',
            fontfamily=FONT, color='#374151')
    ax.text(16.5, 7.0, 'Daily: Pipeline sync', fontsize=7.5, fontfamily=FONT, color='#4B5563')
    ax.text(16.5, 6.7, 'Daily: Risk scoring', fontsize=7.5, fontfamily=FONT, color='#4B5563')
    ax.text(16.5, 6.4, 'Weekly: Driver report', fontsize=7.5, fontfamily=FONT, color='#4B5563')
    ax.text(16.5, 6.1, 'Weekly: Alert emails', fontsize=7.5, fontfamily=FONT, color='#4B5563')
    ax.text(16.5, 5.8, 'Monthly: Model retrain', fontsize=7.5, fontfamily=FONT, color='#4B5563')

    # ── Footer ──
    ax.text(9, 0.4, 'Designed for: CROs, Sales Managers, RevOps  |  Stack: Python + PostgreSQL + Airflow + Slack/Email',
            ha='center', fontsize=8.5, fontfamily=FONT, color='#9CA3AF')

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/13_system_architecture.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print(f"✅ Architecture diagram saved to {OUTPUT_DIR}/13_system_architecture.png")


# ══════════════════════════════════════════════════════════════════════
# 2. PRINT SYSTEM DESIGN SPEC
# ══════════════════════════════════════════════════════════════════════

def print_system_design():
    print("=" * 60)
    print("PART 4 — SYSTEM DESIGN: Sales Insight & Alert System")
    print("=" * 60)

    print("""
┌─────────────────────────────────────────────────────────────┐
│                    SYSTEM OVERVIEW                           │
├─────────────────────────────────────────────────────────────┤
│  A lightweight pipeline that ingests CRM data daily,        │
│  scores every deal for risk, detects win rate shifts,       │
│  and delivers alerts to sales leaders automatically.        │
│                                                             │
│  Audience: CROs, Sales Managers, RevOps                     │
│  Goal: Detect → Diagnose → Act before deals are lost       │
└─────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
① DATA FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  CRM (Salesforce/HubSpot)
    │
    ▼
  Daily ETL Pipeline (Airflow / Cron)
    ├── Extract: Pull new/updated deals via CRM API
    ├── Clean: Validate fields, handle nulls, dedup
    ├── Transform: Compute derived features
    │     • deal_velocity = amount / cycle_days
    │     • cycle_bucket = categorize by duration
    │     • rep_rolling_wr = 90-day rolling win rate
    │     • days_since_last_stage_change
    └── Load: Write to PostgreSQL
    │
    ▼
  Analysis Engines (run after ETL)
    ├── Win Rate Driver Engine (weekly)
    │     • Chi-square tests by segment
    │     • Multi-factor combination analysis
    │     • Compare current vs previous period
    │
    ├── Deal Risk Scorer (daily)
    │     • Score each open deal 0-100
    │     • Weighted: cycle (30%) + rep (25%) + industry (15%)
    │     •           + lead_source (15%) + stage (15%)
    │     • Flag tier: Low / Medium / High / Critical
    │
    ├── Trend Detector (weekly)
    │     • 4-week moving average win rate by segment
    │     • Detect ±5% shifts → trigger alert
    │
    └── Alert Generator (daily + weekly)
          • Match rules → generate alerts
          • Deduplicate (don't repeat same alert)
          • Prioritize by revenue impact
    │
    ▼
  Delivery Layer
    ├── Dashboard (Streamlit / Metabase)
    ├── Weekly Email Digest
    ├── Slack Notifications (urgent only)
    └── Rep Scorecards (monthly)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
② EXAMPLE ALERTS & INSIGHTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🔴 CRITICAL ALERT (Slack — immediate)
  "Deal D04521 ($75K, EdTech) has been at Proposal stage for
   82 days with rep_22 (40% WR). Risk score: 57/100.
   Recommended: Reassign to rep_21 or escalate to VP."

  🟡 WEEKLY DIGEST (Email — Monday 8am)
  "Pipeline Risk Report — Week of Feb 10
   • 3 deals moved to Critical Risk this week ($180K total)
   • EdTech win rate dropped 4% vs last month
   • Referral leads converting 5% better — consider scaling
   • rep_18 has lost 5 consecutive deals in FinTech"

  📊 TREND INSIGHT (Dashboard — updated daily)
  "Win rate for Outbound + EdTech has declined from 48% to 34%
   over the last 8 weeks. This combination now has the lowest
   win rate of any channel-industry pair. 12 open deals match
   this profile, totaling $340K in pipeline."

  📋 REP SCORECARD (Email — monthly)
  "rep_22 — February Performance:
   Win Rate: 38% (team avg: 45%) ▼
   Consistency Index: 0.110 (improving)
   Deal Velocity: $420/day (team avg: $650/day) ▼
   Recommendation: Focus on shorter-cycle deals.
   Pair with rep_21 for coaching sessions."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
③ SCHEDULING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌────────────┬──────────────────────────────────────────┐
  │ Frequency  │ Task                                     │
  ├────────────┼──────────────────────────────────────────┤
  │ Daily 6am  │ CRM data sync + feature engineering      │
  │ Daily 7am  │ Risk scoring on all open deals            │
  │ Daily 7:30 │ Critical alerts → Slack                   │
  │ Weekly Mon │ Driver analysis + trend detection         │
  │ Weekly Mon │ Email digest to CRO + managers            │
  │ Monthly 1st│ Rep scorecards + model recalibration      │
  └────────────┴──────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
④ TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────┬──────────────────────────────────────────┐
  │ Component   │ Tool                                     │
  ├─────────────┼──────────────────────────────────────────┤
  │ Orchestrator│ Apache Airflow (or cron for MVP)         │
  │ Pipeline    │ Python (pandas, scipy)                   │
  │ Database    │ PostgreSQL                               │
  │ Dashboard   │ Streamlit (MVP) or Metabase (scale)      │
  │ Alerts      │ Slack API + SendGrid (email)             │
  │ Deployment  │ Docker + AWS EC2 (or Railway for MVP)    │
  └─────────────┴──────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⑤ FAILURE CASES & LIMITATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────────────┬──────────────────────────────────┐
  │ Failure Case        │ Mitigation                       │
  ├─────────────────────┼──────────────────────────────────┤
  │ CRM data is late    │ Retry with backoff; alert DevOps │
  │ or missing          │ if >2 hrs late. Use last good    │
  │                     │ snapshot as fallback.            │
  ├─────────────────────┼──────────────────────────────────┤
  │ New rep / industry  │ Default to overall avg win rate  │
  │ with no history     │ until 30+ deals accumulated.     │
  │                     │ Flag as "insufficient data."     │
  ├─────────────────────┼──────────────────────────────────┤
  │ Market shift makes  │ Monthly recalibration updates    │
  │ historical rates    │ lookup tables. Weight recent     │
  │ stale               │ data more (exponential decay).   │
  ├─────────────────────┼──────────────────────────────────┤
  │ Alert fatigue (too  │ Deduplicate alerts. Only fire    │
  │ many notifications) │ on ≥5% change or ≥$50K at risk. │
  │                     │ Weekly digest for non-urgent.    │
  ├─────────────────────┼──────────────────────────────────┤
  │ Reps game the       │ Track "stage regression" (deals  │
  │ system (fake stage  │ moving backward). Audit random   │
  │ updates)            │ sample monthly.                  │
  ├─────────────────────┼──────────────────────────────────┤
  │ Scoring is too      │ Current model has narrow risk    │
  │ narrow (51-57       │ range. Add more features (email  │
  │ range)              │ activity, meetings, champion     │
  │                     │ engagement) to widen separation. │
  └─────────────────────┴──────────────────────────────────┘

  KNOWN LIMITATIONS:
  • No competitive intelligence — can't detect "lost to competitor X"
  • No buyer engagement signals (email opens, meeting attendance)
  • Risk scores cluster in a narrow band with current features
  • Rule-based system won't capture non-linear interactions
  • Assumes CRM data is accurate and up-to-date
""")


# ══════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print_system_design()
    draw_architecture()
    print("\n✅ Part 4 complete!")
