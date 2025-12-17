import json

equipos = [
    {
        "Nombre": "Real Madrid",
        "país": "España",
        "nivelAtaque": 90,
        "nivelDefensa": 85
    },
    {
        "Nombre": "Manchester City",
        "país": "Inglaterra",
        "nivelAtaque": 92,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Bayern Múnich",
        "país": "Alemania",
        "nivelAtaque": 89,
        "nivelDefensa": 84
    }
]


json_equipos = json.dumps(equipos, indent=4, ensure_ascii=False)

print(json_equipos)


