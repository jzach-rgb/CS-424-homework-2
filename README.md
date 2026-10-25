# CS-424-homework-2

## Task 1

For this assignment, I will continue analyzing Cor Coffee's sales data collected through Square's Point of Sale (POS) system. My original goal was to investigate how customers customize their drinks and how different modifiers relate to sales.

After reviewing the dataset, I decided to focus on three questions:

1) How do customer customization preferences differ across drink types?

2) How do drink and modifier preferences change throughout the day?

3) Which combinations of drinks, milk types, and flavored syrups occur most frequently?

The dataset contains 2,676 sales records collected across 19 weekdays between September 8 and October 2, 2026.  During my first check, I identified 256 records with missing modifiers, several records with quantities greater than one, and two records with negative quantities. These issues will need to be considered during data preparation to avoid misleading comparisons. Since customer identifiers aren't available, I will focus on product-level and temporal relationships instead of repeat-customer behavior. My next step is to adapt my previous ETL process to this dataset, validate the derived attributes, and explore different visualization approaches.



## Task 2

To prepare the sales data for visualization, I created a Python cleaning script using Pandas to clean the original CSV and create additional attributes.
I began by selecting the columns relevant to my questions and then converted dates and times into appropriate data types and removed currency symbols from the monetary columns so they could be used in numerical calculations. Next, I standardized inconsistent product labels and extracted several attributes from the Modifiers Applied column. These included drink temperature, milk type, syrup, caffeine preference, sweetness, and service method. I also derived the hour and weekday of each sale for temporal analysis.

One challenge I had was differrntiating missing information from actual customer preferences. For example, some beverage records did not explicitly specify a temperature or milk type. For the milk's with nothing specified, I defulted all to whole since the baristas tend to not select anything for whole milk prefrence since there is no charge but for temperture prefrence, rather than assigning default values, I kept these as missing to avoid potentially misleading results. I also marked drink-specific attributes as inapplicable for food and merchandise. The resulting dataset has everything I need to investigate drink customization, temporal patterns, and relationships between different modifiers.


## Task 3

<img width="1620" height="972" alt="01_top_drinks" src="https://github.com/user-attachments/assets/97a0fd3f-c727-4a0d-b6d0-911d7eff7efd" />

I first examined the distribution of beverage types and found that lattes represented the largest portion of the dataset, with 1,116 records. This gave me a potential problem with comparing raw modifier frequencies, since popular drinks naturally contribute more observations. As a result, I explored normalized comparisons of milk preferences across different beverages.

<img width="1800" height="990" alt="02_milk_by_drink" src="https://github.com/user-attachments/assets/5216df53-1fe9-4b75-a87a-968e8ce2a9ab" />

I examined milk preferences across five drink types using a normalized stacked bar chart. Whole milk was the most common across all drinks, while oat milk was the most popular alternative, especially for Matcha Lattes. Coffee had the highest proportion of whole milk at approximately 80%, while Matcha Lattes had the lowest at around 58%. Using percentages instead of raw counts made comparing drinks easier, although missing milk information may affect the results.

<img width="1620" height="954" alt="03_syrup_frequency" src="https://github.com/user-attachments/assets/9368a91c-8197-45cd-bb0b-19f2e3415697" />

Then, I investigated syrup preferences. Cinnamon Roll and Vanilla were the most commonly recorded flavors, appearing in 611 and 484 beverage records, respectively. Some records contained multiple flavors, so I separated these entries when counting individual syrup selections. I also recognized that these preferences may be influenced by the limited collection period.

<img width="1620" height="900" alt="04_hourly_volume" src="https://github.com/user-attachments/assets/29be0cab-5b69-4614-9435-a909da0b2ece" />

Then I looked at temporal patterns. Beverage records peaked at 10 AM, with 461 observations, followed by a smaller increase around noon. This suggests that it could be helpfult to explore hourly purchasing patterns, especially when comparing different types of beverages and modifiers.

<img width="1800" height="936" alt="05_temperature_completeness" src="https://github.com/user-attachments/assets/efdf43bb-f30b-455b-abad-146c4aafbded" />

Finally, I investigated temperature preferences and discovered that approximately 32% of beverage records lacked an explicitly recorded temperature. This made certain hot-versus-iced comparisons potentially misleading. I decided to preserve these missing values rather than make assumptions about customer selections.

