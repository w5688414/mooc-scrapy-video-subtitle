
import json
import pandas as pd

def read_json(json_path):
    with open(json_path,'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict

def output_to_csv(list_data,csv_name):
    column_name = ['url']
    xml_df = pd.DataFrame(list_data, columns=column_name)
    print(xml_df.shape)
    xml_df=xml_df.drop_duplicates()
    print(xml_df.shape)
    xml_df.to_csv(csv_name, index=None)


json_path='data.json'
data=read_json(json_path)

list_data=data['result']

list_items=[]
for item in list_data:
    schoolShortName=item['schoolShortName']
    termId=item['courseId']
    courseId='https://www.icourse163.org/course/'+item['schoolShortName']+'-'+str(item['courseId'])
    list_items.append(courseId)


csv_name='data.csv'
output_to_csv(list_items,csv_name)


