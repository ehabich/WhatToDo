'''
Object
'''

class Establishment():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.latitude = self._find_lat_long(self.address)[0]
        self.longitude = self._find_lat_long(self.address)[1]
        self.events_hosted = [] # list of associated Event objects of events organized by this establishment
        self.events_held = [] # list of associated Event objects of events held at this establishment

    def _find_lat_long(self, address):
        # use self.address to query and find address (UT database?)
        return ['test_lat', 'test_long']

    def add_hosted_event(self, event):
        self.hosted_events.append(event)

    def add_helf_event(self, event):
        self.held_events.append(event)

    def __str__(self):
        return f"{self.name} \n {self.address} \n ({self.latitude}, {self.longitude}) \n hosted events: {self.events} \n held events: {self.events_held}"

class Event():
    def __init__(self, name, date, time, location_establishment, host_establishment=None):
        self.name = name
        self.date = date
        self.time = time
        self.host_establishment = host_establishment # None if host an dlcoation are the same, pass an Establishment object
        self.location_establishment = location_establishment # pass an Establishment object

    def __str__(self):
        host = f"Hosted by {self.host_establishment.name}" if self.host_establishment else None
        return f"{self.name} \n {self.location} \n {self.date} \n {self.time} \n {self.establishment.name} \n {host}"
    

# Example usage:

# Create an establishment
establishment = Establishment(name="Cafe ABC", address="123 Main St")

# Create events associated with the establishment
event1 = Event(name="Live Music Night", date="2025-08-10", time="7:00 PM", location="Cafe ABC", establishment=establishment)
event2 = Event(name="Poetry Reading", date="2025-08-12", time="6:00 PM", location="Cafe ABC", establishment=establishment)

# Access events from the establishment
print(f"Events at {establishment.name}:")
for event in establishment.events:
    print(f"- {event.name} on {event.date} at {event.time}")
