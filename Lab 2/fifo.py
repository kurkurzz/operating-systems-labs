from queue import Queue

# FIFO
'''
1- Start traversing the pages.
 i) If set holds less pages than capacity.
   a) Insert page into the set one by one until 
      the size  of set reaches capacity or all
      page requests are processed.
   b) Simultaneously maintain the pages in the
      queue to perform FIFO.
   c) Increment page fault
 ii) Else 
   If current page is present in set, do nothing.
   Else 
     a) Remove the first page from the queue
        as it was the first to be entered in
        the memory
     b) Replace the first page in the queue with 
        the current page in the string.
     c) Store current page in the queue.
     d) Increment page faults.

2. Return page faults.
'''
def page_faults(pages, frame_capacity):
	frame = []
	q = Queue(frame_capacity)
	page_fault = 0

	# traverse each pages
	for i in range(len(pages)):
		if pages[i] not in frame:
			page_fault += 1
			if len(frame) != frame_capacity: 
				frame.append(pages[i])
				q.put(pages[i])
			else:
				frame[frame.index(q.get())] = pages[i]
				q.put(pages[i])
			print(frame)
			
	return page_fault

pages = [0,2,1,6,4,0,1,0,3,1,2,1]
print("Page Fault(s): ", page_faults(pages, 3))
