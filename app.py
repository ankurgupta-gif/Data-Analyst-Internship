import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Influencer Campaign ROI Dashboard")

with st.sidebar:
    st.header("Upload Campaign Data")
    inf_file = st.file_uploader("Upload influencers.csv", type="csv")
    posts_file = st.file_uploader("Upload posts.csv", type="csv")
    track_file = st.file_uploader("Upload tracking_data.csv", type="csv")
    payout_file = st.file_uploader("Upload payouts.csv", type="csv")

if inf_file and posts_file and track_file and payout_file:
    influencers = pd.read_csv(inf_file)
    posts = pd.read_csv(posts_file)
    tracking = pd.read_csv(track_file)
    payouts = pd.read_csv(payout_file)

    revenue = tracking.groupby("influencer_id")["revenue"].sum().reset_index()
    roas = pd.merge(revenue, payouts, on="influencer_id")
    roas["ROAS"] = roas["revenue"] / roas["total_payout"]
    roas_data = pd.merge(roas, influencers, left_on="influencer_id", right_on="id")

    platform = st.selectbox("Filter by Platform", options=["All"] + list(roas_data["platform"].unique()))
    if platform != "All":
        roas_data = roas_data[roas_data["platform"] == platform]

    st.subheader("Influencer ROAS Summary")
    st.dataframe(roas_data[["name", "platform", "ROAS", "revenue", "total_payout"]].sort_values("ROAS", ascending=False))

    fig = px.bar(roas_data.sort_values("ROAS", ascending=False).head(10), x="name", y="ROAS", color="platform")
    st.plotly_chart(fig)
else:
    st.warning("👈 Upload all 4 required CSV files to get started.")