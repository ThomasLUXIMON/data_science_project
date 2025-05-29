import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

data1_csv_content = """City,Minimum_temperature,Maximum_temperature,Rainfall,Sunshine_duration
Ajaccio,12.3,22.5,515.8,2854.5
Bastia,12.6,22.0,921.0,2613.6
Beauvais,7.7,16.1,864.7,1430.3
Biarritz,11.5,19.2,1819.4,1812.7
Bordeaux,10.6,19.3,1016.8,1871.5
Brest,8.9,15.5,1437.2,1363.2
Caen,8.4,16.1,749.4,1633.6
Chartres,8.1,16.3,833.5,1496.3
Clermont-Ferrand,8.4,18.2,715.2,1841.0
Colmar,7.8,17.7,700.6,1771.2
Dijon,8.1,16.9,881.3,1633.7
Lyon,9.4,18.6,989.3,1838.3
Melun,8.4,16.7,998.7,1511.8
Montelimar,10.4,19.5,1030.9,2362.3
Montpellier,11.5,21.1,579.7,2596.2
Nantes,9.2,17.1,1023.3,1674.0
Nice,14.2,20.7,1017.6,2731.8
Orleans,8.3,16.5,828.0,1545.0
Paris,10.1,17.0,901.1,1509.0
Perpignan,12.9,21.9,517.9,2467.3
Poitiers,8.7,17.5,808.5,1694.0
Quimper,9.2,16.1,1287.2,1562.2
Strasbourg,8.4,17.3,796.6,1633.7
Toulouse,10.5,19.6,606.6,1971.8
Tours,9.1,17.1,841.4,1608.7
"""
df1 = pd.read_csv(io.StringIO(data1_csv_content))

# Prepare a list of dictionaries to store results for CSV
output_data_list = []

# --- q1 ---
num_cities_initial = df1['City'].nunique()
output_data_list.append({'Question': 'q1a', 'Answer1': num_cities_initial, 'Answer2': '', 'Answer3': ''})

missing_per_city = df1.isnull().any(axis=1)
cities_with_missing_data = df1[missing_per_city]
num_cities_affected_by_missing = cities_with_missing_data['City'].nunique()
output_data_list.append({'Question': 'q1b', 'Answer1': num_cities_affected_by_missing, 'Answer2': '', 'Answer3': ''})

if num_cities_affected_by_missing > 0:
    df1.dropna(inplace=True)

df1_indexed = df1.set_index('City')

# --- q2 ---
city_lowest_min_temp = df1_indexed['Minimum_temperature'].idxmin()
value_lowest_min_temp = df1_indexed['Minimum_temperature'].min()
output_data_list.append({'Question': 'q2a', 'Answer1': city_lowest_min_temp, 'Answer2': value_lowest_min_temp, 'Answer3': ''})

city_highest_min_temp = df1_indexed['Minimum_temperature'].idxmax()
value_highest_min_temp = df1_indexed['Minimum_temperature'].max()
output_data_list.append({'Question': 'q2b', 'Answer1': city_highest_min_temp, 'Answer2': value_highest_min_temp, 'Answer3': ''})

city_lowest_max_temp = df1_indexed['Maximum_temperature'].idxmin()
value_lowest_max_temp = df1_indexed['Maximum_temperature'].min()
output_data_list.append({'Question': 'q2c', 'Answer1': city_lowest_max_temp, 'Answer2': value_lowest_max_temp, 'Answer3': ''})

city_highest_max_temp = df1_indexed['Maximum_temperature'].idxmax()
value_highest_max_temp = df1_indexed['Maximum_temperature'].max()
output_data_list.append({'Question': 'q2d', 'Answer1': city_highest_max_temp, 'Answer2': value_highest_max_temp, 'Answer3': ''})

city_lowest_rainfall = df1_indexed['Rainfall'].idxmin()
value_lowest_rainfall = df1_indexed['Rainfall'].min()
output_data_list.append({'Question': 'q2e', 'Answer1': city_lowest_rainfall, 'Answer2': value_lowest_rainfall, 'Answer3': ''})

