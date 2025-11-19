def swap_ends (L,k):
    LC = L.copy()
    if k <= 0 or k > len(L)//2 or len(L)==0:
        return (LC, 0)
    else:
        new_list = LC
        new_list[:k]= LC[-k:]
        new_list[-k:] = LC[:k]
        return (new_list, k)
# %%
print(swap_ends([1, 2, 3, 4], 2))
