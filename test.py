import json
import pandas as pd
data =[{'review_id': 'KU_O5udG6zpxOg-VcAEodg', 'text': "If you decide to eat here, just be aware it is going to take about 2 hours from beginning to end. We have tried it multiple times, because I want to like it! I have been to it's other locations in NJ and never had a bad experience. \n\nThe food is good, but it takes a very long time to come out. The waitstaff is very young, but usually pleasant. We have just had too many experiences where we spent way too long waiting. We usually opt for another diner or restaurant on the weekends, in order to be done quicker.", 'label': 1}, {'review_id': 'saUsX_uimxRlCVr67Z4Jig', 'text': 'Family diner. Had the buffet. Eclectic assortment: a large chicken leg, fried jalapeño, tamale, two rolled grape leaves, fresh melon. All good. Lots of Mexican choices there. Also has a menu with breakfast served all day long. Friendly, attentive staff. Good place for a casual relaxed meal with no expectations. Next to the Clarion Hotel.', 'label': 1}, {'review_id': 'AqPFMleE6RsU23_auESxiA', 'text': "Wow!  Yummy, different,  delicious.   Our favorite is the lamb curry and korma.  With 10 different kinds of naan!!!  Don't let the outside deter you (because we almost changed our minds)...go in and try something new!   You'll be glad you did!", 'label': 1}, {'review_id': 'Sx8TMOWLNuJBWer-0pcmoA', 'text': "Cute interior and owner (?) gave us tour of upcoming patio/rooftop area which will be great on beautiful days like today. Cheese curds were very good and very filling. Really like that sandwiches come w salad, esp after eating too many curds! Had the onion, gruyere, tomato sandwich. Wasn't too much cheese which I liked. Needed something else...pepper jelly maybe. Would like to see more menu options added such as salads w fun cheeses. Lots of beer and wine as well as limited cocktails. Next time I will try one of the draft wines.", 'label': 1}, {'review_id': 'JrIxlS1TzJ-iCu79ul40cQ', 'text': "I am a long term frequent customer of this establishment. I just went in to order take out (3 apps) and was told they're too busy to do it. Really? The place is maybe half full at best. Does your dick reach your ass? Yes? Go fuck yourself! I'm a frequent customer AND great tipper. Glad that Kanella just opened. NEVER going back to dmitris!", 'label': 0}]

# data_file = open("data\\yelp_academic_dataset_review.json", encoding='utf-8')
# review_df = pd.DataFrame(data_file)
# data_file.close()

# print(review_df.head(1).values)

import csv
  
employee_info = ['review_id', 'text', 'label']
  
  
with open('test4.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = employee_info, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(data)


# for i in data:
#     y = json.loads(i)
# print(y.keys())