Overall, the exploratory analysis helped narrow my focus toward three potential visualization directions: normalized modifier comparisons, temporal purchasing patterns, and relationships between drink types and modifiers. It also highlighted the importance of accounting for missing information and differences in drink popularity when interpreting results.

## Task 4




## Task 4: Implement Visualization Alternatives

### Milk Preferences by Drink Type

I created a normalized stacked bar chart to compare milk preferences across five drink types. The chart uses bars as marks, with length representing percentages and color distinguishing milk types. Whole milk was the most common across all drinks, while oat milk was the most popular alternative, especially for Matcha Lattes. I decided to keep this approach because it makes comparisons easy, although the number of milk categories makes some smaller proportions difficult to distinguish.

<img width="1700" height="850" alt="A_milk_composition" src="https://github.com/user-attachments/assets/becfd0a5-1f7e-408f-98a1-0c828091e2c2" />

### Oat Milk Preferences by Hour

I created a heatmap to investigate how oat milk preferences vary by drink type and time of day. The visualization uses rectangular cells as marks, with position representing drink type and hour, and color intensity representing the percentage of oat milk selections. Matcha Lattes showed a relatively high oat milk percentage at 2 PM (43%), while Chai Lattes varied considerably throughout the day. I would modify this approach by considering sample sizes because some hourly percentages may be based on relatively few observations.

<img width="1530" height="646" alt="B_oat_hour_heatmap" src="https://github.com/user-attachments/assets/2f31514a-ef51-489b-a978-02eaa845e159" />

### Hourly Drink Purchasing Patterns

I created a line chart to compare when Lattes, Matcha Lattes, and Chai Lattes were purchased throughout the day. The chart uses lines and points as marks, with horizontal position representing time, vertical position representing the percentage of each drink's sales, and color distinguishing the drink types. Lattes peaked at 10 AM, while Chai Lattes showed a higher proportion of purchases at 9 AM, noon, and 3 PM. I decided to keep this visualization because it makes temporal trends easy to compare, although it does not explain the causes of those patterns.

<img width="1800" height="900" alt="C_drink_hourly_lines" src="https://github.com/user-attachments/assets/72b50c83-478a-4ae7-8d04-50084305a52a" />


All three visualizations revealed different aspects of customer behavior. Direction A was most effective for comparing milk preferences, Direction B helped identify hourly differences in oat milk selection, and Direction C made overall purchasing patterns easier to interpret. I would continue refining Direction B because it combines drink customization with temporal patterns, although I would need to address potentially misleading percentages caused by small sample sizes.



## Task 5

I considered adding interactive filtering and multiple coordinated views to explore drink preferences more closely. But I decided to keep the current visualizations static because the limited number of categories and time intervals makes the comparisons relatively easy to interpret without interaction. The three visualizations provide complementary views of customer behavior, covering milk preferences, hourly customization patterns, and purchasing trends.

## Task 6

<img width="1800" height="756" alt="iteration_1_hourly_with_counts" src="https://github.com/user-attachments/assets/25c58325-a0db-4ddd-9b23-648c9df1a16e" />

The original heatmap displayed oat milk percentages without showing how many records contributed to each value. This made percentages from smaller samples potentially misleading. I added sample sizes to each cell so readers could better evaluate the comparisons.


<img width="1800" height="756" alt="iteration_2_grouped_hours" src="https://github.com/user-attachments/assets/5143329b-6caa-4ea8-8101-4e735944a26e" />

Although the first iteration improved transparency, some hourly percentages still fluctuated significantly, especially for Chai Lattes. I grouped the hours into three broader periods to reduce these fluctuations and make the patterns easier to interpret. This revealed that Chai Lattes had a higher proportion of oat milk selections during the morning, while Matcha Lattes showed a higher proportion in the afternoon.


I decided to keep the second iteration because it provides clearer comparisons with larger sample sizes, although grouping hours sacrifices some temporal detail.


## Task 7 

I selected the grouped-time oat milk heatmap as my current design because it provides a clearer comparison of milk preferences across drinks and time periods. The visualization uses rectangular cells as marks, with position representing drink type and time period, and color intensity representing the percentage of oat milk selections. Compared to the original heatmap, this version includes sample sizes and groups hours together to reduce fluctuations from smaller samples. Although grouping hours sacrifices some detail, it makes the overall patterns easier to interpret. For Assignment 3, I would evaluate whether users can accurately compare percentages and understand how sample sizes affect their interpretation.
