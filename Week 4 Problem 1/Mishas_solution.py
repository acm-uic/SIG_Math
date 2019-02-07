# problem statement
# Given a set of size n, comprised of (1, 2, 3 ... n - 1, n) how many permutations have no number
# in its natural position
# Due to the dearrangement theorem, the answer, as n approaches infinity, is (n / e) sets

# Permutation function taken from geeks4geeks
# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

def permutation_test(test_list):
    for j in range(len(test_list) - 1, -1, -1):
        for i in range(len(test_list[j])):
            if test_list[j][i] == i + 1:
                del test_list[j]
                break
    return test_list


test_set = [1]

for k in range(1, 10):
    permuted_list = list(permutation(test_set))
    value_of_e = (1 + (1 / k)) ** k 
    print("Size", len(permuted_list))
    print("Length of set with no number in natural position is: ", len(permutation_test(permuted_list)), str(value_of_e * int(len(permutation_test(permuted_list)))))
    test_set.append(2 + k)
