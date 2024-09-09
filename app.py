import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import dash_ag_grid as dag

# Initialize the Dash app with the Zephyr theme from Bootswatch
app = dash.Dash(__name__, external_stylesheets=['https://bootswatch.com/5/zephyr/bootstrap.min.css'])

import requests
import pandas as pd
from io import BytesIO

# URL of the Excel file
url = 'https://github.com/OBAUDE95/DataAnalysis-Competition/raw/main/Jijicars.xlsx'

# Send a GET request to download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the downloaded content into a BytesIO object
    file = BytesIO(response.content)

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file).drop("Unnamed: 0",axis=1)

    # Display the first few rows of the DataFrame
    #print(df.head())
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
def convert(x):
    return int(x.replace("₦","").replace(",",""))
df['Price'] = df['Price'].apply(convert)

# Calculate summary statistics
total_cars = len(df)
total_titles = df['Title'].nunique()
total_categories = df['Type'].nunique()

# Shorten values for clarity
def shorten_number(num):
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)

# Shortened values
short_total_cars = shorten_number(total_cars)
short_total_titles = shorten_number(total_titles)
short_total_categories = shorten_number(total_categories)

# Calculate mean values by 'Title'
mean_df = df.groupby('Title').mean().reset_index()

# Create a bar plot for top 5 titles (ascending mean price)
top_5 = mean_df.sort_values(by='Price', ascending=True).head(5)
fig_top = go.Figure()
fig_top.add_trace(go.Bar(
    y=top_5['Title'],
    x=top_5['Price'],
    orientation='h',
    marker=dict(color='royalblue', line=dict(color='black', width=1.5)),
    text=top_5['Price'].round(2),
    textposition='outside',
    textfont=dict(size=12, color='black'),
))
fig_top.update_layout(
    title={
        'text': 'Top 5 Titles by Mean Price',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': 'rgb(0, 0, 0)'}
    },
    xaxis_title='Mean Price',
    yaxis_title='Title',
    plot_bgcolor='white',
    paper_bgcolor='rgba(243, 243, 243, 0.5)',
    margin=dict(l=50, r=50, t=80, b=50)
)

# Create a bar plot for bottom 5 titles (descending mean price)
bottom_5 = mean_df.sort_values(by='Price', ascending=False).head(5)
fig_bottom = go.Figure()
fig_bottom.add_trace(go.Bar(
    y=bottom_5['Title'],
    x=bottom_5['Price'],
    orientation='h',
    marker=dict(color='tomato', line=dict(color='black', width=1.5)),
    text=bottom_5['Price'].round(2),
    textposition='outside',
    textfont=dict(size=12, color='black'),
))
fig_bottom.update_layout(
    title={
        'text': 'Bottom 5 Titles by Mean Price',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'color': 'rgb(0, 0, 0)'}
    },
    xaxis_title='Mean Price',
    yaxis_title='Title',
    plot_bgcolor='white',
    paper_bgcolor='rgba(243, 243, 243, 0.5)',
    margin=dict(l=50, r=50, t=80, b=50)
)

# Create a pie chart using Plotly Graph Objects
fig_pie = go.Figure(data=[go.Pie(labels=df['Title'].value_counts().index, values=df['Title'].value_counts().values)])
fig_pie.update_layout(title_text='Distribution of Car Titles')

# Create a box plot for price distribution by car type
types = df['Type'].unique()
fig_box = go.Figure()
for t in types:
    fig_box.add_trace(go.Box(
        y=df[df['Type'] == t]['Price'],
        name=t,  # Use the type name as the boxplot label
    ))

fig_box.update_layout(
    title={
        'text': "Price Distribution by Type",
        'x': 0.5,  # Center the title
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Type",
    yaxis_title="Price",
    boxmode='group',  # Group the boxes together
    plot_bgcolor='white',
    paper_bgcolor='rgba(243, 243, 243, 0.5)',
    margin=dict(l=50, r=50, t=80, b=50)
)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Car Title Analysis Dashboard", style={'text-align': 'center'}),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody("Total Cars"),
            dbc.CardFooter(short_total_cars, id='total-cars')
        ], className="border border-primary rounded p-3"), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody("Total Car Titles"),
            dbc.CardFooter(short_total_titles, id='total-titles')
        ], className="border border-primary rounded p-3"), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody("Total Categories"),
            dbc.CardFooter(short_total_categories, id='total-categories')
        ], className="border border-primary rounded p-3"), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody("Foreign | Local used"),
            dbc.CardFooter(f"2400 | 1600", id='total-used')
        ], className="border border-primary rounded p-3"), width=3)
    ], className="mb-4 justify-content-around"),

    dbc.Row([
        dbc.Col(
            dcc.Graph(figure=fig_top),
            width=6
        ),
        dbc.Col(
            dcc.Graph(figure=fig_bottom),
            width=6
        )
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(
            dcc.Graph(figure=fig_box),
            width=12
        )
    ], className="mb-4"),

    html.Div([
        html.P("Comment:Local used car prices are generally cheaper compared to foreign imports, as illustrated by the box plot above.")
    ], style={'text-align': 'center', 'font-size': '16px', 'margin': '20px'}),

    dbc.Row([
        dbc.Col(
            dcc.Graph(figure=fig_pie),
            width=12
        )
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H3("Detailed Car Data Table", style={'text-align': 'center', 'margin-bottom': '20px'}),
                dag.AgGrid(
                    id='data-table',
                    columnDefs=[{'headerName': col, 'field': col, 'filter': True} for col in df.columns],
                    rowData=df.to_dict('records'),
                    defaultColDef={'sortable': True, 'filter': True, 'resizable': True},  # Add sorting, filtering, resizing
                    style={'height': '400px', 'width': '100%'},
                    className="ag-theme-alpine"
                )
            ]),
            width=12
        )
    ], className="mb-4")

], className="container")



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
