nums=[3,4,"doce",True,"False",{
    "product": "mouse",
    "value": 300,
    "cantidad": 3
}]

product2={
    "product": "tv",
    "value": 600,
    "cantidad": 20
}

nums.append(product2)
print(nums[5]["value"])
print(nums[6])

list1=[1,2,3]
list2=[4,5,6]

list1.extend(list2)

print(list1)

for i in list1:
    result = i*2
    print(result)

names=["diego", "sara", "jose", "ana", "luisa", "david", "pedro", "jose"]
for name in names:
    print(f"hola {name}")

del names[1:5]
print(names)    

dicNums={
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6
}
