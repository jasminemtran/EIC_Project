import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


cln_df_touchpoints = pd.read_parquet("C:\\Labs\\EIC_Project\\Labs\\Resources\\team-project\\touchpoints_cleaned.parquet")
cln_df_mkt_cmp = pd.read_parquet("C:\\Labs\\EIC_Project\\Labs\\Resources\\team-project\\marketing_campaign_cleaned.parquet")
cln_df_trans = pd.read_parquet("C:\\Labs\\EIC_Project\\Labs\\Resources\\team-project\\transactions_cleaned.parquet")

st.write("\n" + "=" * 60)
st.write("CATEGORICAL DATA ANALYSIS")
st.write("=" * 60)

# Create visualizations for categorical data
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Categorical Data Analysis', fontsize=16, fontweight='bold')

# 1. Channel distribution in touchpoints
st.write("\n1. Touchpoint Channels:")
channel_counts = cln_df_touchpoints['channel'].value_counts()
st.write(f"  Unique values: {cln_df_touchpoints['channel'].nunique()}")
st.write(f"  Top 3: {', '.join(channel_counts.head(3).index.tolist())}")
st.write("  Value counts:")
st.write(channel_counts)

ax1 = axes[0, 0]
channel_counts.plot(kind='bar', ax=ax1, color='mediumpurple', edgecolor='purple')
ax1.set_title('Touchpoint Channels')
ax1.set_xlabel('Channel')
ax1.set_ylabel('Count')
ax1.tick_params(axis='x', rotation=45)

# 2. Device types
st.write("\n2. Device Types:")
device_counts = cln_df_touchpoints['device_type'].value_counts()
st.write(f"  Unique values: {cln_df_touchpoints['device_type'].nunique()}")
st.write("  Value counts:")
st.write(device_counts)

ax2 = axes[0, 1]
device_counts.plot(kind='bar', ax=ax2, color='coral', edgecolor='darkred')
ax2.set_title('Device Types')
ax2.set_xlabel('Device')
ax2.set_ylabel('Count')
ax2.tick_params(axis='x', rotation=45)

# 3. Touchpoint types
st.write("\n3. Touchpoint Types:")
touchpoint_counts = cln_df_touchpoints['touchpoint_type'].value_counts()
st.write(f"  Unique values: {cln_df_touchpoints['touchpoint_type'].nunique()}")
st.write("  Value counts:")
st.write(touchpoint_counts)

ax3 = axes[0, 2]
touchpoint_counts.plot(kind='bar', ax=ax3, color='lightgreen', edgecolor='darkgreen')
ax3.set_title('Touchpoint Types')
ax3.set_xlabel('Type')
ax3.set_ylabel('Count')
ax3.tick_params(axis='x', rotation=45)


# Replot after fixing
# channel_fixed = cln_df_touchpoints['channel'].value_counts()
# ax4 = axes[1, 0]
# channel_fixed.plot(kind='bar', ax=ax4, color='mediumpurple', edgecolor='purple')
# ax4.set_title('Channels (After Standardization)')
# ax4.set_xlabel('Channel')
# ax4.set_ylabel('Count')
# ax4.tick_params(axis='x', rotation=45)

# Transaction channels
st.write("\nTransaction Channels:")
trans_channel_counts = cln_df_trans['channel'].value_counts()
st.write("  Value counts:")
st.write(trans_channel_counts)

ax4 = axes[1, 0]
trans_channel_counts.plot(kind='bar', ax=ax4, color='gold', edgecolor='orange')
ax4.set_title('Transaction Channels')
ax4.set_xlabel('Channel')
ax4.set_ylabel('Count')
ax4.tick_params(axis='x', rotation=45)

# Campaign types
st.write("\nCampaign Types:")
campaign_types = cln_df_mkt_cmp['campaign_type'].value_counts()
st.write("  Value counts:")
st.write(campaign_types)

ax5 = axes[1, 1]
campaign_types.plot(kind='bar', ax=ax5, color='salmon', edgecolor='red')
ax5.set_title('Campaign Types')
ax5.set_xlabel('Type')
ax5.set_ylabel('Count')
ax5.tick_params(axis='x', rotation=45)
st.pyplot(fig)