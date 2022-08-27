import json
import pandas as pd

data_file = open("data\\yelp_academic_dataset_business.json", encoding='utf-8')
business_df = pd.DataFrame(data_file)
# print(business_df)
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

print(dict(list(restaurant_dict.items())[:2]))


data_file = open("data\\yelp_academic_dataset_review.json", encoding='utf-8')
review_df = pd.DataFrame(data_file)
data_file.close()
restaurant_revs = {}
for z in review_df.to_numpy():
    # try:
    review_data = json.loads(z[0])
    #handles categories with null
    if review_data['business_id'] and review_data['business_id'] in restaurant_dict.keys():
            # restaurant_revs.update(review_data['business_id'])
            
            
            print('True')
            quit()
    else: 
        pass





