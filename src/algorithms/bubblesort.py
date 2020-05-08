def sort_one(lines):
    if lines.already_sorted < len(lines.values) - 1:
        for i in range(len(lines.values) - lines.already_sorted - 1):
            if lines.values[i] > lines.values[i + 1]:
                lines.values[i], lines.values[i + 1] = lines.values[i + 1], lines.values[i]
        lines.already_sorted += 1
