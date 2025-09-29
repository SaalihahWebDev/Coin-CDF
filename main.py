import itertools
coins=["H","T"]
outcomes=list(itertools.product(coins,repeat=6))
total=len(outcomes)
for outcome in outcomes:
    print(f"Probability of {outcome}=1/{total}={1/total}")
