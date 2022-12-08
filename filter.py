import json  
import collections
import random


def getData(input_business,input_reviews):
    business_datas = [json.loads(line)
        for line in open(input_business, 'r', encoding='utf-8')]
    reviewdatas = [json.loads(line)
        for line in open(input_reviews, 'r', encoding='utf-8')]
    random.shuffle(reviewdatas)
    return [business_datas,reviewdatas]




def construct_filter(business_datas,reviewdatas,choice,num_reviews,num_output,download):
    # choice: True, output the loction json
    # choice: False, output the restaurant json
    flag =  0
    if choice == True:
        flag = 1
    businessId2list = collections.defaultdict(list)
    businessId2json = collections.defaultdict(list)
    for data in business_datas:
        businessId2list[data["business_id"]] = [data["name"],data["city"],data["state"],data["categories"],data["review_count"],data["stars"]]
    visited = set()
    for data in reviewdatas:
        if businessId2list[data["business_id"]][flag] in visited:
            continue
        tempdict = {}
        tempdict["business_id"] = data["business_id"]
        tempdict["user_id"] = data["user_id"]
        tempdict["review_id"] = data["review_id"]
        tempdict["stars"] = businessId2list[data["business_id"]][5]
        tempdict["actual_yelp_score"] = data["stars"]
        time = data["date"].split(" ")
        tempdict["date"] = time[0]
        tempdict["time"] = time[1]
        tempdict["review"] = [data["text"]]
        tempdict["city"] = businessId2list[data["business_id"]][1]
        tempdict["state"] = businessId2list[data["business_id"]][2]
        tempdict["categories"] = businessId2list[data["business_id"]][3]
        tempdict["business_review_count"] = businessId2list[data["business_id"]][4]
    
        businessId2json[businessId2list[data["business_id"]][flag]].append(tempdict)
        
        if len(businessId2json[businessId2list[data["business_id"]][flag]]) >= num_reviews:
                visited.add(businessId2list[data["business_id"]][flag])
                if len(visited) == num_output:
                    break
        if download:
            for key in visited:
                name = key + ".json"
                try:
                    with open(name, 'w') as f:
                        for data in businessId2json[key]:
                            json.dump(data, f)
                except:
                    print("An exception occurred")
        else:
            res = []
            for key in visited:
                res.append(businessId2json[key])
        return res

    

if __name__ == "__main__":
  argments = sys.argv
  start = argments[0]
  end = argments[1]
  review_data_path = str(argments[3])
  num = int(argments[4])
  business_data_path = str(argments[5])
  output_path = str(argments[6])
  print('-----' + 'load review data begin'+ '-----')
  review_datas = [json.loads(line) for line in open(review_data_path, 'r', encoding='utf-8')]
  print('-----' + 'main data collection begin'+ '-----')
  main(start, end, review_datas,business_data_path, num, output_path)