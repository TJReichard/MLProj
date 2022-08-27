import json
import pandas as pd

data_file = open("data\\yelp_academic_dataset_business.json", encoding='utf-8')
business_df = pd.DataFrame(data_file)
print(business_df)
data_file.close()
restaurant_dict= {}
# rest_idx = 0
idx = 0

for i in business_df.to_numpy():
    idx +=1
    try:
        business_data = json.loads(i[0])
        #handles categories with null
        if business_data['categories'] and 'categories' in business_data.keys() and 'Restaurants' in business_data['categories']:
            restaurant_dict.update({business_data['business_id']: {'categories': business_data['categories']}})   
            # rest_idx += 1
    except Exception as a: print(idx, i, a)


# print('Number of Restaurants: ', rest_idx)
# print('Number of Items: ', idx)

# print(list(restaurant_dict.items())[:10])


data_file = open("data\\yelp_academic_dataset_review.json", encoding='utf-8')
review_df = pd.DataFrame(data_file)
data_file.close()
for i in review_df.to_numpy():
    try:
        review_data = json.loads(i[0])
        print(review_data)
        quit()
        #handles categories with null
        if business_data['categories'] and 'categories' in business_data.keys() and 'Restaurants' in business_data['categories']:
            restaurant_dict.update({business_data['business_id']: {'categories': business_data['categories']}})   
            # rest_idx += 1
    except Exception as a: print(idx, i, a)

print('review keys ', review_data.keys())



