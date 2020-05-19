import pandas as pd
import os
import datetime
import tkinter as tk
from tkinter import Tk,filedialog
import xlsxwriter


def backend(folderloc, mainfile):
    lst = os.listdir(folderloc)
    print('\n\n\n\n')
    print(lst)
    desktop = os.path.expanduser("~/Desktop")
    fmain = pd.ExcelFile(mainfile)  # Highlight
    for s in fmain.sheet_names:   # Traversing the sheets of the main file
        df_main = fmain.parse(s)

        # Adding the new columns into the main file
        df_main.insert(len(df_main.columns), "CGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "SGST/UTGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "IGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "CESS", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "TOTAL", df_main.shape[0] * [0])

        for file in lst:  # Traversing all the files except the main file.
            if (folderloc + "/" + str(file)) != mainfile:
                f = pd.ExcelFile(folderloc + "/" +  str(file)) # Highlight
                for sheet in f.sheet_names:
                    df = f.parse(sheet)
                    for i in range(len(df)):
                        sum = 0
                        for j in range(len(df_main)):  # Every file data is compared with this main file.
                            if str(df_main["GSTIN"][j]) == str(df["GSTIN"][i]):
                                #print("\n\ndf_main['GSTIN''][j] = ", df_main["GSTIN"][j] , '\ndf["GSTIN"][i] = ', df["GSTIN"][i])
                                s1 = str(df_main["CGST"][j])
                                m1 = str(df["CGST"][i])
                                sum = sum + int(s1.replace(',','')) + int(m1.replace(',',''))
                                df_main["CGST"][j] = int(s1.replace(',','')) + int(m1.replace(',',''))

                                s2 = str(df_main["SGST/UTGST"][j])
                                m2 = str(df["SGST/UTGST"][i])
                                sum = sum + int(s2.replace(',','')) + int(m2.replace(',',''))
                                df_main["SGST/UTGST"][j] = int(s2.replace(',','')) + int(m2.replace(',',''))

                                s3 = str(df_main["IGST"][j])
                                m3 = str(df["IGST"][i])
                                sum = sum + int(s3.replace(',','')) + int(m3.replace(',',''))
                                df_main["IGST"][j] = int(s3.replace(',','')) + int(m3.replace(',',''))

                                s4 = str(df_main["CESS"][j])
                                m4 = str(df["CESS"][i])
                                sum = sum + int(s4.replace(',','')) + int(m4.replace(',',''))
                                df_main["CESS"][j] = int(s4.replace(',','')) + int(m4.replace(',',''))

                                df_main["TOTAL"][j] = df_main["TOTAL"][j] + sum
        print('\n\n')
        print(df_main)

        # SAVING THE FINAL FILE
        Date = datetime.datetime.now()
        df_main.to_excel(desktop + "/GST_Report_" + str(Date.day) + "_" + str(Date.month) + "_" + str(Date.year) +".xlsx", 'Yearly Report')
