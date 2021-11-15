from typing import Optional, List, Dict
from typing import Callable as F

RegistryT = Dict[str, F[[str], str]]

def default_msg(fruit:str) -> str:
    return f"I dont want a {fruit}"

def to_msg(fruit:str) ->str:
    return f"I didn`t know {fruit} is a fruit"

def to_registry() ->RegistryT:
    d:RegistryT = {}
    d['apple'] = lambda x: "I love apples"
    for x in ('eggplant', 'squash'):
        d[x] = to_msg
    return d

REGISTRY = to_registry()

def eat(fruit:str) ->str:
    return REGISTRY.get(fruit, default_msg)(fruit)

print(eat('apple'))
print(eat('apple'))


