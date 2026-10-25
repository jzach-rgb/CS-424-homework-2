import pandas as pd

raw = pd.read_csv('sanitized_raw_data.csv')

df = raw[['Date', 'Time', 'Category', 'Item', 'Qty', 'Count', 'Modifiers Applied',
          'Gross Sales', 'Discounts', 'Net Sales']].copy()

df['Date'] = pd.to_datetime(df['Date'], errors='raise')
df['Time'] = pd.to_datetime(
    df['Time'], format='%H:%M:%S', errors='raise').dt.time
for col in ['Gross Sales', 'Discounts', 'Net Sales']:
    df[col] = pd.to_numeric(df[col].str.replace(
        r'[$,]', '', regex=True), errors='raise')
df['Item'] = df['Item'].replace(
    {'LiaP Cookie': 'Cookie', 'Matcha lemonade': 'Matcha Lemonade'})
df['Category'] = df['Category'].replace(
    {'Teas': 'Tea-Based Drinks', 'Coffee Drinks': 'Coffee-Based Drinks'})

is_drink = ~df['Category'].isin(['Food', 'Merch'])


def tokens(value):
    return [p.strip().casefold() for p in value.split(',') if p.strip()] if isinstance(value, str) else []


parsed = df['Modifiers Applied'].map(tokens)


def choice(parts, possibilities):
    for key, value in possibilities:
        if key in parts:
            return value
    return pd.NA



temp_keys = [('iced', 'Iced'), ('hot', 'Hot')]
milk_keys = [('oat', 'Oat'), ('almond', 'Almond'), ('soy', 'Soy'), ('coconut', 'Coconut'),
             ('half&half (breve)', 'Half & Half'), ('half&half', 'Half & Half'), ('whole', 'Whole')]
service_keys = [('to go', 'To go'), ('here', 'Here')]
caffeine_keys = [('decaf', 'Decaf'), ('half-caf', 'Half-Caf'),
                 ('cafe', 'Caffeinated')]
sweet_keys = [('sweet', 'Sweet'), ('regular', 'Regular')]
syrups = {'vanilla', 'lavender', 'hazelnut', 'strawberry', 'rose', 'ube', 'pistachio',
          'peppermint', 'gingerbread', 'pumpkin', 'caramel apple', 'cinnamon roll',
          'blueberry', 'apple', 'sugar cookie', 'ganache', 'miel', 'cor de hanoi',
          "s'mores"}

for col, keys in [('Temp', temp_keys), ('Milk', milk_keys), ('Service', service_keys),
                  ('Caffeine', caffeine_keys), ('Sweetness', sweet_keys)]:
    df[col] = parsed.map(lambda p: choice(p, keys)).astype('string')
    df.loc[~is_drink, col] = pd.NA


def extract_syrups(parts):
    found = sorted(set(parts) & syrups)
    return ', '.join(s.title() for s in found) if found else pd.NA


df['Syrup'] = parsed.map(extract_syrups).astype('string')
df.loc[~is_drink, 'Syrup'] = pd.NA
df['Is_Drink'] = is_drink

df['Hour'] = df['Time'].map(lambda t: t.hour)
df['Weekday'] = df['Date'].dt.day_name()
df['Has_Modifier_Text'] = df['Modifiers Applied'].notna()


df.to_csv("clean_data", index=False)

