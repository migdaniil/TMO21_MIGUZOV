def chairs_per_row(chairs, rows):
    if rows == 0:
        return "На ноль делить нельзя"
    return chairs / rows


assert chairs_per_row(72, 9) == 8.0

assert chairs_per_row(72, 0) == "На ноль делить нельзя"

assert chairs_per_row(50, 5) == 10.0


words = ["ряд", "класс", "библиотека"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)