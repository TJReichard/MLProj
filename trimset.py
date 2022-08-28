import json
import pandas as pd
import csv
import time
from datetime import datetime  

start = time.time()
date_time = datetime.fromtimestamp(start)
print('startet at: ', date_time)

print('Starting JSON conversion')
data_file = open("data\\yelp_academic_dataset_business.json", encoding='utf-8')
business_df = pd.DataFrame(data_file)
# print(business_df)
data_file.close()
end = time.time()
print('business file loaded, time elapsed: ', end - start)
restaurant_dict= {}
# rest_idx = 0
idx = 0

for i in business_df.to_numpy():
    idx +=1
    try:
        business_data = json.loads(i[0])
        #handles categories with null
        if business_data['categories'] and 'categories' in business_data.keys() and 'Restaurants' in business_data['categories']:
            restaurant_dict.update({business_data['business_id']: 'Restaurants'})   
            # rest_idx += 1
    except Exception as a: print(idx, i, a)
end = time.time()
print('Restaurants in dict, time elapsed: ', end - start)

# print('Number of Restaurants: ', rest_idx)
# print('Number of Items: ', idx)

# print(dict(list(restaurant_dict.items())[:2]))


data_file = open("data\\yelp_academic_dataset_review.json", encoding='utf-8')
review_df = pd.DataFrame(data_file)
data_file.close()
restaurant_revs = []
end = time.time()
print('review file loaded, time elapsed: ', end - start)

for z in review_df.to_numpy():
    # try:
    review_data = json.loads(z[0])
    #handles categories with null
    if review_data['business_id'] and review_data['business_id'] in restaurant_dict.keys():
        review_text = review_data['text'].casefold().replace('\n', ' ')
        
        if review_data['stars'] >2:
            restaurant_revs.append({'text':review_text, 'label': 1})                
        else:     
            restaurant_revs.append({'text':review_text, 'label': 0})
    else: 
        pass


# print(restaurant_revs[:5])


end = time.time()
print('review data labeled, time elapsed: ', end - start)


csv_field_names = ['text', 'label']
  
print('Starting CSV creation')  
with open('reviews_labeled.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = csv_field_names, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(restaurant_revs)
# print(type(restaurant_revs))    
end = time.time()
print('csv done, time elapsed: ', end - start)