import pandas as pd
import os
import xlsxwriter


def Backend_Cal(lst):
    fmain = pd.ExcelFile("Excel_Files/" + str(lst[0]))  # Highlight
    for s in fmain.sheet_names:   # Traversing the sheets of the main file
        df_main = fmain.parse(s)

        # Adding the new columns into the main file
        df_main.insert(len(df_main.columns), "CGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "SGST/UTGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "IGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "CESS", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "TOTAL", df_main.shape[0] * [0])


        for file in lst[1:]:  # Traversing all the files except the main file.
            f = pd.ExcelFile("Excel_Files/" + str(file)) # Highlight
            for sheet in f.sheet_names:
                df = f.parse(sheet)
                for i in range(len(df)):
                    sum = 0
                    for j in range(len(df_main)):
                        if str(df_main["GSTIN"][j]) == str(df["GSTIN"][i]):
                            print("\n\ndf_main['GSTIN''][j] = ", df_main["GSTIN"][j] , '\ndf["GSTIN"][i] = ', df["GSTIN"][i])
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
        df_main.to_excel("Excel_Files/demo.xlsx", 'sheet1')

# Temperory function call with demo excel files.
l = ['Full_demo.xlsx', 'April_demo.xlsx']
Backend_Cal(l)


"""
    * You will get the location of the MAIN FILE from the frontend. In string format.
      Eg. "C:\KSHITIJ R. SANGAR\Desktop\Kshitij Projects\Python projects\GST_miniproject\Excel_Files\Full_demo.xlsx"
    * From this file location, you have to separate out it's folder location.
    * And, from this folder, you will read the all the file names.
    * Now you have to write a logic so that our program will read
        all the file names from that folder, and does not repeats itself.

    #Method to read all the file names from a folder
    import 
    l = os.listdir('/')
"""
