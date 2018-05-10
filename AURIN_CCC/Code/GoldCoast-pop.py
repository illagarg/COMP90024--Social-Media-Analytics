import json
file_data = open("C:/Users/Chetan Garg/Desktop/GoldCoast-pop.json",'r')
obj = json.load(file_data)
data = obj["features"]
props = {"p_15_19_yrs": 0, "p_20_24_yrs": 0, "p_25_29_yrs": 0, "p_30_34_yrs": 0, "p_35_39_yrs": 0,
         "p_40_44_yrs": 0, "p_45_49_yrs": 0, "p_50_54_yrs": 0, "p_55_59_yrs": 0, "p_60_64_yrs": 0,
         "p_65_69_yrs": 0, "p_70_74_yrs": 0, "p_75_79_yrs": 0, "p_tot": 0 }
for feat in data:
	if "properties" in feat:
		if "p_15_19_yrs" in feat["properties"]: props["p_15_19_yrs"] += feat["properties"]["p_15_19_yrs"]
		if "p_20_24_yrs" in feat["properties"]: props["p_20_24_yrs"] += feat["properties"]["p_20_24_yrs"]
		if "p_25_29_yrs" in feat["properties"]: props["p_25_29_yrs"] += feat["properties"]["p_25_29_yrs"]
		if "p_30_34_yrs" in feat["properties"]: props["p_30_34_yrs"] += feat["properties"]["p_30_34_yrs"]
        if "p_35_39_yrs" in feat["properties"]: props["p_35_39_yrs"] += feat["properties"]["p_35_39_yrs"]
        if "p_40_44_yrs" in feat["properties"]: props["p_40_44_yrs"] += feat["properties"]["p_40_44_yrs"]
        if "p_45_49_yrs" in feat["properties"]: props["p_45_49_yrs"] += feat["properties"]["p_45_49_yrs"]
        if "p_50_54_yrs" in feat["properties"]: props["p_50_54_yrs"] += feat["properties"]["p_50_54_yrs"]
        if "p_55_59_yrs" in feat["properties"]: props["p_55_59_yrs"] += feat["properties"]["p_55_59_yrs"]
        if "p_60_64_yrs" in feat["properties"]: props["p_60_64_yrs"] += feat["properties"]["p_60_64_yrs"]
        if "p_65_69_yrs" in feat["properties"]: props["p_65_69_yrs"] += feat["properties"]["p_65_69_yrs"]
        if "p_70_74_yrs" in feat["properties"]: props["p_70_74_yrs"] += feat["properties"]["p_70_74_yrs"]
        if "p_75_79_yrs" in feat["properties"]: props["p_75_79_yrs"] += feat["properties"]["p_75_79_yrs"]
        if "p_tot" in feat["properties"]: props["p_tot"] += feat["properties"]["p_tot"]
       
print props
print type(props)
js = json.dumps(props)

# Open new json file if not exist it will create
fp = open('test.json', 'a')

# write to json file
fp.write(js)

# close the connection
fp.close()