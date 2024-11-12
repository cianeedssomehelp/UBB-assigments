"""
6. Given an array of integers A, maximize the value of the expression A[m] - A[n] + A[p] - A[q], where m, n, p, q are array indices with m > n > p > q.
For A = [30, 5, 15, 18, 30, 40], the maximum value is 32, obtained as 40 - 18 + 15 - 5. Display both the maximum value as well as the expression used to calculate it.

"""

def format_expression(a, b, c, d):
    # Use a conditional expression to format each number
    def fmt(num):
        return f"({num})" if num < 0 else str(num)

    expression = f"{fmt(a)} - {fmt(b)} + {fmt(c)} - {fmt(d)}"
    return expression

"""
This function aims to solve the problem efficiently using a dynamic programming approach.

Variables like max_m, max_m_n, max_m_n_p, and max_m_n_p_q represent the maximum values of partial expressions at each stage.
Index lists like max_m_index, max_m_n_indices, etc., store the indices associated with each maximum value.

We iterate backward from the second-to-last element to the beginning of the array. This reverse traversal allows us to accumulate maximum values for the required expressions.

At each step, the function checks whether adding/subtracting the current element improves any of the partial results (max_m, max_m_n, etc.).
It stores the maximum values in a way that builds up from simpler to more complex expressions (e.g., from max_m to max_m_n_p_q), tracking the best indices at each stage.

Time Complexity: O(n)

"""


def dynamicapproach(arr: list, length: int):

    # Initialize variables for the dynamic programming approach
    max_m = [float('-inf')] * length  #arr[m]
    max_m_n = [float('-inf')] * length #arr[m] - arr[n]
    max_m_n_p = [float('-inf')] * length #arr[m] - arr[n] + arr[p]
    max_m_n_p_q = float('-inf')  # Final result (only need one value for it) arr[m] - arr[n] + arr[p] - arr[q]

    # Track indices for each step
    max_m_index = [0] * length
    max_m_n_index = [[0, 0]] * length
    max_m_n_p_index = [[0, 0, 0]] * length
    final_indices = [0, 0, 0, 0]

    # Step 1: Fill max_m (best value for A[m])
    """
    Goal: Populate max_m[i] with the best possible value for A[m] from index i onward.
    We start by setting max_m[-1] to arr[-1] (the last element) and track its index.
    Then, for each index i from length - 2 to 0, we check whether arr[i] is greater than the next value in max_m[i + 1]. 
    If it is, max_m[i] becomes arr[i] and the corresponding index is stored in max_m_index[i]. 
    Otherwise, we carry forward the maximum value from the next index.
    """
    max_m[-1] = arr[-1]
    max_m_index[-1] = length - 1
    for i in range(length - 2, -1, -1):
        if arr[i] > max_m[i + 1]:
            max_m[i] = arr[i]
            max_m_index[i] = i
        else:
            max_m[i] = max_m[i + 1]
            max_m_index[i] = max_m_index[i + 1]

    # Step 2: Fill max_m_n (best value for A[m] - A[n])
    """
    Goal: Populate max_m_n[i] with the best possible value for A[m] - A[n] from index i onward.
    For each index i from length - 2 to 0, we check if the value max_m[i + 1] - arr[i] is greater than the current max_m_n[i + 1]. 
    If it is, we update max_m_n[i] and track the indices of m and n that give this maximum value.
    """
    for i in range(length - 2, -1, -1):
        if max_m_index[i + 1] != i and max_m[i + 1] - arr[i] > max_m_n[i + 1]:
            max_m_n[i] = max_m[i + 1] - arr[i]
            max_m_n_index[i] = [max_m_index[i + 1], i]
        else:
            max_m_n[i] = max_m_n[i + 1]
            max_m_n_index[i] = max_m_n_index[i + 1]

    # Step 3: Fill max_m_n_p (best value for A[m] - A[n] + A[p])
    """
    Goal: Populate max_m_n_p[i] with the best possible value for A[m] - A[n] + A[p] from index i onward.
    For each index i from length - 3 to 0, we check if the value max_m_n[i + 1] + arr[i] is greater than the current max_m_n_p[i + 1]. 
    If it is, we update max_m_n_p[i] and track the indices of m, n, and p that give this maximum value.
    """
    for i in range(length - 3, -1, -1):
        if max_m_n_index[i + 1][1] != i and max_m_n_index[i + 1][0] != i \
                and max_m_n[i + 1] + arr[i] > max_m_n_p[i + 1]:
            max_m_n_p[i] = max_m_n[i + 1] + arr[i]
            max_m_n_p_index[i] = max_m_n_index[i + 1] + [i]
        else:
            max_m_n_p[i] = max_m_n_p[i + 1]
            max_m_n_p_index[i] = max_m_n_p_index[i + 1]

    # Step 4: Compute max_m_n_p_q (final result A[m] - A[n] + A[p] - A[q])
    """
    Goal: Compute the final result for A[m] - A[n] + A[p] - A[q].
    For each index i from length - 4 to 0, we check if i is not already part of the indices used for m, n, and p. 
    If it’s not, and if max_m_n_p[i + 1] - arr[i] is greater than the current max_m_n_p_q, we update max_m_n_p_q and store the indices of m, n, p, and q.
    """
    for i in range(length - 4, -1, -1):
        indices_to_check = max_m_n_p_index[i + 1]
        if i not in indices_to_check and max_m_n_p[i + 1] - arr[i] > max_m_n_p_q:
            max_m_n_p_q = max_m_n_p[i + 1] - arr[i]
            final_indices = indices_to_check + [i]

    # Retrieve values for the expression
    m, n, p, q = final_indices

    expression_str = format_expression(arr[m], arr[n], arr[p], arr[q])

    return max_m_n_p_q, expression_str




"""
This function is a brute-force approach, checking all possible index combinations to find the maximum value of the expression.

This function uses four nested loops to iterate through all possible index positions for  m,n,p,q that satisfy m>n>p>q.

O(n^4): The four nested loops mean this approach has a time complexity of O(n^4) which is computationally expensive for larger arrays.
"""

def naiveapproach(arr: list, length: int):

    max_value = None
    max_expression = None

    for m in range(length-1, 2, -1):
        for n in range(m-1, 1, -1):
            for p in range(n-1, 0, -1):
                for q in range(p-1, -1, -1):
                    curr_value = arr[m] - arr[n] + arr[p] - arr[q]
                    # Update max_value for the first time or if a larger value is found
                    if max_value is None or curr_value > max_value:
                        max_value = curr_value
                        max_expression = (arr[m], arr[n], arr[p], arr[q])

    if max_expression is None:
        max_value = 0
        max_expression = (0, 0, 0, 0)
    return max_value, max_expression


def printsolutionandexpression(arr, length):
    print("Naive Approach: ")
    max_value_naive, expression_naive = naiveapproach(arr, length)
    print(f"Max Value = {max_value_naive}, Expression = {expression_naive[0]} - {expression_naive[1]} + {expression_naive[2]} - {expression_naive[3]}")
    print("\nDynamic Programming Approach:")
    max_value_dp, expression_dp = dynamicapproach(arr, length)
    print(f"Max Value = {max_value_dp}, Expression = {expression_dp}")

def main():
    try:
        length = int(input("Enter the size of your array: "))
        if length < 4:
            # Not enough elements to satisfy m > n > p > q
            raise ValueError
        arr = []
        for i in range(length):
            num = int(input("Enter the number from your list: "))
            arr.append(num)
        printsolutionandexpression(arr, length)
    except ValueError:
        print("The values you introduced are not integers, so they are not valid or the length is not greater than 4.")
main()