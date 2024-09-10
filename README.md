# DataAnalysis-Competition

## Project Title:
**Comprehensive Car Pricing and Sales Insights Dashboard**

## Project Description:
This dashboard provides a detailed analysis of car pricing and sales data. It leverages various visualizations to offer insights into car prices, distribution by type, and comparisons between foreign and local vehicles. The dashboard includes:

1. **Overview of Car Data:**
   - Displays total number of cars, car models, and car conditions.
   - Uses summary statistics to provide an overview of the dataset.

2. **Top 5 Most Expensive Cars:**
   - A bar plot showing the top 5 most expensive car models based on mean price.

3. **Top 5 Most Affordable Cars:**
   - A bar plot illustrating the top 5 most affordable car models based on mean price.

4. **Price Distribution by Car Type:**
   - A box plot showing the distribution of car prices by type, highlighting differences between foreign and local cars.

5. **Comparison of Foreign vs Local Cars:**
   - A bar plot comparing the counts of foreign and local cars.

6. **Detailed Car Data Table:**
   - An interactive table displaying detailed information about each car in the dataset, including car condition, title, and price.

### Data Preprocessing:
1. **Data Loading:**
   - The data is sourced from an Excel file available [here](https://github.com/OBAUDE95/DataAnalysis-Competition/raw/main/Jijicars.xlsx).
   - The file is loaded into a pandas DataFrame after being downloaded.

2. **Data Cleaning:**
   - Removed the unnecessary "Unnamed: 0" column.
   - Converted the "Price" column from a string format with currency symbols to integer values for numerical analysis.

3. **Data Transformation:**
   - Applied a function to convert price values from Nigerian Naira format to integers.
   - Calculated summary statistics including the total number of cars, unique car titles, and car conditions.
   - Grouped data by car title to compute mean prices for the top and bottom 5 car models.

### Features:
- Interactive and responsive design with Dash and Plotly.
- Use of Bootstrap components for a clean and modern look.
- Detailed visualizations including bar plots, box plots, and interactive data tables.
- Customizable and user-friendly interface for exploring car pricing and sales data.

### Author:
Obaude Ayodeji Michael

