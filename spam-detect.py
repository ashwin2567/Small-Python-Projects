import os

def isFound(item, spam_word):
    with open(item) as f:
        content = f.read()
        if spam_word in content.lower():
            return True
        else :
            return False

if __name__ == "__main__":
    dir_content = os.listdir()
    for item in dir_content:
        if item.endswith('txt'):
            spam_word = "spammm"
            flag = isFound(item, spam_word)
            if flag:
                print(f"--------------{spam_word} found in {item}--------------")
            else:
                print(f"Not found in {item}")
        