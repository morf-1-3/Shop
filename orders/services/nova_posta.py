# d52574df69afe93302a2ecf161829429
import requests
from types import SimpleNamespace
API="d52574df69afe93302a2ecf161829429"
URL = "https://api.novaposhta.ua/v2.0/json/"

main_sities = [
        SimpleNamespace(Ref='e718a680-4b33-11e4-ab6d-005056801329', Description='м. Київ, Київська обл.'),
        SimpleNamespace(Ref='e717110a-4b33-11e4-ab6d-005056801329', Description='м. Дніпро, Дніпропетровська обл.'),
        SimpleNamespace(Ref='e71f8842-4b33-11e4-ab6d-005056801329', Description='м. Харків, Харківська обл.'),
        SimpleNamespace(Ref='e717bce9-4b33-11e4-ab6d-005056801329', Description='м. Запоріжжя, Запорізька обл.'),
        SimpleNamespace(Ref='e71c2a15-4b33-11e4-ab6d-005056801329', Description='м. Одеса, Одеська обл.'),
        SimpleNamespace(Ref='e71a2cab-4b33-11e4-ab6d-005056801329', Description='м. Кривий Ріг, Дніпропетровська обл.'),
        SimpleNamespace(Ref='e71abb60-4b33-11e4-ab6d-005056801329', Description='м. Львів, Львівська обл.'),
        SimpleNamespace(Ref='e71629ab-4b33-11e4-ab6d-005056801329', Description='м. Вінниця, Вінницька обл.'),
        SimpleNamespace(Ref='e71b108c-4b33-11e4-ab6d-005056801329', Description='м. Миколаїв, Миколаївська обл.'),
        SimpleNamespace(Ref='e71d006d-4b33-11e4-ab6d-005056801329', Description='м. Полтава, Полтавська обл.')
        ]

def get_settlements(part_find:str):
    query_setlement_json = {
    "apiKey": API,
    "modelName": "AddressGeneral",
    "calledMethod": "getSettlements",
    "methodProperties": {
        "FindByString" : part_find,
        "Limit" : "7",
        # "Ref" : "db5c88f0-391c-11dd-90d9-001a92567626"
        # "Warehouse" : "1",
        }
    }

    response = requests.get(URL,json=query_setlement_json)
    
    data = response.json()["data"]
    rez = []
    if len(data) > 0:
        # for settlement in data:
        #     name_settlement = f'{settlement["Description"]}, {settlement["RegionsDescription"] + " р-н," if settlement["RegionsDescription"] else ""} {settlement["AreaDescription"]} обл.'
        #     ref = settlement["Ref"]
        #     SimpleNamespace(Ref = ref, Description = name_settlement)
        #     rez.append(SimpleNamespace(Ref = ref, Description = name_settlement))
        rez = [
            SimpleNamespace(
                Ref = settlement["Ref"], 
                Description = f'{settlement["Description"]}, '
                f'{settlement["RegionsDescription"] + " р-н, " if settlement["RegionsDescription"] else ""}'
                f'{settlement["AreaDescription"]} обл.'
            )
            for settlement in data
        ]
    return rez

    

def get_warehouses_by_ref(ref:str):

    quert_warehouses= {
    "apiKey": API,
    "modelName": "AddressGeneral",
    "calledMethod": "getWarehouses",
    "methodProperties": {
        

        "Ref" : ref,
        # "WarehouseRef" : ref,
        "Limit" : "1",
  
  }
}   
  
    response = requests.get(URL,json=quert_warehouses)
    data = response.json()
    # rez = []
    # print(data)
    


def get_warehouses(ref:str,search_str:str=""):

    quert_warehouses= {
    "apiKey": API,
    "modelName": "AddressGeneral",
    "calledMethod": "getWarehouses",
    "methodProperties": {
        "FindByString" : search_str,
        # "CityName" : "Чернівці",
        # "CityRef" : ref,
        "SettlementRef" : ref,
        # "Page" : "1",
        "Limit" : "15",
        # "Language" : "UA",
        # "TypeOfWarehouseRef" : "00000000-0000-0000-0000-000000000000",
        # "WarehouseId" : "151"
  }
}   
  
    response = requests.get(URL,json=quert_warehouses)
    data = response.json()["data"]
    rez = []
    if len(data)>0:
        rez = [SimpleNamespace(
                Ref = warehouse["Ref"],
                Description = warehouse["Description"]
            ) 
            for warehouse in data
        ]
    # for rezult in rez:
    #     print(rezult.Description)
    return rez

# if __name__ == "__main__":
#     # ref = "0ebd8e4d-4b3a-11e4-ab6d-005056801329"
#     # ref = "8d5a980d-391c-11dd-90d9-001a92567626"
#     ref = "2d6a26fb-e9aa-11e4-8a92-005056887b8d"
    
#     get_warehouses_by_ref(ref)
    # find_by_ref(ref)


