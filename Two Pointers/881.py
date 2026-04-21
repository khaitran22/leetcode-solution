def numRescueBoats(people, limit):
    """
        Time: O(nlogn) -> due to sorted()
        Space: O(1)
    """
    people = sorted(people)
    i = 0
    j = len(people) - 1
    num_boat = 0
    while i < j:
        if people[i] + people[j] <= limit:
            i += 1

        num_boat += 1
        j -= 1
    if i == j:
        num_boat += 1
    return num_boat