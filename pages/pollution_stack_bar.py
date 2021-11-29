import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
import sys
import plotly.express as px
import streamlit as st
import pandas as pd

# @st.cache
def app():

    st.markdown("## Pollution Comparison by Country ")
    st.markdown("### Mexico 2011 vs Sweden 2012 ")


# Country1Name = sys.argv[1]
# Country1Year = sys.argv[2]
# Country1Urban = 0.0
# Country1Rural = 0.0
#
# Country2Name = sys.argv[3]
# Country2Year = sys.argv[4]
# Country2Urban = 0.0
# Country2Rural = 0.0
#
# filename = 'Pollution.csv'
#
# # row 7 = location
# # row 9 = year
# # row 12 = Area type
# # row 29 = total pollution for that area type
#
# with open(filename, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row in datareader:
#         if Country1Name in row:
#             if Country1Year in row:
#                 if row[12] == 'Rural':
#                     Country1Rural = float(row[29].split(" ", 1)[0])
#                 elif row[12] == 'Urban':
#                     Country1Urban = float(row[29].split(" ", 1)[0])
#         if Country2Name in row:
#             if Country2Year in row:
#                 if row[12] == 'Rural':
#                     Country2Rural = float(row[29].split(" ", 1)[0])
#                 elif row[12] == 'Urban':
#                     Country2Urban = float(row[29].split(" ", 1)[0])
#
#
# labels = [Country1Name, Country2Name]
# UrbanTotal = [Country1Urban, Country2Urban]
# RuralTotal = [Country1Rural, Country2Rural]
# width = 0.35       # the width of the bars: can also be len(x) sequence
#
# fig, ax = plt.subplots()
#
# ax.bar(labels, UrbanTotal, width, label='Urban Fine Particulate Matter')
# ax.bar(labels, RuralTotal, width, bottom=UrbanTotal,
#        label='Rural Fine Particulate Matter')
#
# ax.set_ylabel('Pollution Level \n (Annual mean concentration of particulate matter of less than \n 2.5 microns of diameter (PM2.5) [ug/m3])')
# ax.set_title('Pollution of {0} ({1}) vs {2} ({3})'.format(Country1Name, Country1Year, Country2Name, Country2Year))
# ax.legend()
#
# ax.text(0, (Country1Urban / 2), Country1Urban)
# ax.text(0, (Country1Urban + ( Country1Rural / 2)), Country1Rural)
# ax.text(0, (Country1Urban + Country1Rural), "Total: {0}".format(Country1Rural + Country1Urban))
#
# ax.text(1, (Country2Urban / 2), Country2Urban)
# ax.text(1, (Country2Urban + ( Country2Rural / 2)), Country2Rural)
# ax.text(1, (Country2Urban + Country2Rural), "Total: {0}".format(Country2Rural + Country2Urban))
# plt.legend(bbox_to_anchor=(.75, -.02), bbox_transform=ax.transAxes)
# plt.show()