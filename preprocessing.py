import pandas as pd
import json

data_path = 'data/cache/store_steamspy/apps.json'

with open(data_path, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

app_data = pd.DataFrame(raw_data['apps'])

app_data.drop('supported_languages',axis=1,inplace=True)

app_data.drop('recommendations',axis=1, inplace=True)

def get(element,key):
    try:
        return element[key]
    except:
        return None

app_data['price'] = app_data['price_overview'].apply(lambda x: get(x,'initial'))
app_data.drop('price_overview',axis=1,inplace=True)

app_data['released'] = app_data['release_date'].apply(lambda x: not get(x,'coming_soon'))
app_data['release_date'] = app_data['release_date'].apply(lambda x: get(x, 'date'))


app_data.drop('genres',axis=1,inplace=True)

def get_owners(string):
    bounds = [int(item.replace(',','')) for item in string.split(' .. ')]
    return int((bounds[0]+bounds[1])/2)

app_data['median_owners'] = app_data['owners'].apply(get_owners)

app_data['categories'] = app_data['categories'].apply(lambda x: [{'id': 2, 'description': 'Single-player'}] if x is None else x)

app_data['categories'] = app_data['categories'].apply(lambda tags: [tag['description'] for tag in tags])

app_data.dropna(subset=['languages','developers'],inplace=True)

app_data['price'] = app_data.apply((lambda x: 0 if x['is_free']==True else x['price']), axis=1)

app_data.to_csv('data/prod/app_data.csv')