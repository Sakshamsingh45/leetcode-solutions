class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()  # sort by start day
        i = 0
        day = 1
        n = len(events)
        attended = 0
        ongoing = []

        # Maximum day any event can end
        last_day = max(end for _, end in events)

        while day <= last_day:
            # Add events starting today
            while i < n and events[i][0] == day:
                ongoing.append(events[i][1])
                i += 1

            # Remove events that expired before today
            ongoing = [end for end in ongoing if end >= day]

            if ongoing:
                # Simulate picking the event that ends earliest
                min_end = min(ongoing)
                ongoing.remove(min_end)
                attended += 1

            day += 1

        return attended
