def optimize_trip(profile):
    plan = {
        "departure": profile["location"],
        "destination": profile["destination"],
        "goal": profile["goal"],
        "dates": profile["dates"],
        "budget": profile["budget"],
        "recommendations": []
    }

    return plan
