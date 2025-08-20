def find_missing_ranges(frames: list[int]) -> dict:
    max_frame = 0
    for f in frames:
        if f > max_frame:
            max_frame = f


    received = set(frames)

    gaps = []
    longest_gap = []
    missing_count = 0

    i = 1
    while i <= max_frame:
        if i not in received:
            start = i
            while i <= max_frame and i not in received:
                i += 1
            end = i - 1
            gaps.append([start, end])

            gap_size = end - start + 1
            missing_count += gap_size
            if gap_size > (longest_gap[1] - longest_gap[0] + 1 if longest_gap else 0):
                longest_gap = [start, end]
        i += 1

    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }
