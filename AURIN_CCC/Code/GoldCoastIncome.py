import json
file_data = open("C:/Users/Chetan Garg/Desktop/GoldCoast-income.json",'r')
obj = json.load(file_data)
data = obj["features"]
props = {"Negative_Nil_income_Tot": 0, "HI_1_199_Tot": 0, "HI_200_299_Tot": 0, "HI_300_399_Tot": 0, "HI_400_599_Tot": 0,
         "HI_600_799_Tot": 0, "HI_800_999_Tot": 0, "HI_1000_1249_Tot": 0, "HI_1250_1499_Tot": 0, "HI_1500_1999_Tot": 0,
         "HI_2000_2499_Tot": 0, "HI_2500_2999_Tot": 0, "HI_3000_3499_Tot": 0, "HI_3500_3999_Tot": 0, "HI_4000_more_Tot": 0, "Tot_Tot": 0 }
for feat in data:
	if "properties" in feat:
		if "Negative_Nil_income_Tot" in feat["properties"]: props["Negative_Nil_income_Tot"] += feat["properties"]["Negative_Nil_income_Tot"]
		if "HI_1_199_Tot" in feat["properties"]: props["HI_1_199_Tot"] += feat["properties"]["HI_1_199_Tot"]
		if "HI_200_299_Tot" in feat["properties"]: props["HI_200_299_Tot"] += feat["properties"]["HI_200_299_Tot"]
		if "HI_300_399_Tot" in feat["properties"]: props["HI_300_399_Tot"] += feat["properties"]["HI_300_399_Tot"]
        if "HI_400_599_Tot" in feat["properties"]: props["HI_400_599_Tot"] += feat["properties"]["HI_400_599_Tot"]
        if "HI_600_799_Tot" in feat["properties"]: props["HI_600_799_Tot"] += feat["properties"]["HI_600_799_Tot"]
        if "HI_800_999_Tot" in feat["properties"]: props["HI_800_999_Tot"] += feat["properties"]["HI_800_999_Tot"]
        if "HI_1000_1249_Tot" in feat["properties"]: props["HI_1000_1249_Tot"] += feat["properties"]["HI_1000_1249_Tot"]
        if "HI_1250_1499_Tot" in feat["properties"]: props["HI_1250_1499_Tot"] += feat["properties"]["HI_1250_1499_Tot"]
        if "HI_1500_1999_Tot" in feat["properties"]: props["HI_1500_1999_Tot"] += feat["properties"]["HI_1500_1999_Tot"]
        if "HI_2000_2499_Tot" in feat["properties"]: props["HI_2000_2499_Tot"] += feat["properties"]["HI_2000_2499_Tot"]
        if "HI_2500_2999_Tot" in feat["properties"]: props["HI_2500_2999_Tot"] += feat["properties"]["HI_2500_2999_Tot"]
        if "HI_3000_3499_Tot" in feat["properties"]: props["HI_3000_3499_Tot"] += feat["properties"]["HI_3000_3499_Tot"]
        if "HI_3500_3999_Tot" in feat["properties"]: props["HI_3500_3999_Tot"] += feat["properties"]["HI_3500_3999_Tot"]
        if "HI_4000_more_Tot" in feat["properties"]: props["HI_4000_more_Tot"] += feat["properties"]["HI_4000_more_Tot"]
        if "Tot_Tot" in feat["properties"]: props["Tot_Tot"] += feat["properties"]["Tot_Tot"]
       
print props
print type(props)
js = json.dumps(props)

# Open new json file if not exist it will create
fp = open('test.json', 'a')

# write to json file
fp.write(js)

# close the connection
fp.close()