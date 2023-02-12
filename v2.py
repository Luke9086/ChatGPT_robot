from revChatGPT.V2 import Chatbot
import sys
import json
import time
import random
"""
pip3 install --upgrade revChatGPT
Refer to https://github.com/acheong08/ChatGPT
for more information
"""

async def main(prompt):
    chatbot = Chatbot(email="adps1@foxmail.com", password="openai1311!")
    messages = ""
    async for line in chatbot.ask(prompt):
        print(line["choices"][0]["text"].replace("<|im_end|>", ""), end="")
        sys.stdout.flush()
        message = line["choices"][0]["text"].replace("<|im_end|>", "")
        messages = messages + message
    q_a = {"question":prompt,"answer":messages}
    json_objects = json.dumps(q_a,indent=4)
    # change the file name by yourself
    with open("sample.json","a") as f:
        f.write(json_objects)

    print()
    #print(response["choices"][0]["text"])

if __name__ == "__main__":
    import asyncio
    # change the file name by yourself, each line end with "\n"
    with open("test.txt","r") as f:
        prompts = f.read()
    for prompt in prompts.split("\n"):
        print(prompt)
        if prompt == "":
            continue
        asyncio.run(main(prompt))
        time.sleep(random.random()*3)
