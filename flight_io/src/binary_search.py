def binary_search_flights(flights, origin, destination):
    left, right = 0, len(flights) - 1
    result = []
    while left <= right:
        mid = (left + right) // 2
        if flights[mid]["origin"] == origin and flights[mid]["destination"] == destination:
            result.append(flights[mid])  # Found a direct flight
            # Search for additional matches around mid
            i = mid - 1
            while i >= 0 and flights[i]["origin"] == origin and flights[i]["destination"] == destination:
                result.append(flights[i])
                i -= 1
            i = mid + 1
            while i < len(flights) and flights[i]["origin"] == origin and flights[i]["destination"] == destination:
                result.append(flights[i])
                i += 1
            return result
        elif flights[mid]["origin"] < origin or (flights[mid]["origin"] == origin and flights[mid]["destination"] < destination):
            left = mid + 1
        else:
            right = mid - 1
    return result
