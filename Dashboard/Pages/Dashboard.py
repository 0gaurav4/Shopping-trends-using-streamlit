import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


df = pd.read_csv(r"C:\Users\gaura\Downloads\python practice\Project\Dashboard\shopping_trends.csv")
df.sample(5)

# Sidebar filters
# 1. Filter by Age Range
age_range = st.sidebar.slider('Select Age Range', int(df['Age'].min()), int(df['Age'].max()), (18, 70))

# 2. Filter by Gender
gender_options = st.sidebar.multiselect('Select Gender', options=df['Gender'].unique(), default=df['Gender'].unique())

# 3. Filter by Location
location_options = st.sidebar.multiselect('Select Location', options=df['Location'].unique(), default=df['Location'].unique())

# 4. Filter by Category
category_options = st.sidebar.multiselect('Select Category', options=df['Category'].unique(), default=df['Category'].unique())

# 5. Filter by Subscription Status
subscription_options = st.sidebar.multiselect('Select Subscription Status', options=df['Subscription Status'].unique(), default=df['Subscription Status'].unique())

# 6. Filter by Season
season_options = st.sidebar.multiselect('Select Season', options=df['Season'].unique(), default=df['Season'].unique())

# 7. Filter by Preferred Payment Method
payment_method_options = st.sidebar.multiselect('Select Preferred Payment Method', options=df['Preferred Payment Method'].unique(), default=df['Preferred Payment Method'].unique())

# 8. Filter by Size
size_options = st.sidebar.multiselect('Select Size', options=df['Size'].unique(), default=df['Size'].unique())


# Apply filters to the dataframe
filtered_df = df[
    (df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1]) &
    (df['Gender'].isin(gender_options)) &
    (df['Location'].isin(location_options)) &
    (df['Category'].isin(category_options)) &
    (df['Subscription Status'].isin(subscription_options)) &
    (df['Season'].isin(season_options)) &
    (df['Preferred Payment Method'].isin(payment_method_options)) &
    (df['Size'].isin(size_options))
]

# Now use the filtered dataframe for the visualizations

# 1. Demographic Information
# Gender distribution
gender_counts = filtered_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']
fig = px.bar(gender_counts, x="Gender", y="Count", color="Gender", title='Gender Distribution')
st.plotly_chart(fig)

# 2. Purchase Behavior
# Bar chart for Purchase Amount (USD) by Age and Gender
fig = px.bar(filtered_df, x="Age", y="Purchase Amount (USD)", color="Gender", title='Purchase Amount (USD) by Age and Gender')
st.plotly_chart(fig)

# Pie chart for Purchase Amount (USD) by Category
fig = px.pie(filtered_df, values='Purchase Amount (USD)', names='Category', title='Purchase Amount (USD) by Category')
st.plotly_chart(fig)

# Line chart for Purchase Amount (USD) over Age
fig = px.histogram(filtered_df, x='Age', y='Purchase Amount (USD)', title='Purchase Amount (USD) over Age')
st.plotly_chart(fig)

# Bar chart for Purchase Amount by Gender and Category
fig = px.bar(filtered_df, x="Category", y="Purchase Amount (USD)", color="Gender", barmode="group", title='Purchase Amount by Gender and Category')
st.plotly_chart(fig)

# 3. Purchase Frequency and Payment Information
# Frequency of Purchases distribution
frequency_counts = filtered_df['Frequency of Purchases'].value_counts().reset_index()
frequency_counts.columns = ['Frequency of Purchases', 'Count']
fig = px.pie(frequency_counts, values="Count", names="Frequency of Purchases", title='Frequency of Purchases')
st.plotly_chart(fig)

# Payment method distribution
payment_method_counts = filtered_df['Preferred Payment Method'].value_counts().reset_index()
payment_method_counts.columns = ['Preferred Payment Method', 'Count']
fig = px.bar(payment_method_counts, x="Preferred Payment Method", y="Count", color="Preferred Payment Method", title='Preferred Payment Method Distribution')
st.plotly_chart(fig)

# Bar chart for Preferred Payment Method by Purchase Frequency
fig = px.bar(filtered_df, x="Preferred Payment Method", color="Frequency of Purchases", title='Preferred Payment Method by Purchase Frequency')
st.plotly_chart(fig)

