import requests, json, os
import xlrd
from xlutils.copy import copy


def transaction():
    headers = {"content-type": "application/json", "x-access-token": "5443b693E341cb0ab695Xb8"}
    url = "https://safe-payy.herokuapp.com/api/v1/safepay/querypayment/initiated"
    try:
        #Make API call
        r = requests.get(url=url, headers=headers)
        print(f"Status code: {r.status_code}")  #Print status code
        response = r.json()

        if not response.get("status"):
            return response.get("message")
        
        #Record needed to be saved in excel
        record = response.get("data")     #This record is a list dictionaries.

        FOLDER = '/home/megzy/Desktop/IDL_PROJECTS/sptransfer_safePAY/app/static/SAFEPAY_STATEMENT'
        filename = "transaction.xlsx" 

        if filename in os.listdir(FOLDER):

            file='{}/{}'.format(FOLDER, filename)
            print(file)
            try:
                book = xlrd.open_workbook(file,encoding_override="cp1251")  
            except:
                book = xlrd.open_workbook(file)
            # sheet1 = book.sheet_by_index(0) #sheet1
            # rx = sheet1.nrows #number of rows filled with data.

            #xlutils is for updating the table later
            wb = copy(book)
            sheet1 = wb.get_sheet(0) #open sheet 1
            
            count = 0
            rx = 0
            

            for elem in record:
                print(elem)
                count += 1
                rx += 1
                print(rx)
                initiating_date = elem.get("initiating_date")
                paymentref = elem.get("paymentref")
                merchant_id = elem.get("merchant_id")
                business_name = elem.get("business_name")
                product_amount = elem.get("product_amount")
                    
                sheet1.write(rx,0,initiating_date)
                sheet1.write(rx,1,paymentref)
                sheet1.write(rx,2,merchant_id)
                sheet1.write(rx,3,business_name)
                sheet1.write(rx,4,product_amount)
                continue    #continue to For-loop

            #save the updated table
            wb.save(file)
            return "All data successfully recorded in spreadsheet."
        else:
            return "Excel file not in Folder"
    except Exception as e:
        return f"Encountered error: {e}"


    
