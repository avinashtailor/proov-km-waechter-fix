# fleet_report.py
# Prints the nightly fleet-health summary for Vossberg Mobility.
# Written in 2014. Runs every morning. Never cleaned up.

from km_wachter import wear_percent, needs_service, SERVICE_INTERVAL_KM


def car_wear(car):
    last = car["last_service_km"]                 # crashes if a car has no reading
    return wear_percent(car["odometer"] - last, SERVICE_INTERVAL_KM)


def fleet_summary(fleet):
    total = 0
    due = 0
    for car in fleet:
        total = total + car_wear(car)
        if needs_service(car) == True:
            due = due + 1
    average = total // len(fleet)                 # whole-number division loses the average
    return {"count": len(fleet), "due": due, "average_wear": average}


def print_report(fleet):
    s = fleet_summary(fleet)
    print("Fleet: %d cars" % s["count"])
    print("Due for service: %d" % s["due"])
    print("Average wear: %d%%" % s["average_wear"])
