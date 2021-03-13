# LRU
'''
Let capacity be the number of pages that
memory can hold.  Let set be the current
set of pages in memory.

1- Start traversing the pages.
 i) If set holds less pages than capacity.
   a) Insert page into the set one by one until 
      the size  of set reaches capacity or all
      page requests are processed.
   b) Simultaneously maintain the recent occurred
      index of each page in a map called indexes.
   c) Increment page fault
 ii) Else 
   If current page is present in set, do nothing.
   Else 
     a) Find the page in the set that was least 
     recently used. We find it using index array.
     We basically need to replace the page with
     minimum index.
     b) Replace the found page with current page.
     c) Increment page faults.
     d) Update index of current page.

2. Return page faults.
'''
def page_faults(pages, frame_capacity):
   page_fault = 0
   frame = []
   indexes = []
   least_recent_index = 0
   for i in range(len(pages)):
      if len(frame) != frame_capacity:
         frame.append(pages[i])
         page_fault += 1
         indexes.append(i)
      else:
         if pages[i] in frame:
            # update index
            indexes[frame.index(pages[i])] = i
         else:
            frame[indexes.index(least_recent_index)] = pages[i]
            indexes[indexes.index(least_recent_index)] = i
            page_fault += 1

         least_recent_index = min(indexes)   
            
   return page_fault

pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
print("Page Fault(s): ", page_faults(pages, 4))