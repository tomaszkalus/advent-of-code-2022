with open('input.txt') as f:
    text = f.read()

index = 0
for i, c in enumerate(text):
    try:
        chars = [text[x] for x in range(i, i+14)]
    except IndexError:
        break
    if len(set(chars)) == len(chars):
        index = i + 14
        break

print("First marker after character", index)
