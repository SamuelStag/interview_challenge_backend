from models.hoa import HOA
from typing import List
from repository import hoa



def get_hoas() -> List[HOA]:
    json_hoas = hoa.get_hoas()
    hoas = []
    for json_hoas in json_hoas:
        u = HOA(json_hoas.get("id"), json_hoas.get("name"), json_hoas.get("address"))
        hoas.append(u)
    return hoas

def get_hoas_by_id(val) ->List[HOA]:
    json_hoas = hoa.get_hoas()
    hoas =[]
    for json_hoas in json_hoas:
        u = HOA(json_hoas.get("id"), json_hoas.get("name"), json_hoas.get("address"))
        if u.id==val:
            hoas.append(u)
    return hoas

def add_hoas(hoas_name,hoas_address):
    hoas_id = len(hoa.get_hoas()) + 1
    new_hoas = HOA(hoas_id, hoas_name,hoas_address)
    hoa.add_hoas(new_hoas)

