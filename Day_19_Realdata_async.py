import requests
from pprint import pprint
import aiohttp
import asyncio
from time import time


# async def get_user_name():
#     async with aiohttp.ClientSession() as session:
#         url = "https://65f82857b4f842e808871367.mockapi.io/users"
#         async with session.get(url) as response:
#             users = await response.json()
#             return "\n".join([user["name"] for user in users])


# async def main():
#     user_names = await get_user_name()
#     print(user_names)


# asyncio.run(main())
# --------------------------------------------------------------------------
# Delete user with id 15
async def delete_user_by_id(id):
    url = f"https://65f82857b4f842e808871367.mockapi.io/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            user = await response.json()
            return user


# async def main(id):
#     user = await delete_user_by_id(id)
#     pprint(user)


# asyncio.run(main(10))
# ----------------------------------------------------------------------------
# Task: delete first 5 users
async def get_users():
    url = f"https://65f82857b4f842e808871367.mockapi.io/users/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            return users


async def main():
    first_five = users[:5]
    first_five_Co_routine = [delete_user_by_id([user["id"] for user in first_five])]
    deleted_user_by_id = await asyncio.gather(*first_five_Co_routine)
    pprint(deleted_user_by_id)


asyncio.run(main())
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
# task 2- cahnge the avatar to human rights flag
