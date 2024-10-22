
# Shopping Trends Dashboard

This project is a Streamlit dashboard for visualizing shopping trends based on a dataset of customer purchases. 
The dashboard includes various demographic and purchase behavior visualizations with interactive filters.

## Steps to Launch the Project

1. **Clone or Download the Project**
   - Navigate to the directory where you want to store the project, then run the following command to clone the project:
     ```bash
     git clone <project-repository-url>
     ```

2. **Navigate to the Project Directory**
   - Once you have the project, use the `cd` command to go to the project directory:
     ```bash
     cd path_to_project_directory
     ```

3. **Install the Dependencies**
   - Install all required dependencies listed in the `requirements.txt` file using the following command:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Streamlit Application**
   - Launch the dashboard by running the Streamlit app with this command:
     ```bash
     streamlit run <your_file_name>.py
     ```

   - Replace `<your_file_name>` with the actual Python filename of your Streamlit application.

5. **Access the Dashboard**
   - The Streamlit application will open in your web browser. You can also access it by navigating to `http://localhost:8501` in your browser.


## Libraries Used:
- **Streamlit**: For creating the web-based dashboard.
- **Pandas**: For data manipulation and filtering.
- **Plotly**: For interactive visualizations (bar charts, line charts, pie charts, etc.).
- **Matplotlib**: For additional plotting.
- **Seaborn**: For statistical data visualization.
- **WordCloud**: For generating word clouds.
- **NumPy**: For numerical operations.

## Dataset:
The dataset `shopping_trends.csv` includes customer purchase data such as age, gender, purchase amount, location, payment methods, product preferences, etc.

### Code Explanation:

### 1. Importing Libraries:
```python
import streamlit as st
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image
```
These are the required libraries for the dashboard:
- **Streamlit** is used for creating the app.
- **Pandas** is used to manipulate the dataset.
- **NumPy** is used for numerical operations.
- **Plotly** is used for creating the visualizations.
- **Matplotlib** and **Seaborn** are for data visualization.

### 2. Loading the dataset:
```python
df = pd.read_csv(r"C:\Users\gaura\Downloads\python practice\Project\Dashboard\shopping_trends.csv")
df.sample(5)
```
The dataset is loaded using `pd.read_csv`, and `df.sample(5)` prints 5 random samples for inspection.

### 3. Sidebar Filters:
The dashboard includes various filters to allow users to interactively filter data and see specific visualizations.

#### 3.1 Filter by Age Range:
```python
age_range = st.sidebar.slider('Select Age Range', int(df['Age'].min()), int(df['Age'].max()), (18, 55))
```
This creates a slider in the sidebar for selecting an age range to filter the data.

#### 3.2 Filter by Gender:
```python
gender_options = st.sidebar.multiselect('Select Gender', options=df['Gender'].unique(), default=df['Gender'].unique())
```
This filter allows users to select one or more genders from the dataset.

#### 3.3 Filter by Location:
```python
location_options = st.sidebar.multiselect('Select Location', options=df['Location'].unique(), default=df['Location'].unique())
```
This allows users to select specific locations.

#### 3.4 Filter by Category:
```python
category_options = st.sidebar.multiselect('Select Category', options=df['Category'].unique(), default=df['Category'].unique())
```
This filter allows users to select product categories.

#### 3.5 Filter by Subscription Status:
```python
subscription_options = st.sidebar.multiselect('Select Subscription Status', options=df['Subscription Status'].unique(), default=df['Subscription Status'].unique())
```
This lets users filter by the subscription status of the customers.

#### 3.6 Filter by Season:
```python
season_options = st.sidebar.multiselect('Select Season', options=df['Season'].unique(), default=df['Season'].unique())
```
Users can filter the data based on the season of purchase.

#### 3.7 Filter by Payment Method:
```python
payment_method_options = st.sidebar.multiselect('Select Preferred Payment Method', options=df['Preferred Payment Method'].unique(), default=df['Preferred Payment Method'].unique())
```
This allows filtering by payment methods like credit card, PayPal, etc.

#### 3.8 Filter by Size:
```python
size_options = st.sidebar.multiselect('Select Size', options=df['Size'].unique(), default=df['Size'].unique())
```
The user can filter the data by the sizes of products purchased.

### 4. Applying Filters to the Data:
```python
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
```
This filters the original dataframe `df` based on the selections made in the sidebar.

### 5. Visualizations:

#### 5.1 Gender Distribution:
```python
gender_counts = filtered_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']
fig = px.bar(gender_counts, x="Gender", y="Count", color="Gender", title='Gender Distribution')
st.plotly_chart(fig)
```
This creates a bar chart showing the distribution of genders in the filtered data.

#### 5.2 Purchase Amount by Age and Gender:
```python
fig = px.bar(filtered_df, x="Age", y="Purchase Amount (USD)", color="Gender", title='Purchase Amount (USD) by Age and Gender')
st.plotly_chart(fig)
```
This bar chart shows purchase amounts segmented by age and gender.

#### 5.3 Purchase Amount by Category:
```python
fig = px.pie(filtered_df, values='Purchase Amount (USD)', names='Category', title='Purchase Amount (USD) by Category')
st.plotly_chart(fig)
```
This pie chart shows the breakdown of purchase amounts by product category.

#### 5.4 Other Visualizations:
Similar blocks of code are used to create histograms, pie charts, and bar charts to display purchase behavior, payment methods, discounts applied, review ratings, and more.

### 6. Average Purchase Amount by Age Group:
```python
filtered_df['Age Group'] = pd.cut(filtered_df['Age'], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=['<18', '18-25', '25-35', '35-45', '45-55', '55-65', '65+'])
avg_purchase_by_age = filtered_df.groupby('Age Group')['Purchase Amount (USD)'].mean().reset_index()
fig = px.line(avg_purchase_by_age, x="Age Group", y="Purchase Amount (USD)", title='Average Purchase Amount by Age Group')
st.plotly_chart(fig)
```

### `pd.cut()`

The `pd.cut()` function in pandas is used to divide a range of numbers into smaller groups or categories. This makes it easier to look at and understand data.

**Example:**

```python
age_groups = pd.cut(df['Age'], bins=[0, 18, 35, 55, 100], labels=['<18', '18-35', '35-55', '55+'])
```

This code groups customers into age categories and shows the average purchase amount for each group using a line chart.

## Summary:

This Streamlit app provides a comprehensive dashboard for analyzing shopping trends based on customer data. The user can filter by demographics, preferences, and purchase details, and view interactive visualizations. The filters allow for dynamic changes in the data and update visualizations in real-time. It is useful for retail businesses and analysts to understand customer behavior and optimize marketing strategies.
