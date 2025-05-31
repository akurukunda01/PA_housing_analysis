import pandas as pd
colspecs = [
    (0, 2),      # 1-2:   FIPS State code
    (3, 6),      # 4-6:   FIPS county code

    (7, 15),     # 8-15:  Estimate of people all ages in poverty
    (16, 24),    # 17-24: 90% CI lower bound estimate people all ages
    (25, 33),    # 26-33: 90% CI upper bound estimate people all ages
    (34, 38),    # 35-38: Estimated percent people all ages in poverty
    (39, 43),    # 40-43: 90% CI lower bound percent people all ages
    (44, 48),    # 45-48: 90% CI upper bound percent people all ages

    (49, 57),    # 50-57: Estimate of people age 0-17 in poverty
    (58, 66),    # 59-66: 90% CI lower bound estimate people 0-17
    (67, 75),    # 68-75: 90% CI upper bound estimate people 0-17
    (76, 80),    # 77-80: Estimated percent people 0-17 in poverty
    (81, 85),    # 82-85: 90% CI lower bound percent people 0-17
    (86, 90),    # 87-90: 90% CI upper bound percent people 0-17

    (91, 99),    # 92-99: Estimate of related children age 5-17 in poverty
    (100,108),   # 101-108: 90% CI lower bound related children 5-17
    (109,117),   # 110-117: 90% CI upper bound related children 5-17
    (118,122),   # 119-122: Estimated percent related children 5-17
    (123,127),   # 124-127: 90% CI lower bound percent related children 5-17
    (128,132),   # 129-132: 90% CI upper bound percent related children 5-17

    (133,139),   # 134-139: Estimate median household income
    (140,146),   # 141-146: 90% CI lower bound median household income
    (147,153),   # 148-153: 90% CI upper bound median household income

    # Columns 154-191 are blank for county level, skip or include if needed
    
    (154,161),   # 155-161: Estimate people under age 5 in poverty
    (162,169),   # 163-169: 90% CI lower bound people under 5
    (170,177),   # 171-177: 90% CI upper bound people under 5
    (178,182),   # 179-182: Estimated percent people under 5 in poverty
    (183,187),   # 184-187: 90% CI lower bound percent people under 5
    (188,192),   # 189-192: 90% CI upper bound percent people under 5

    (193,238),   # 194-238: State or county name (string)
    (239,241),   # 240-241: Two-letter postal state abbreviation
    (242,264),   # 243-264: File name and date tag
]
colnames = [
    'FIPS_State', 'FIPS_County',
    'Poverty_All_Ages_Estimate', 'Poverty_All_Ages_CI_Lower', 'Poverty_All_Ages_CI_Upper',
    'Poverty_All_Ages_Pct_Estimate', 'Poverty_All_Ages_Pct_CI_Lower', 'Poverty_All_Ages_Pct_CI_Upper',

    'Poverty_0_17_Estimate', 'Poverty_0_17_CI_Lower', 'Poverty_0_17_CI_Upper',
    'Poverty_0_17_Pct_Estimate', 'Poverty_0_17_Pct_CI_Lower', 'Poverty_0_17_Pct_CI_Upper',

    'Related_Children_5_17_Estimate', 'Related_Children_5_17_CI_Lower', 'Related_Children_5_17_CI_Upper',
    'Related_Children_5_17_Pct_Estimate', 'Related_Children_5_17_Pct_CI_Lower', 'Related_Children_5_17_Pct_CI_Upper',

    'Median_Household_Income_Estimate', 'Median_Household_Income_CI_Lower', 'Median_Household_Income_CI_Upper',

    'Poverty_Under_5_Estimate', 'Poverty_Under_5_CI_Lower', 'Poverty_Under_5_CI_Upper',
    'Poverty_Under_5_Pct_Estimate', 'Poverty_Under_5_Pct_CI_Lower', 'Poverty_Under_5_Pct_CI_Upper',

    'County', 'State_Abbr', 'File_Tag'
]

data2023 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2023/2023-state-and-county/est23-pa.txt',colspecs=colspecs,header=None)
data2022 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2022/2022-state-and-county/est22-pa.txt',colspecs=colspecs,header=None)
data2021 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2021/2021-state-and-county/est21-pa.txt',colspecs=colspecs,header=None)
data2020 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2020/2020-state-and-county/est20-pa.txt',colspecs=colspecs,header=None)
data2019 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2019/2019-state-and-county/est19-pa.txt',colspecs=colspecs,header=None)
data2018 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2018/2018-state-and-county/est18-pa.txt',colspecs=colspecs,header=None)
data2017 = pd.read_fwf('https://www2.census.gov/programs-surveys/saipe/datasets/2017/2017-state-and-county/est17-pa.txt',colspecs=colspecs,header=None)
data2023.columns, data2023['Year'] = colnames,2023
data2022.columns, data2022['Year'] = colnames, 2022
data2021.columns, data2021['Year']= colnames, 2021
data2020.columns, data2020['Year'] = colnames, 2020
data2019.columns, data2019['Year'] = colnames, 2019
data2018.columns, data2018['Year'] = colnames, 2018
data2017.columns, data2017['Year'] = colnames, 2017
data = pd.concat([data2023,data2022,data2021,data2020,data2019,data2018,data2017],ignore_index=True)
income_data = data.pivot_table(index = 'County', columns = 'Year', values='Median_Household_Income_Estimate')
income_data.to_excel('household_income_estimate_county_pennsylvania.xlsx', index =False)
