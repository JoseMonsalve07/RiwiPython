numbers=[{
    1: "uno",
    2: "dos",
    3: {
        "nombre": "David",
        "cc": 1035854944
    },
    4: "cuatro",
    5: "cinco",

},
{
    1: "uno",
    2: "dos",
    3: {
        "nombre": "Jose",
        "cc": 1035854946
    },
    4: "cuatro",
    5: "cinco",

}
]

result=numbers[1][3]["cc"]
print(result)