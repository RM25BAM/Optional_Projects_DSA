Updated Flight Reservation Project Plan
The plan incorporates the following:

Core Features:
Sign In, Sign Up.
Flight Search.
Reservation Management.
Payment Integration.
Algorithms and Data Structures:
Two searching algorithms.
Two sorting algorithms.
Two non-array data structures.
Bonus Features:
Optional additions for more credit.
1. Searching Algorithms
a. Binary Search:

Use Case: Direct flight search when flights are stored in a sorted database (sorted by departure time, price, or destination).
Implementation:
Assume the flight list is sorted by departure time or price.
Use binary search to quickly locate flights matching the origin and destination.
b. Breadth-First Search (BFS):

Use Case: Finding connecting flights (shortest layover path) using a graph where nodes represent airports and edges represent flights.
Implementation:
Use BFS to traverse a graph and find the shortest path (layover connections) from origin to destination.
Bonus Search Algorithm: Hash Lookup:

Use Case: Efficient reservation lookup by reservation ID using a hash table.
2. Sorting Algorithms
a. Merge Sort:

Use Case: Sort flights by price, departure time, or duration in ascending order.
Implementation:
Implement Merge Sort for the flight database.
b. Quick Sort:

Use Case: Sort passenger reservations by name or booking time for administrative reports.
Implementation:
Use Quick Sort on the reservation list.
Bonus Sorting Algorithm: Bucket Sort:

Use Case: Efficient sorting of flights by price range.
3. Data Structures
a. Hash Table:

Use Case:
Store and retrieve reservations by unique reservation ID.
O(1) average time complexity for lookups.
Implementation:
Key: Reservation ID.
Value: Reservation details.
b. Graph:

Use Case:
Represent flight routes between cities.
Nodes: Cities.
Edges: Flights.
Implementation:
Use adjacency lists to represent the graph.
Bonus Data Structures:

Trie:
Auto-complete for airport codes or city names during flight search.
Priority Queue (Heap):
Store flights to retrieve the cheapest flight efficiently.
4. Integration of Algorithms and Data Structures
Here’s how to integrate the required components into the project:

Feature 1: Flight Search

Input: Origin, destination, and travel date.
Process:
Binary Search:
Quickly find direct flights in a sorted database (by price or time).
Breadth-First Search (BFS):
Traverse a graph of flight routes to find connecting flights.
Sorting:
Use Merge Sort to organize results by price or travel time.
Output: Display a table of available flights.
Feature 2: Reservation Management

Input: Passenger details, flight ID, seat selection.
Process:
Hash Table:
Store reservations by reservation ID for quick lookup and management.
Quick Sort:
Sort reservations by booking time or passenger name.
Output: Confirmation of booking and a sorted list of reservations.
Feature 3: Admin Dashboard

Input: View flight data and reservations.
Process:
Graph:
Visualize flight connections.
Priority Queue:
Retrieve flights based on priority (e.g., cheapest or earliest).
Output: Administrative tools for flight and reservation management.
Workflow
Here’s the project workflow to meet the requirements:

Step 1: Setup Data Structures:
Initialize a flight database as a list of dictionaries.
Use a hash table for reservations.
Represent flight routes as a graph.
Step 2: Implement Searching Algorithms:
Binary Search for direct flight lookup.
BFS for finding connecting flights.
Step 3: Implement Sorting Algorithms:
Merge Sort for flight results.
Quick Sort for reservations.
Step 4: Combine Features:
Integrate searching and sorting algorithms into the flight search and reservation management features.
Step 5: Advanced Features (Optional):
Add a priority queue for retrieving cheapest flights.
Use a Trie for airport code auto-compl