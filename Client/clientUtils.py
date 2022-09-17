def isPlanValid(providedPlan: str):
    check = providedPlan.lower() in ["small", "medium", "large"]
    if not check:
        raise ValueError("plan should be one of the three: small, medium, large")
    return True
