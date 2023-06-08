import yaml

print(yaml.load(open('inf.yml',encoding='utf-8'), Loader=yaml.FullLoader))
with open('demo.yml','w',encoding='utf-8') as f:
    yaml.dump(data = ['name:刘康', {'adress': ['省份:湖北', '城市:武汉']}],stream=f)