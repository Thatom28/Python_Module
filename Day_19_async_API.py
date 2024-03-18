import requests
from pprint import pprint
import aiohttp
import asyncio
from time import time

TOKEN = "f06fdf2d66c24a91a6c93111241503"


# def get_city_temp(city_name):
#     response = requests.get(
#         f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no",
#         verify=False,
#     )
#     weather = response.json()
#     return weather["current"]["temp_c"]


# print(get_city_temp("capeTown"))


async def get_city_name(city_name):
    print(f"getting temp of {city_name}")
    await asyncio.sleep(2)
    async with aiohttp.ClientSession() as session:
        url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
        async with session.get(url) as response:
            weather = await response.json()
            print(
                f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']} °C "
            )


# task
# async def main():
#     all_cities = [
#         get_city_name("cape town"),
#         get_city_name("durban"),
#         get_city_name("pretoria"),
#     ]
# scheduling starts here
#     await asyncio.gather(*all_cities)

# asyncio.run(main())


# task 2
##cities =[] and crete a task
# 2s + 0.2 api
start_time = time()


# scheduling starts here
async def main():
    all_cities_tasks = [
        asyncio.create_task(get_city_name("cape town")),
        asyncio.create_task(get_city_name("durban")),
        asyncio.create_task(get_city_name("pretoria")),
    ]
    await asyncio.gather(*all_cities_tasks)  # it passes each city_task


# asyncio.run(main())
end_time = time()
# print(f"taken time ={end_time - start_time}")

# Task 3 : list comprehension
# Dry
cities = [
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Dubai",
    "Singapore",
    "Sydney",
    "Istanbul",
    "Hong Kong",
    "Cape Town",
]
# start_time = time()


# async def main():
#     all_cities_tasks = [get_city_name(city_name) for city_name in cities]
#     await asyncio.gather(*all_cities_tasks)


# # asyncio.run(main())
# end_time = time()
# print(f"taken time ={end_time - start_time}")
# -------------------------------------------------------------------------------------------------------
# Create a function that takes a list of cities provide the corrosponding temperature in a dictionary


# async def get_city_temp(city_name):
#     async with aiohttp.ClientSession() as session:
#         url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#         async with session.get(url) as response:
#             weather = await response.json()
#             return (weather["location"]["name"], weather["current"]["temp_c"])


# async def main(cities):
#     all_cities_and_temp = [get_city_temp(city_name) for city_name in cities]
#     all_cities_and_temp = await asyncio.gather(*all_cities_and_temp)
#     print(dict(all_cities_and_temp))


# async def main():
#     all_cities_and_temp = {
#         city_name: await get_city_temp(city_name) for city_name in cities
#     }


# print(all_cities_and_temp)


# async def get_temps(cities):
#     for city_name in cities:
#         async with aiohttp.ClientSession() as session:
#             url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#             async with session.get(url) as response:
#                 weather = await response.json()
#     return {city_name: weather["current"]["temp_c"]}


# async def main():
#     all_cities_and_temp = {get_temps(cities)}
#     print(await asyncio.gather(*all_cities_and_temp))


# asyncio.run(main())


# ------------------------------------------------------------------------------------------------
# RAGAV SOLUTION
async def get_city_name_temp(city_name):
    print(f"Getting temp of {city_name}")
    url = f"https://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return (weather["location"]["name"], weather["current"]["temp_c"])


# async def main(cities):
#     # print(await get_city_name_temp("New York"))
#     # print(await get_city_name_temp("Hong Kong"))
#     cities_data = [await get_city_name_temp(city) for city in cities]
#     pprint(dict(cities_data))


# asyncio.run(main(cities))


# Performance
async def main(cities):
    cities_data_co_current = [get_city_name_temp(city) for city in cities]
    cities_data = await asyncio.gather(*cities_data_co_current)
    pprint(dict(cities_data))


asyncio.run(main(cities))
