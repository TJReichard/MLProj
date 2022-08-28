from cProfile import label
import pandas as pd

data_file = open("reviews_stars.csv", encoding='utf-8')
labeled_data = pd.DataFrame(data_file)
# print(business_df)
data_file.close()

print(labeled_data.head(5).values)