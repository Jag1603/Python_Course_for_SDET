from queue import Queue
q=Queue(); q.put("job-1"); q.put("job-2")
while not q.empty(): print(q.get())