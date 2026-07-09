from dotenv import load_dotenv
import os
import argparse
#load enviornmental varriable
load_dotenv()
api_key = os.getenv("API_KEY")
# print(api_key)

# //t0 = input("Enter Text : ") instead

parser = argparse.ArgumentParser()
parser.add_argument("text")
args = parser.parse_args()
text = args.text

word0 = text.split()
keywords = {
   "ai",
    "data",
    "model",
    "python",
    "inference"
}
count = 0
for word in word0:
    if word.lower() in keywords:
        count += 1

print(f"""
======== AI REPORT ========

Total Words : {len(word0)}

AI Keywords : {count}

===========================
""")



