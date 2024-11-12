"""
7. Generate all subsequences of length 2n+1, formed only by 0, -1 or 1, such that a1 = 0, ..., a2n+1= 0 and |ai+1 - ai| = 1 or 2, for any 1 ≤ i ≤ 2n.
"""

solutioncnt = 0

def consistent(arr: list) -> bool:
    """
    Determines whether the current partial array can lead to a solution
    """
    for i in range(len(arr)-1):
        if abs(arr[i + 1] - arr[i]) not in {1, 2}:  #if the absolute difference is not from {1, 2} it is not a valid subsequence
            return False
    return True


def solution(arr: list, n: int):
    """
    Determines whether we have a solution (i. e., a subsequence of length 2n+1).
    """
    return len(arr) == 2 * n + 1 and arr[-1] == 0 # arr[-1] == 0 last elem of list


def solution_found(arr):
    """
    What to do when a solution is found (in this case, print it).
    """
    global solutioncnt
    solutioncnt += 1
    print(f"Solution {solutioncnt}: ", arr)

# time complexity: O(3^(2n+1)) because the maximum depth of recursion is 2n+1 and we need to check from three choices [-1, 0, 1]
# space complexity: O(n) for the recursion stack and O(n * 3^(2n+1)) for storing each partial sequence
def bkt_rec(arr, n):
    """
    Backtracking algorithm for subsequences problem, recursive implementation.
    """
    if len(arr) == 2 * n + 1:
        #If we have built a sequence of length 2n+1, check if it's a solution.
        if solution(arr, n):
            solution_found(arr)
        return

    #try each possible value in the set {-1, 0, 1}
    for i in [-1, 0, 1]:
        arr.append(i)
        if consistent(arr):
            bkt_rec(arr, n)
        arr.pop()


# time complexity: O(3^(2n+1)) because the maximum depth of recursion is 2n+1 and we need to check from three choices [-1, 0, 1]
# space complexity: O(n * 3^(2n+1)) for storing each partial sequence
def bkt_iter(arr: list, n: int) -> tuple:
    """2
        Backtracking algorithm for subsequences problem, iterative implementation
    """
    stack = [arr]
    while len(stack) > 0:
        current_arr = stack.pop()
        if len(current_arr) == 2 * n + 1:
            if solution(current_arr, n):
                solution_found(current_arr)
            continue

        for i in [-1, 0, 1]:
            new_arr = current_arr + [i]  # Create a new candidate array
            if consistent(new_arr):  # Proceed only if consistent
                stack.append(new_arr)  # Push the new state onto the stack

def generate_subsequences(n: int):
    """
    Starts the backtracking process by initializing the sequence with the first element being 0.
    """
    x = [0]
    bkt_rec(x, n)
    bkt_iter(x, n)

def main():
    try:
        n = int(input("Enter the size of your list: "))
        generate_subsequences(n)
    except:
        print("Value error")
main()
