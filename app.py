import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['About','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1,col2 = st.columns(2)

    with col1:
        city = db.fetch_city_names()
        source = st.selectbox('Source',sorted(city))

    with col2:
        city = db.fetch_city_names()
        destination = st.selectbox('Destination',sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif user_option == 'Analytics':
    st.title('Analytics')
    airline,frequency = db.fetch_Airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)


    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.header("Bar chart")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.header("Line graph")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


else:
    st.header('Flights Data Analysis using Python and SQL')
    st.subheader('Project Description:')
    st.write('In an era of global connectivity, understanding and visualizing flight data is essential for both travel enthusiasts and industry professionals. The "Flights Data Analysis using Python and SQL" project offers a comprehensive and user-friendly platform for exploring, analyzing, and gaining insights from a vast repository of flight data.')
    st.subheader('Project Purpose:')
    st.write('The primary goal of this project is to empower users to access and analyze flight data effortlessly. Users can easily check available flights by selecting their source and destination, providing real-time information on flight options.')
    st.markdown("""
    ### Key Features:
    - ##### Flight Search:
     Users can search for flights by specifying their source and destination. The system provides up-to-date flight details, including airline, departure time, and duration.
    - ##### Data Analysis:
     The project employs SQL queries to fetch and aggregate data stored in a MySQL database. Users can visualize the data in three distinct ways:
    - Pie Chart: Explore airline frequencies to gain insights into the market share of different carriers.
    - Bar Chart: Analyze the busiest airports based on the number of flights, offering valuable information for travelers and airport operators.
    - Line Graph: Observe the trends in flight frequency over time, helping users make informed decisions about travel dates.
    
    - ##### Interactive Visualization:
     Leveraging Plotly's graph_objects and express libraries, the project ensures that users can interact with and customize their data visualizations for a richer analysis experience.
    """)
    st.markdown("""
    ### Technologies Used:
    - Python for data analysis and visualization.
    - SQL for querying and managing the database.
    - MySQL Workbench for database management.
    - Plotly graph_objects and express for interactive data visualization.
    """)
