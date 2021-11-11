geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish", "Eagle", " Grippen", "Cock", "Swift"]
def goose_filter(birds):
    result = []
    for bird in birds:
        count = 0
        for goose in geese:
            if bird == goose:
                count += 1
        if count == 0:
            result.append(bird)
    return result
print(goose_filter(birds))
