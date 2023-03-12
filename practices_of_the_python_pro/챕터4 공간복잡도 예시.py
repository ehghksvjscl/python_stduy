from collections import defaultdict, Counter

# 제너레이터 구현 연습
def square(numbers):
    for number in numbers:
        yield number ** 2

def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number

    return number_with_highest_count

## 리펙토링
def get_number_with_highest_count_refeactor(counts):
    return max(counts, key=lambda number: counts[number])

def get_most_frequent(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 0

    return get_number_with_highest_count(counts)

## 리펙토링
def get_most_frequent_refeactor(numbers):
    counts = defaultdict(int)
    for number in numbers:
        counts[number] += 1

    return get_number_with_highest_count(counts)

## 다시 리펙토링
def get_most_frequent_refeactor2(numbers):
    counts = Counter(numbers)
    print(counts)
    return get_number_with_highest_count_refeactor(counts)

print(get_most_frequent_refeactor2([1,1,2,2,3,3,2]))