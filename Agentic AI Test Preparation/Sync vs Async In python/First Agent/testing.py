# #sync example:

# import time

# #Step 1 
# print("Test hona shuru...")
# time.sleep(5)
# print("Test hogaya.") 

# #Step 2 
# print("Result ana shuru...")
# time.sleep(5)
# print("Result agaya.")  


#async example:

import asyncio

async def test_hona_shuru():
    print("Test hona shuru...")
    await asyncio.sleep(3)
    print("Test hogaya.")
    
async def result_ana_shuru():
    print("Result ana shuru...")
    await asyncio.sleep(5)
    print("Result agaya.")
    
async def main():
    await asyncio.gather(test_hona_shuru(), result_ana_shuru())
    
asyncio.run(main()) 