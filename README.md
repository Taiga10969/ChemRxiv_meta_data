# ChemRxiv_meta_data
ChemRxivからMeta Dataを収集するコードです．

## collect-data
```
python3 collect-data.py
```
**Setting**
- `params_term` : 検索キーワードのリスト
- `start_date` : 収集開始日（指定した日以降のものが対象）
- `end_date` : 収集終了日（指定した日以前のものが対象）
  
※1requestあたり直近50件のメタデータしか収集できないため，1日ずつrequestするプログラムになっております．<br>
※デフォルトのままですと，ChemRxivサービス開始日の`2017/8/14`から`2024/5/4`までの2455日のデータを対象として収集しています．<br>
