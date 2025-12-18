# planner.py
def plan(goal: str):
    g = goal.lower()

    if "termux" in g and "python" in g:
        return [
            "update termux packages",
            "install python",
            "verify python installation"
        ]

    if "error" in g or "traceback" in g:
        return [
            "identify error source",
            "suggest fix"
        ]

    return ["analyze request", "respond"]
