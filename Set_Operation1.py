# Elena Voinu

L1 = [3, 6, 9, 0, 3]
L2 = [9, 6, 3, 0, 9, 4]

# L1 and L2 are two different lists, but as sets they are considered equal
print([L1 == L2, set(L1) == set(L2)])

# test membership, asking whether 10 is in each of the sets:
print([10 in L1, 10 in L2])
# will print false and false

print("Intersection of sets: ", set(L1) & set(L2))

union = set(L1) | set(L2)
print("Union of sets", union)

# The symmetric difference of A and B  is the set of all elements
# that are in A and B but not in both.
sym_diff = set(L1) - set(L2)
print("Symmetric difference of sets", sym_diff)

# set of elements that are in L2 and not in L1.
print("Complement of set L2: ", set(L2).difference(set(L1)))

# set of elements that are in L1 and not in L2.
print("Complement of set L1: ", set(L1).difference(set(L2)))
