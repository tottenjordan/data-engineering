The goal of this program is to assess the execution time of breadth-frst-search (BFS) on a connection graph. 

We develop a five level connection graph, without duplicates in each node, and search for particular names in each level of the graph. The purpose of the connection graph is to work in a similar fashion as a dictionary. From the results, we noted that connection graphs, like dictionaries, tend to have incredibly fast run times.

#### Breadth-First Search
* BFS tells you if there's a path from A to B
* If there's a path, BFS will find the shortest path
* If you havea problem like "find the shortest X," try modeling your problem as a graph, and use BFS to solve
* Undirected graphs dont have arrows, and the relationship goes both ways (ross - rachel means "ross dated rachel and rachel dated ross")
* Queues are FIFO 
* Stakcs are LIFO
* You need to check people in the order they were added to the search list, so the search lst needs to be a queue. Otherwise, you won't get the shortest path
* Once you check someone, make sure you don't check them again. Otherwise, you might end up in an infinite loop
