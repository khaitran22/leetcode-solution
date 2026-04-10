# %%
def maxArea(height) -> int:
    idx_start = 0
    idx_end = len(height)-1
    max_area = min(height[idx_start], height[idx_end]) * (idx_end - idx_start)
    while idx_start < idx_end:
        if height[idx_start] < height[idx_end]:
            idx_start += 1
        else:
            idx_end -= 1

        current_area = min(height[idx_start],
                           height[idx_end]) * (idx_end - idx_start)
        if max_area < current_area:
            max_area = current_area

    return max_area


# %%
height = [1, 1]
maxArea(height)

# %%
