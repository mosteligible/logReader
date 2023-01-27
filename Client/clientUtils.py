def isPlanValid(providedPlan: str):
    check = providedPlan.lower() in ["small", "medium", "large"]
    return check
