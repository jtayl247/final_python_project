import streamlit as st
import numpy as np
from PIL import Image

# Custom imports
from multipage import MultiPage
from pages import home, attributable_deaths, pollution_stack_bar, pollution_by_country

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Create an instance of the app
app = MultiPage()

# Title of the main page
# display = Image.open('Logo.png')
# display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.columns(2)
# col1.image(display, width = 400)
col2.title("Air Pollution App")
# Add all your application here
app.add_page("Home", home.app)
app.add_page("Attributable Deaths", attributable_deaths.app)
app.add_page("Pollution", pollution_stack_bar.app)
app.add_page("Pollution by Country", pollution_by_country.app)

# The main app
app.run()
