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
    st.markdown("### Select the Country")
    # # Get country name to plot data as system arg
    # Country1Name = sys.argv[1]
    #
    # # dataset name
    # filename = 'Pollution.csv'
    #
    # yr2011 = 0
    # yr2012 = 0
    # yr2013 = 0
    # yr2014 = 0
    # yr2015 = 0
    # yr2016 = 0
    #
    # yr2011Urban = 0
    # yr2012Urban = 0
    # yr2013Urban = 0
    # yr2014Urban = 0
    # yr2015Urban = 0
    # yr2016Urban = 0
    #
    # yr2011Rural = 0
    # yr2012Rural = 0
    # yr2013Rural = 0
    # yr2014Rural = 0
    # yr2015Rural = 0
    # yr2016Rural = 0
    #
    # # When reading the csv here are what the rows contain
    # # row 7 = Country
    # # row 9 = year
    # # row 12 = Area type [Urban, Rural, Total]
    # # row 29 = total pollution for that area type
    # with open(filename, 'r') as csvfile:
    #     datareader = csv.reader(csvfile)
    #     for row in datareader:
    #         if Country1Name in row:
    #             if row[9] == '2011':
    #                 if row[12] == 'Total':
    #                     yr2011 = float(row[29].split(" ", 1)[0])
    #                     print(yr2011)
    #                 elif row[12] == 'Urban':
    #                     yr2011Urban = float(row[29].split(" ", 1)[0])
    #                     print(yr2011Urban)
    #                 elif row[12] == 'Rural':
    #                     yr2011Rural = float(row[29].split(" ", 1)[0])
    #                     print(yr2011Rural)
    #             elif row[9] == '2012':
    #                 if row[12] == 'Total':
    #                     yr2012 = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Urban':
    #                     yr2012Urban = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Rural':
    #                     yr2012Rural = float(row[29].split(" ", 1)[0])
    #             elif row[9] == '2013':
    #                 if row[12] == 'Total':
    #                     yr2013 = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Urban':
    #                     yr2013Urban = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Rural':
    #                     yr2013Rural = float(row[29].split(" ", 1)[0])
    #             elif row[9] == '2014':
    #                 if row[12] == 'Total':
    #                     yr2014 = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Urban':
    #                     yr2014Urban = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Rural':
    #                     yr2014Rural = float(row[29].split(" ", 1)[0])
    #             elif row[9] == '2015':
    #                 if row[12] == 'Total':
    #                     yr2015 = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Urban':
    #                     yr2015Urban = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Rural':
    #                     yr2015Rural = float(row[29].split(" ", 1)[0])
    #             elif row[9] == '2016':
    #                 if row[12] == 'Total':
    #                     yr2016 = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Urban':
    #                     yr2016Urban = float(row[29].split(" ", 1)[0])
    #                 elif row[12] == 'Rural':
    #                     yr2016Rural = float(row[29].split(" ", 1)[0])
    #
    # # on chart: x is year -> y is pollution level
    # # plot details
    # x = (2011, 2012, 2013, 2014, 2015, 2016)
    # y1 = (yr2011, yr2012, yr2013, yr2014, yr2015, yr2016)
    # y2 = (yr2011Rural, yr2012Rural, yr2013Rural, yr2014Rural, yr2015Rural, yr2016Rural)
    # y3 = (yr2011Urban, yr2012Urban, yr2013Urban, yr2014Urban, yr2015Urban, yr2016Urban)
    # plt.plot(x, y1, color='blue', marker='o', label="Combined Avg")
    # plt.plot(x, y2, color='red', marker='o', label="Rural")
    # plt.plot(x, y3, color='green', marker='o', label="Urban")
    # plt.title("Pollution levels of " + Country1Name + " from 2011 - 2016")
    # plt.xlabel("Year")
    # plt.ylabel("Pollution level")
    # plt.grid(True)
    # leg = plt.legend(loc='upper right')
    # plt.rcParams["figure.autolayout"] = True
    # plt.show()