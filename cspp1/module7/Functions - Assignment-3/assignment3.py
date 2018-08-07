"""# Functions - Assignment-3 - Using Bisection Search to Make
 the Program Faster
# You'll notice that in Problem 2, your monthly payment had to be a
 multiple of $10. Why did we cent amount (in other words, the monthly
  payment is a multiple of $0.01).
# Does your code still work? It should, but you may notice that your
 code runs more slowly,
 especially in cases with very large balances and interest rates.
  (Note: when your code is
 running on our servers, there are limits on the amount of computing
  time each submission
# is allowed, so your observations from running this experiment on the grading system might be
limited to an error message complaining about too much time taken.)
# What is a good upper bound? Imagine that instead of paying monthly, we paid
 off the entire balance at the end of the year. What we
# ultimately pay must be greater than what we would've paid in monthly installments,
 because the interest was compounded on the balance
# we didn't pay off each month. So a good upper bound for the
 monthly payment would be one-twelfth of the balance, after having its
# interest compounded monthly for an entire year."""
def paying_debt_off_in_a_year(balance, annual_interest_rate):
    """# In short:
    # the smallest monthly payment to the cent (no more multiples of $10) such that we
     can pay off the debt within a year. Try it out with
    # large inputs, and notice how fast it is (try the same large inputs in your solution to Problem
     2 to compare!). Produce the same return
    # value as you did in Assignment 2."""
    monthly_interest_rate = (annual_interest_rate) / 12.0
    monthly_payment_lower_bound = balance / 12
    monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    n_balance = balance
    eps = 0.001
    guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2
    while True:
        mon = 1
        while mon <= 12:
            n_balance = n_balance - guess
            n_balance = n_balance + (monthly_interest_rate * n_balance)
            mon += 1
        if n_balance > 0 and n_balance > eps:
            monthly_payment_lower_bound = guess
            n_balance = balance
        elif n_balance < 0 and n_balance < eps:
            monthly_payment_upper_bound = guess
            n_balance = balance
        else:
            return guess

        guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2
def main():
    """ it is a main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(round(paying_debt_off_in_a_year(data[0], data[1]), 2)))
if __name__ == "__main__":
    main()
