import os
import time
import json
import datetime
import requests
from tqdm import tqdm

import utils

url = "https://chemrxiv.org/engage/chemrxiv/public-api/v1/items"
save_directory = './Chemrxiv_meta_data'
params_term = ['protein', 'biochemistry', 'peptides', 'enzymes', 'amino acids', 'biomolecules', 'proteinomics', 'chemical biology', 'macromolecules', 'biopolymers']

# データを取得する範囲の開始日
start_date = datetime.datetime.strptime("2017-08-14", "%Y-%m-%d")
# データを取得する範囲の終了日
end_date = datetime.datetime.strptime("2023-05-05", "%Y-%m-%d")
# 検索間隔（1日ごと）
delta = datetime.timedelta(days=1)
date_list = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days)]
print(f"Collection period range {len(date_list)} days")

utils.create_directory(save_directory)


data_dict = {}
save_total_num = 0

for term in params_term:

    term_data_list = []
   
    progress_bar = tqdm(date_list, desc=f"Term: {term}")
    for date in progress_bar:

        params = {
            "term": term,
            "limit": 50,  # 1ページあたりのアイテム数 (50max)
            "searchDateFrom": date.strftime('%Y-%m-%d'),  # 開始日
            "searchDateTo": (date + delta).strftime('%Y-%m-%d')  # 終了日
        }

        time.sleep(1)
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            for i, item_hit in enumerate(data['itemHits']):
                filename = item_hit['item']['doi'].replace("/", "-")

                if filename not in term_data_list:
                    term_data_list.append(filename)

                # ファイルが存在しない場合のみ保存
                if not os.path.exists(os.path.join(save_directory, f"{filename}.json")):
                    with open(os.path.join(save_directory, f"{filename}.json"), 'w') as f:
                        # JSON形式で保存
                        json.dump(item_hit, f, indent=4)
                    save_total_num += 1
                
                progress_bar.set_postfix({"get_data": len(data['itemHits']), "save_total_num": save_total_num})
        else:
            print(f"error >> term: {term} searchDateFrom: {date.strftime('%Y-%m-%d')}")  

    data_dict[term] = term_data_list

with open(os.path.join("collect-data_result.json"), 'w') as f:
    # JSON形式で保存
    json.dump(data_dict, f, indent=4)