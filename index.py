""" Create a function that calculates the chance of being an imposter.
Make sure to round the value to the nearest integer and return the
value as a percentage. """

def likely_imposter(imposter_count, player_count):
    imposter = 100 * (imposter_count/player_count)
    imposter = round(imposter)
    return f"{imposter}%"

print(likely_imposter(1, 2))
