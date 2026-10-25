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

