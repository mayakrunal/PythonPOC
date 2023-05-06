import re

if __name__ == '__main__':
    text = "The agent's phone number is 408-555-1234. Call soon!"
    pattern = 'phone'
    match = re.search(pattern, text)
