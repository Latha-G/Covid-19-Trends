

















# Extracting required columns 

Covid_US_data = raw_US_data[["City/State",
                             "Latitude","Longitude",
                             "1/22/20", "1/29/20","2/5/20","2/12/20",
                             "2/19/20", "2/26/20", "3/4/20", "3/11/20",
                             "3/18/20", "3/25/20", "4/2/20"
                             
                            ]]


# Sorting the DataFrame by latest case count

Covid_US_data = Covid_US_data.sort_values("4/2/20", ascending = False)

Covid_US_data.head(60)


# Splitting City/State column in to separate City and State columns

city_states = Covid_US_data["City/State"]

cities = []
states = []

# Lopp through City/State Column

for citystate in city_states:
    x = citystate.split(",",2)
    cities.append(x[0])
    states.append(x[1])

# Add cities to City Clumn & states to "State" column 

Covid_US_data["City"] = cities
Covid_US_data["State"] = states


