def first_and_last(message):
    if (message == ""):
        return True
    if (message[0] == message[-1]):
        return True
    # print(message[0])
    # print(message[-1])
    return False

print("else:" + str(first_and_last("else")))
print("tree: " + str(first_and_last("tree")))
print("Empty String: " + str(first_and_last("")))