city_highest_rainfall = df1_indexed['Rainfall'].idxmax()
value_highest_rainfall = df1_indexed['Rainfall'].max()
output_data_list.append({'Question': 'q2f', 'Answer1': city_highest_rainfall, 'Answer2': value_highest_rainfall, 'Answer3': ''})

city_lowest_sunshine = df1_indexed['Sunshine_duration'].idxmin()
value_lowest_sunshine = df1_indexed['Sunshine_duration'].min()
output_data_list.append({'Question': 'q2g', 'Answer1': city_lowest_sunshine, 'Answer2': value_lowest_sunshine, 'Answer3': ''})

city_highest_sunshine = df1_indexed['Sunshine_duration'].idxmax()
value_highest_sunshine = df1_indexed['Sunshine_duration'].max()
output_data_list.append({'Question': 'q2h', 'Answer1': city_highest_sunshine, 'Answer2': value_highest_sunshine, 'Answer3': ''})

# --- q3 ---
variances = df1_indexed.var(ddof=1) # sample variance
output_data_list.append({'Question': 'q3a', 'Answer1': round(variances['Minimum_temperature'], 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q3b', 'Answer1': round(variances['Maximum_temperature'], 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q3c', 'Answer1': round(variances['Rainfall'], 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q3d', 'Answer1': round(variances['Sunshine_duration'], 4), 'Answer2': '', 'Answer3': ''})

# --- q4 ---
lowest_variance_var = variances.idxmin()
mean_lvv = df1_indexed[lowest_variance_var].mean()
median_lvv = df1_indexed[lowest_variance_var].median()
std_lvv = df1_indexed[lowest_variance_var].std(ddof=1)
output_data_list.append({'Question': 'q4a', 'Answer1': round(mean_lvv, 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q4b', 'Answer1': round(median_lvv, 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q4c', 'Answer1': round(std_lvv, 4), 'Answer2': '', 'Answer3': ''})

# Plot for q4
plt.figure(figsize=(8, 6))
sns.histplot(df1_indexed[lowest_variance_var], kde=True)
plt.title(f'Histogram of {lowest_variance_var} (Lowest Variance)')
plt.xlabel(lowest_variance_var)
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
print(f"Comment q4: The variable with the lowest variance is {lowest_variance_var}. Mean: {mean_lvv:.4f}, Median: {median_lvv:.4f}, Std Dev: {std_lvv:.4f}.")

# --- q5 ---
highest_variance_var = variances.idxmax()
mean_hvv = df1_indexed[highest_variance_var].mean()
median_hvv = df1_indexed[highest_variance_var].median()
std_hvv = df1_indexed[highest_variance_var].std(ddof=1)
output_data_list.append({'Question': 'q5a', 'Answer1': round(mean_hvv, 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q5b', 'Answer1': round(median_hvv, 4), 'Answer2': '', 'Answer3': ''})
output_data_list.append({'Question': 'q5c', 'Answer1': round(std_hvv, 4), 'Answer2': '', 'Answer3': ''})

# Plot for q5
plt.figure(figsize=(8, 6))
sns.histplot(df1_indexed[highest_variance_var], kde=True)
plt.title(f'Histogram of {highest_variance_var} (Highest Variance)')
plt.xlabel(highest_variance_var)
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
print(f"Comment q5: The variable with the highest variance is {highest_variance_var}. Mean: {mean_hvv:.4f}, Median: {median_hvv:.4f}, Std Dev: {std_hvv:.4f}.")


# --- q6 ---
correlation_matrix_vars = df1_indexed.corr()
correlations_list = []
for col1 in correlation_matrix_vars.columns:
    for col2 in correlation_matrix_vars.columns:
        if col1 < col2:
            correlations_list.append(((col1, col2), correlation_matrix_vars.loc[col1, col2]))

sorted_correlations = sorted(correlations_list, key=lambda item: item[1])

# q6a: Most positively correlated variables
most_positive_pair_details = sorted_correlations[-1]
var1_mp, var2_mp = most_positive_pair_details[0]
corr_mp = most_positive_pair_details[1]
output_data_list.append({'Question': 'q6a', 
                         'Answer1': var1_mp, 
                         'Answer2': var2_mp, 
                         'Answer3': round(corr_mp, 2)})

# Plot for q6a
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df1_indexed, x=var1_mp, y=var2_mp)
for i in range(df1_indexed.shape[0]):
    plt.text(df1_indexed[var1_mp][i], df1_indexed[var2_mp][i], df1_indexed.index[i], fontsize=8)
plt.title(f'Most Positively Correlated: {var1_mp} vs {var2_mp} (Corr: {corr_mp:.2f})')
plt.xlabel(var1_mp)
plt.ylabel(var2_mp)
plt.grid(True)
plt.show()
print(f"Comment q6a: Most positively correlated variables are {var1_mp} and {var2_mp} with a correlation of {corr_mp:.2f}.")


# q6b: Most negatively correlated variables
most_negative_pair_details = sorted_correlations[0]
var1_mn, var2_mn = most_negative_pair_details[0]
corr_mn = most_negative_pair_details[1]
output_data_list.append({'Question': 'q6b', 
                         'Answer1': var1_mn, 
                         'Answer2': var2_mn, 
                         'Answer3': round(corr_mn, 2)})

# Plot for q6b
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df1_indexed, x=var1_mn, y=var2_mn)
for i in range(df1_indexed.shape[0]):
    plt.text(df1_indexed[var1_mn][i], df1_indexed[var2_mn][i], df1_indexed.index[i], fontsize=8)
plt.title(f'Most Negatively Correlated: {var1_mn} vs {var2_mn} (Corr: {corr_mn:.2f})')
plt.xlabel(var1_mn)
plt.ylabel(var2_mn)
plt.grid(True)
plt.show()
print(f"Comment q6b: Most negatively correlated variables are {var1_mn} and {var2_mn} with a correlation of {corr_mn:.2f}.")


# q6c: Least correlated variables (correlation value closest to 0)
least_correlated_pair_details = min(correlations_list, key=lambda item: abs(item[1]))
var1_lc, var2_lc = least_correlated_pair_details[0]
corr_lc = least_correlated_pair_details[1]
output_data_list.append({'Question': 'q6c', 
                         'Answer1': var1_lc, 
                         'Answer2': var2_lc, 
                         'Answer3': round(corr_lc, 2)})

# Plot for q6c
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df1_indexed, x=var1_lc, y=var2_lc)
for i in range(df1_indexed.shape[0]):
    plt.text(df1_indexed[var1_lc][i], df1_indexed[var2_lc][i], df1_indexed.index[i], fontsize=8)
plt.title(f'Least Correlated (closest to 0): {var1_lc} vs {var2_lc} (Corr: {corr_lc:.2f})')
plt.xlabel(var1_lc)
plt.ylabel(var2_lc)
plt.grid(True)
plt.show()
print(f"Comment q6c: Least correlated variables (closest to 0) are {var1_lc} and {var2_lc} with a correlation of {corr_lc:.2f}.")


# --- q7 ---
# Linear correlations between cities.
city_corr_matrix = df1_indexed.T.corr() # Transpose to have cities as rows for correlation
q7_comment_csv = "City correlation matrix (25x25) was computed. See plot for visualization. Not displayed in CSV due to size."
output_data_list.append({'Question': 'q7', 'Answer1': q7_comment_csv, 'Answer2': '', 'Answer3': ''})

# Plot for q7
plt.figure(figsize=(12, 10))
sns.heatmap(city_corr_matrix, annot=False, cmap='coolwarm', fmt=".2f") # annot=True can be too crowded for 25x25
plt.title('Correlation Matrix Between Cities')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()
print("Comment q7: The correlation matrix between cities (heatmap displayed) shows the pairwise linear correlations of weather profiles between cities.")


# Create the final DataFrame for CSV output
output_df = pd.DataFrame(output_data_list)
output_df = output_df[['Question', 'Answer1', 'Answer2', 'Answer3']]

# Generate CSV string output
final_csv_output = output_df.to_csv(index=False)

print("\n--- CSV Output ---")
print(final_csv_output)

