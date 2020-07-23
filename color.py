def color_pattern_times(cols):
    time_count = 2
    for i in range(1, len(cols)):
        if cols[i] == cols[i-1]:
            time_count += 2
        else:
            time_count += 3
    return time_count


color_pattern_times(["Red", "Blue", "Red", "Blue", "Red"])
