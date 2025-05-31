import pandas as pd
zillow_data = pd.read_csv('County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month (1).csv', delimiter=',')
PA_data = zillow_data[zillow_data['State'] == 'PA']
new_cols = ['RegionName']
for col in PA_data.columns:
    
    if col[0:2]=='20':
        year = int(col[:4])
        month = int(col[5]+col[6])
        if year == 2017:
            if month>=7:
                new_cols+=[col]
        elif year>2017:
            new_cols+=[col]
PA_data = PA_data[new_cols]
PA_data.to_excel('PA_home_values.xlsx', index=False)