'''
Write a program to simulate disk scheduling algorithms
a) FCFS

Algorithm:

1. Let Request array represents an array storing indexes of tracks that have been requested 
in ascending order of their time of arrival. ‘head’ is the position of disk head.
2. Let us one by one take the tracks in default order and calculate the absolute distance 
of the track from the head.
3. Increment the total seek count with this distance.
4. Currently serviced track position now becomes the new head position.
5. Go to step 2 until all tracks in request array have not been serviced.
'''
request = [176, 79, 34, 60, 92, 11, 41, 114] 
current_position = 50
seek_count = 0

for track in request:
    seek_count += abs(current_position - track)
    current_position = track

print("Total number of seek operations: ", seek_count)