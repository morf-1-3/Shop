# d52574df69afe93302a2ecf161829429
import requests
from types import SimpleNamespace
from dotenv import load_dotenv
import os
load_dotenv()
API=os.getenv("API_POSHTA")
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
    "calledMethod": "searchSettlements",
    "methodProperties": {
        "CityName" : part_find,
        "Limit" : "7",

        }
    }

    response = requests.get(URL,json=query_setlement_json)
    
    data = response.json()["data"][0]["Addresses"] 
    
    rez = []

    if len(data) > 0:
        

        rez = [
            SimpleNamespace(
                Ref = settlement["Ref"], 
                Description = settlement["Present"]
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
        "Limit" : "1",
  
  }
}   
  
    response = requests.get(URL,json=quert_warehouses)
    data = response.json()
    


def get_warehouses(ref:str,search_str:str=""):

    quert_warehouses= {
    "apiKey": API,
    "modelName": "AddressGeneral",
    "calledMethod": "getWarehouses",
    "methodProperties": {
        "FindByString" : search_str,
        "SettlementRef" : ref,
        "Limit" : "15",
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
   
    return rez



# if __name__ == "__main__":
#     # get_settlement()
#     datas = get_settlements("Київ")
#     for data in datas:
#         print(data)
#    

