import random
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)


def call_model(prompt, **hyperparams):
    print("=====Model Request =====")
    print(f"Prompt : {prompt}")

    print("\nHyperParameters:")
    print(f"Temperature : {hyperparams.get('temperature')}")
    print(f"Max Tokens : {hyperparams.get('max_tokens')}")
    print("========================")

    success = random.choice([True, False])
    if success:
      logging.info("API Call Successful!")
    else:
      raise ConnectionError("API Call Failed")

    return  f"Processed Prompt: {prompt}"

for attempt in range(1, 4):
    logging.info(f"Attempt - {attempt}")
    try:
      response = call_model(
        "Explain Deep Learning",
        temperature=0.8,
        max_tokens=150,
      )
      logging.info(response)
      break
    except ConnectionError as e:
      logging.error(e)
      if attempt < 3:
       logging.info(f"Retrying in {attempt} seconds...\n")
       time.sleep(attempt)
      else:
       logging.critical("All attempts failed.")
    
