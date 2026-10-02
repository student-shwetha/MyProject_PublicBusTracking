def calculate_eta(distance_km, average_speed_kmh):
    """
    Calculate the estimated arrival time based on distance and average speed.

    Args:
        distance_km (float): Distance to travel in kilometers
        average_speed_kmh (float): Average speed in kilometers per hour

    Returns:
        float: Estimated time in minutes

    Raises:
        ValueError: If distance or speed is negative or zero
    """
    if distance_km <= 0 or average_speed_kmh <= 0:
        raise ValueError("Distance and speed must be positive values")

    time_hours = distance_km / average_speed_kmh
    time_minutes = time_hours * 60
    return time_minutes


# Example usage
if __name__ == "__main__":
    eta = calculate_eta(10, 40)
    print(f"ETA for 10 km at 40 km/h: {eta:.2f} minutes")
