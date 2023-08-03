import json, requests, openpyxl

wb = openpyxl.load_workbook("/Users/ganegodagerodrigo/Desktop/VetsinTech/python3-course/week-4/main_company_inventory.xlsx")
ws = wb["inventory_list"]
wt = wb["order_list"]

# if ws.colC > ws.col
# Product ID	Vendor	Product Name	Order Amount	Unit Price	Total Price

Product_ID = ws["A"]
Vendor = ws["G"]
Product_Name = ws["B"]
Order_Amount = ws["F"]
colD = ws["D"]

for index, cell in enumerate(colD, 0):
    if cell.value == True:
        wt.cell(row = index+1, column = 1, value = Product_ID[index].value)
        wt.cell(row = index+1, column = 2, value = Vendor[index].value)
        wt.cell(row = index+1, column = 3, value = Product_Name[index].value)
        wt.cell(row = index+1, column = 4, value = Order_Amount[index].value)

def remove_whitespace(col_letter):
    col_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4}
    thisCol = wt["{}".format(col_letter)]
    clean_list = []
    #getting rid of white space in non compliant tab 
    for cell in thisCol:
        if cell.value:
            clean_list.append(cell.value)
    #getting rid of white space in non compliant tab 

    wt.delete_cols(col_dictionary["{}".format(col_letter)])
    wt.insert_cols(col_dictionary["{}".format(col_letter)])
    for different_index, value in enumerate(clean_list, 1):
        wt.cell(row = different_index, column = int("{}".format(col_dictionary["{}".format(col_letter)])), value = clean_list[different_index-1])

remove_whitespace("A")
remove_whitespace("B")
remove_whitespace("C")
remove_whitespace("D")

wb.save("main_company_inventory.xlsx")

base_url = "https://vit-py-api.herokuapp.com/"

api_vendor = wt["B"]
api_prodID = wt["A"]
api_ordAmount = wt["D"]

for index, this_call in enumerate(api_vendor, 0):
    try:
        if api_vendor[index+1].value:
            # print(base_url+"{}".format(api_vendor[index+1].value))
       
            response = (requests.get(base_url+"{}".format(api_vendor[index+1].value)+"/{}".format(api_prodID[index+1].value))).json()
            wt.cell(row = index+2, column = 5, value = response["unit_price"])
            wt.cell(row = index+2, column = 6, value = (response["unit_price"]*api_ordAmount[index+1].value))
            print(response["unit_price"])
        else:
            break
    except:
        break

wt["E40"] = "Total Price"
wt["F40"] = "=SUM(F2:F39)"

wb.save("main_company_inventory.xlsx")