# 4. Product Preferences and Discounts
# Item Purchased distribution
item_counts = filtered_df['Item Purchased'].value_counts().reset_index()
item_counts.columns = ['Item Purchased', 'Count']
fig = px.bar(item_counts, x="Item Purchased", y="Count", color="Item Purchased", title='Item Purchased Distribution')
st.plotly_chart(fig)

# Discount Applied distribution
discount_counts = filtered_df['Discount Applied'].value_counts().reset_index()
discount_counts.columns = ['Discount Applied', 'Count']
fig = px.bar(discount_counts, x="Discount Applied", y="Count", color="Discount Applied", title='Discount Applied Distribution')
st.plotly_chart(fig)

# Promo Code Used distribution
promo_code_counts = filtered_df['Promo Code Used'].value_counts().reset_index()
promo_code_counts.columns = ['Promo Code Used', 'Count']
fig = px.bar(promo_code_counts, x="Promo Code Used", y="Count", color="Promo Code Used", title='Promo Code Used Distribution')
st.plotly_chart(fig)

# 5. Additional Information
# Location distribution
location_counts = filtered_df['Location'].value_counts().reset_index()
location_counts.columns = ['Location', 'Count']
fig = px.bar(location_counts, x="Location", y="Count", color="Location", title='Location Distribution')
st.plotly_chart(fig)

# Purchase Amount by Location
location_purchase = filtered_df.groupby('Location')['Purchase Amount (USD)'].sum().reset_index()
fig = px.bar(location_purchase, x="Location", y="Purchase Amount (USD)", color="Location", title='Total Purchase Amount by Location')
st.plotly_chart(fig)

# Color distribution
color_category_counts = filtered_df.groupby(['Category', 'Color']).size().reset_index(name='Count')
fig = px.bar(color_category_counts, x="Category", y="Count", color="Color", barmode="group", title='Color Distribution')
st.plotly_chart(fig)


# Size distribution
size_counts = filtered_df['Size'].value_counts().reset_index()
size_counts.columns = ['Size', 'Count']
fig = px.bar(size_counts, x="Size", y="Count", color="Size", title='Size Distribution')
st.plotly_chart(fig)

# Shipping Type distribution
shipping_type_counts = filtered_df['Shipping Type'].value_counts().reset_index()
shipping_type_counts.columns = ['Shipping Type', 'Count']
fig = px.pie(shipping_type_counts, values="Count", names="Shipping Type", title='Shipping Type Distribution')
st.plotly_chart(fig)

# Purchase Amount by Season
season_purchase = filtered_df.groupby('Season')['Purchase Amount (USD)'].sum().reset_index()
fig = px.bar(season_purchase, x="Season", y="Purchase Amount (USD)", color="Season", title='Purchase Amount by Season')
st.plotly_chart(fig)


# Top counts of Review Rating using pie chart
review_rating_counts = filtered_df['Review Rating'].value_counts().reset_index()
review_rating_counts.columns = ['Review Rating', 'Count']
fig = px.pie(review_rating_counts, values='Count', names='Review Rating', title='Top Counts of Review Rating')
st.plotly_chart(fig)

# Review Rating vs. Purchase Amount (USD)
fig = px.scatter(filtered_df, x="Review Rating", y="Purchase Amount (USD)", title='Review Rating vs Purchase Amount')
st.plotly_chart(fig)

# Previous Purchases distribution
fig = px.histogram(filtered_df, x='Previous Purchases', nbins=20, title='Previous Purchases Distribution', color_discrete_sequence=['orange'])
st.plotly_chart(fig)

# 7. Subscription Status and Discounts
# Subscription Status vs Discount Applied
fig = px.bar(filtered_df, x="Subscription Status", color="Discount Applied", title='Subscription Status vs Discount Applied')
st.plotly_chart(fig)

# Category vs Subscription Status
fig = px.bar(filtered_df, x="Category", color="Subscription Status", title='Category vs Subscription Status')
st.plotly_chart(fig)


# Average Purchase Amount by Age Group
filtered_df['Age Group'] = pd.cut(filtered_df['Age'], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=['<18', '18-25', '25-35', '35-45', '45-55', '55-65', '65+'])
avg_purchase_by_age = filtered_df.groupby('Age Group')['Purchase Amount (USD)'].mean().reset_index()
fig = px.line(avg_purchase_by_age, x="Age Group", y="Purchase Amount (USD)", title='Average Purchase Amount by Age Group')
st.plotly_chart(fig)
