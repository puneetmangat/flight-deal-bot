from modules.optimizer import optimize_trip


def build_profile(answers):
    profile = {
        "location": answers.get("location"),
        "goal": answers.get("goal"),
        "destination": answers.get("destination"),
        "dates": answers.get("dates"),
        "budget": answers.get("budget"),
    }

    profile["trip"] = optimize_trip(profile)

    return profile
