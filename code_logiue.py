"""
Yemba Calendar Correspondence 2026
Author: Kevin Styve Nanvou
Description:
Compute the corresponding Yemba day for any Gregorian date in 2026,
based on a predefined repeating list of 31 days.
"""

from datetime import date

JourYemba = [ "Mbouotchou", "Efa'a", "Njielah", "Ngang", "Mbouwa", "Mbouolo",
              "Meta", "Mbouokeu"]
JourFrancais = ["Jeudi", "Vendredi", "Samedi",
                 "Dimanche","Lundi", "Mardi", "Mercredi"]


# Reference date
day_zero = date(2026, 1, 1)


def yemba_day(target_date):

    delta_days = (target_date - day_zero).days
    indexY = delta_days % len(JourYemba)
    indexF = delta_days % len(JourFrancais)
    return JourYemba[indexY],JourFrancais[indexF]

# Example usage
if __name__ == "__main__":
    # Test for first 10 days of January 2026
    for d in range(1, 32):
        current_date = date(2025, 12, d)
        y_day = yemba_day(current_date)
        print(f"{current_date}: day = {y_day[0]} - {y_day[1]}")

    # Test for any arbitrary date
    test_date = date(2026, 2, 15)
    print(f"{test_date}: day = {yemba_day(test_date)}")