# CS-424-homework-2

## Task 1

For this assignment, I will continue analyzing Cor Coffee's sales data collected through Square's Point of Sale (POS) system. My original goal was to investigate how customers customize their drinks and how different modifiers relate to sales.

After reviewing the dataset, I decided to focus on three questions:

1) How do customer customization preferences differ across drink types?

2) How do drink and modifier preferences change throughout the day?

3) Which combinations of drinks, milk types, and flavored syrups occur most frequently?

The dataset contains 2,676 sales records collected across 19 weekdays between September 8 and October 2, 2026.  During my first check, I identified 256 records with missing modifiers, several records with quantities greater than one, and two records with negative quantities. These issues will need to be considered during data preparation to avoid misleading comparisons. Since customer identifiers aren't available, I will focus on product-level and temporal relationships instead of repeat-customer behavior. My next step is to adapt my previous ETL process to this dataset, validate the derived attributes, and explore different visualization approaches.
