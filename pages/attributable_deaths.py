import plotly.express as px
import streamlit as st
import pandas as pd
import plotly.graph_objs as go


# @st.cache
def app():
    # Air pollution Attributable Deaths dataset
    # st.set_page_config(page_title='Air pollution Attributable Deaths')

    st.markdown("## Air pollution Attributable Deaths Report ")
    st.markdown("### Number of Deaths")

    # Air pollution Attributable Deaths dataset
    df = pd.read_csv('data/AirPollutionAttributableDeaths.csv')
    st.write(df)
    # Renaming the Columns
    df.columns = ['Parent Location Code', 'Parent Location', 'Location', 'Year',
                  'Gender', 'Gender Code', 'Cause Type', 'Fact Value',
                  'Fact Value Low', 'Fact Value High', 'Value', 'Date Modified']

    # Filtering the parent location by continent
    parent_location = df['Parent Location'].unique().tolist()
    # Drop down menu
    continent = st.multiselect('Select the country', parent_location, ['Americas'])
    text_input = st.text_input("Enter a number between 0 and 3500", 'E.G: 45')
    # Selecting the DF by continent
    df = df[df['Parent Location'].isin(continent)]

    # avg_death = df[(df['Fact Value Low'] + df['Fact Value High'] / 2).is_integer()]
    # Creating the bar graph
    fig = px.bar(continent, x=df['Fact Value High'],
                 y=df['Cause Type'], color=df['Parent Location'], range_y=[0, 6],
                 range_x=[0, text_input])

    # Preparing layout
    # layout = px.Layout(title=' Air pollution Attributable Deaths Report', xaxis_title="Number of Deaths",
    #                    yaxis_title="Causes of Deaths", barmode='stack')
    fig.update_layout(width=1000)
    st.write(fig)
