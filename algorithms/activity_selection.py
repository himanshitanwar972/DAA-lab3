def activity_selection(activities):
    """
    Select the maximum number of non-overlapping activities.
    Each activity has a name, start time, and finish time.
    """

    if any(
        activity["start"] > activity["finish"]
        for activity in activities
    ):
        raise ValueError("Start time cannot exceed finish time.")

    # Select activities in increasing order of finish time.
    sorted_activities = sorted(
        activities,
        key=lambda activity: activity["finish"]
    )

    selected = []
    last_finish = None

    for activity in sorted_activities:
        if (
            last_finish is None
            or activity["start"] >= last_finish
        ):
            selected.append(activity)
            last_finish = activity["finish"]

    return selected