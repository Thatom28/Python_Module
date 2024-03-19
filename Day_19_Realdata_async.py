import requests
from pprint import pprint
import aiohttp
import asyncio
from time import time

# NB!!! # do not need gather as we are firing one api

API = "https://65f82857b4f842e808871367.mockapi.io"


async def get_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API}/users") as response:
            return await response.json()


async def get_user_name():
    users = await get_users()
    print("\n".join([user["name"] for user in users]))


# asyncio.run(get_user_name())


async def get_users_by_id(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API}/users/{id}") as response:
            user = await response.json()
            print(user)


# asyncio.run(get_users_by_id(17))


# --------------------------------------------------------------------------
# Delete user with id 15
async def delete_user_by_id(id):
    url2 = f"{API}/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url2) as response:
            return await response.json()


# async def main():
#     user = await delete_user_by_id(5)
#     pprint(user)


# asyncio.run(main())


# ----------------------------------------------------------------------------
# Task: delete first 5 users


# async def main():
#     users = await get_users()
#     first_five_Co_routine = await asyncio.gather(
#         *[delete_user_by_id(user["id"] for user in users[:5])]
#     )
#     pprint(first_five_Co_routine)


async def main():
    users = await get_users()
    five_users_co_routine = [delete_user_by_id(user["id"]) for user in users[:5]]
    deleted = await asyncio.gather(*five_users_co_routine)
    pprint(deleted)


# asyncio.run(main())
# -------------------------------------------------------------------------------------
# RAGAV solution
# async def get_users():
#     url = f"{API}/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


# async def delete_user_by_id(id):
#     url = f"{API}/users/{id}"
#     print(f"Deleting user...{id}")
#     async with aiohttp.ClientSession() as session:
#         async with session.delete(url) as response:
#             user = await response.json()
#             return user


# # Task - 1
# # Delete the first 5 users
# # Performant < 0.5s
# # Clue: 2 Steps
# # Clue: GET & Delete


# async def main():
#     users = await get_users()
#     first_five_users = users[:5]  # slice
#     first_five_users_co_routine = [
#         delete_user_by_id(user["id"]) for user in first_five_users
#     ]
#     deleted_users = await asyncio.gather(*first_five_users_co_routine)
#     pprint(deleted_users)
#     # pprint(first_five_users)
#     # print(len(first_five_users))


# asyncio.run(main())
# -----------------------------------------------------------------------------------
# task 2- change the avatar to human rights flag


# async def change_avater():
#     async with aiohttp.ClientSession() as session:
#         users = await get_users()
#         for user in users:
#             async with session.put(
#                 f"{API}/users{user["id"]}',
#                 json={
#                     "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/2000px-Flag_of_South_Africa.svg.png"
#                 },
#             ) as response:
#                 return await response.json()


# asyncio.run(change_avater())


# --------------------------------------------------------------------------------------------
async def update_avater(id):
    async with aiohttp.ClientSession() as session:
        async with session.put(
            f"{API}/users/{id}",
            json={
                "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/927.jpg"
            },
        ) as response:
            return await response.json()


async def main():
    users = await get_users()
    change_profile = [update_avater(user["id"]) for user in users[:10]]
    profile_pic = await asyncio.gather(*change_profile)
    pprint(profile_pic)


asyncio.run(main())


# -------------------------------------------------------------------------------------------------------------
# creating a user profile
# return coroutine
async def create_user(new_user):
    # print(new_user)
    url = f"{API}/users"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=new_user) as response:
            user = await response.json()
            return user


async def main():
    new_user = {
        "name": "Caleb",
        "avatar": "https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/927.jpg",
    }
    user_data = await create_user(new_user)
    print(user_data)


# asyncio.run(main())
# ------------------------------------------------------------------------------------------------------------------
# task 2: create 5 users
async def create_users(user_list):
    new_user = [
        create_user(
            {
                "name": user,
                "avatar": "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain",
            }
        )
        for user in user_list
    ]
    user_data = await asyncio.gather(*create_user(new_user))  # gather wants a box
    print(user_data)


user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
# asyncio.run(create_users(user_list))

# -----------------------------------------------------------------------------------------------
# RAGAV solution


async def main():

    user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
    flag = (
        "https://th.bing.com/th/id/OIP.K4XfRyYNnlwsR9-qdE-lrQAAAA?rs=1&pid=ImgDetMain"
    )

    user_co_routines = [
        create_user(
            {
                "name": user_name,
                "avatar": flag,
            }
        )
        for user_name in user_list
    ]
    users_data = await asyncio.gather(
        *user_co_routines
    )  # Box(user1), Box(user2).... Box(user5)
    # users_data -> [result1, ....result5]
    pprint(users_data)


# asyncio.run(main())

## When to use await
# when you use another async function in a async function
# - when you know the fuction will take time to complete (sleep() gather() API call)
# - if you dont await on a function, some of the results from the function will not be returned

# GATHER
# - when you want thigs to be fired concurrently asyncio.gather() -> it will take as much time as the longest function to execute

# -NB!! if things are dependent you cannot execute them concurrently e.g you cannot toast and butter the beread at the same time
#  the toast needs to be done before the bread is buttered [DO NOT USE GATHER IN THIS CASE]

# await asyncio.gather(get_user('123'), get_user('234')) #getting the details of the friends
# await asyncio.gather(*[get_user('123'), get_user('234')]) #using * in the above code
