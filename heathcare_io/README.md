# Step 1: Project Design Overview

The Healthcare Information System (HIS) should manage:

Patient Records: Store and retrieve patient details, including name, age, gender, contact info, and unique patient ID.
Appointments: Track appointments with scheduling capabilities.
Medical Histories: Record past visits, diagnoses, prescriptions, and treatments.

# Step 2: Use Data Structures (Avoiding Arrays)

Consider the following data structures to manage data without using arrays:

Hash Tables (or Dictionaries): For efficient patient record lookup by unique patient ID.
Linked Lists: For storing a history of each patient’s visits and medical records in chronological order.
Binary Search Tree (BST) or Balanced Tree (e.g., AVL Tree): For managing appointments in a way that allows efficient searching and sorting by date.

# Step 3: Implement Searching Algorithms

Binary Search: Use binary search in sorted data (like sorted patient IDs or appointment dates) to efficiently retrieve patient or appointment details.
Depth-First Search (DFS): If you use a tree structure for medical histories or other nested data, DFS can help in exploring the tree, such as finding a patient’s earliest or latest history entry.

# Step 4: Implement Sorting Algorithms

Merge Sort: Sort patient records by IDs or names efficiently using Merge Sort, which is stable and works well with linked lists.
Quick Sort: Use Quick Sort to order appointments by date, especially if appointments are stored in an unsorted list.

# Step 5: Plan System Modules and Functions

Patient Record Management

Data Structure: Use a hash table with patient IDs as keys and objects containing patient details as values.
Functions:
add_patient(): Adds a new patient to the hash table.
remove_patient(): Removes a patient based on ID.
update_patient_info(): Updates patient details.
search_patient(): Finds a patient using their ID (binary search within the hash table if IDs are sorted).
Appointment Management

Data Structure: Store appointments in a Binary Search Tree or a list (sorted by date).
Functions:
add_appointment(): Inserts a new appointment (keep the BST balanced if using a tree).
cancel_appointment(): Removes an appointment from the list or tree.
find_appointment(): Searches for an appointment by date or patient ID.
sort_appointments(): Sorts appointments by date (using merge or quick sort).
Medical History Management

Data Structure: Linked list, where each node represents a medical visit entry for a patient.
Functions:
add_medical_history(): Adds a new entry to the end of the linked list for the patient.
view_medical_history(): Displays all entries for a patient.
search_medical_history(): Uses DFS to traverse the list to find specific entries based on date or type of visit.