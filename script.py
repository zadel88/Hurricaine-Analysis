# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']
# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def dmg(x):
  new = []
  for value in x:
    if value.endswith('M'):
      M = value[:-1]
      new.append(float(M)*conversion['M'])
    elif value.endswith('B'):
      B = value[:-1]
      new.append(float(B)*conversion['B'])
    else:
      new.append(value)
  return new
new = dmg(damages)

#print(dmg(damages))
# 2 
# Create a Table
hurricaines = {}
def names_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths):
  for i in range(len(names)):
    hurricaines[names[i]]={'Name':names[i],
                          'Months':months[i],
                          'Years':years[i],
                          'Max Winds':max_sustained_winds[i],
                          'Areas Affected':areas_affected[i],
                          'Damage':new[i],
                          'Deaths':deaths[i]}
  return hurricaines
# Create and view the hurricanes dictionary
hurricaines = names_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths)
#print dictionary by name
#print(hurricaines)
# 3
# Organizing by Year
def year_dictionary(hurricaines):
  year_sort = {}
  for name in hurricaines:
    year = hurricaines[name]['Years']
    names = hurricaines[name]
    if year not in year_sort:
      year_sort[year] = [names]
    else:
      year_sort[year].append(names)
  return year_sort
year_sort = year_dictionary(hurricaines)
# create a new dictionary of hurricanes with year and key
#print(year_sort)
# 4
# Counting Damaged Areas
def affected_areas(hurricaines):
  areas = {}
  for name in hurricaines:
    for area in hurricaines[name]['Areas Affected']:
      if area not in areas:
        areas[area] = 1
      else:
        areas[area] += 1
  return areas
areas = affected_areas(hurricaines)

# create dictionary of areas to store the number of hurricanes involved in
#print(areas)
# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def max_hit(areas):
  max_area = 'Central America'
  max_count = 0
  for area in areas:
    if max_count < areas[area]:
      max_count = areas[area]
      max_area = area
  return max_area, max_count
max_area, max_count = max_hit(areas)
#print(max_area, max_count)
# 6
# Calculating the Deadliest Hurricane
def mortality(hurricaines):
  max_deaths = 'Cuba I'
  max_count = 0
  for area in hurricaines:
    if hurricaines[area]['Deaths'] > max_count:
      max_deaths = area
      max_count = hurricaines[area]['Deaths']
  return max_deaths, max_count
max_deaths, max_count = mortality(hurricaines)
# find highest mortality hurricane and the number of deaths
#print(max_deaths, max_count)
# 7
# Rating Hurricanes by Mortality
def cat_by_mortality(hurricaines):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricanes_by_mortality ={0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for cane in hurricaines:
    num_deaths = hurricaines[cane]['Deaths']
    if num_deaths == mortality_scale[0]: 
      hurricanes_by_mortality[0].append(hurricaines[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricaines[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricaines[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricaines[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricaines[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricaines[cane])
  return hurricanes_by_mortality

hurricanes_by_mortality = cat_by_mortality(hurricaines)

#print(hurricanes_by_mortality)
 
# write your greatest damage function here:
def greatest_damage(hurricanes):
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == "Damages not recorded":
      pass
    elif hurricanes[cane]['Damage'] > max_damage:
      max_damage_cane = cane
      max_damage = hurricanes[cane]['Damage']
  return  max_damage_cane, max_damage
max_damage_cane, max_damage = greatest_damage(hurricaines)
#print(max_damage_cane, max_damage)   
# write your catgeorize by damage function here:

def categorise_by_damage(dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    damage_scale_hurricane = {'No Damage': [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for name in dict:
        if dict[name]['Damage'] == 'Damages not recorded':
            damage_scale_hurricane['No Damage'].append(name)
        elif damage_scale[0] < dict[name]['Damage'] <= damage_scale[1]:
            damage_scale_hurricane[1].append(name)
        elif damage_scale[1] < dict[name]['Damage'] <= damage_scale[2]:
            damage_scale_hurricane[2].append(name)
        elif damage_scale[2] < dict[name]['Damage'] <= damage_scale[3]:
            damage_scale_hurricane[3].append(name)
        elif damage_scale[3] < dict[name]['Damage'] <= damage_scale[4]:
            damage_scale_hurricane[4].append(name)
        else:
            damage_scale_hurricane[5].append(name)
    return damage_scale_hurricane

print(categorise_by_damage(hurricaines))