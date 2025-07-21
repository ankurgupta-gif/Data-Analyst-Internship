# Data-Analyst-Internship
# HealthKart Influencer ROI Dashboard
#DASHBOARD LINK=== https://data-analyst-internship-9odkw2fius3t38cmwdpgrk.streamlit.app/#influencer-campaign-roi-dashboard
This project is a Streamlit dashboard that analyzes influencer campaign data across platforms like Instagram, YouTube, and Twitter. It calculates ROI, ROAS, and tracks performance of influencers, posts, and campaigns.

## 📁 Files Included

- `app.py` — Streamlit dashboard
- `requirements.txt` — dependencies for deployment
- `influencers.csv` — influencer master data
- `posts.csv` — post-level performance
- `tracking_data.csv` — order & revenue tracking
- `payouts.csv` — influencer payout structure

## 🚀 Features

- Upload campaign data via UI
- ROI and Incremental ROAS calculations
- Performance tracking for posts & influencers
- Filtering by platform
- Top influencers and poor ROI insights
- Bar chart of top 10 influencers by ROAS


## 🧠 Assumptions

- Baseline revenue is approximated by average revenue across all products.
- Payouts can be per post or per order.
- Incremental ROAS = (Revenue - Baseline) / Total Payout.
- Users are expected to upload the 4 CSV files when using the dashboard.

## ✨ Example Filters Used

- Platform = Instagram
- Product = Whey Protein
- Category = Fitness
