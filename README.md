# Assessment 003 - Python Data Structures

## Learning Outcomes assessed

- Data Structures
- Data Manipulation
- Recursion
- String Formatting

---

## Assessment Structure

The following Assessment has two sections:

- [Coding Assessment (Questions are below)](#fundamentals-coding-assessment)
- [Long Questions (Questions are below)](#long-format-questions) - `answers.txt`

You can answer them in any order.

---

## Your Goal

Read the instructions below for each [coding question](#fundamentals-coding-assessment), then complete each function in `data_structures.py` while ensuring that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass successfully

Read the instructions below for each [long format question](#long-format-questions), then add your answer under each relevant comment in `answers.txt` while ensuring thatL

- You DO NOT remove the comments
- Read each question carefully before answering the question

---

### How to run your tests

To run all your tests

```bash
python3 -m pytest tests/test_data_structures.py -v
```

To run your tests individually

```bash
python3 -m pytest tests/test_data_structures.py::test_split_coords_logic -v
```

or for more information within the stacktace use

```bash
python3 -m pytest tests/test_data_structures.py::test_split_coords_logic -vv
```

---

## Scoring & Weighting

| Component                                     | Weight  |
| --------------------------------------------- | ------- |
| Coding Section (unit tests)                   | **50%** |
| Long-format Question (answers.txt)            | **50%** |

## Fundamentals Coding Assessment

This assessment consists of five Python functions. Each function has a partially written
implementation. Your task is to **fix the bugs**, **complete the missing logic**, and **ensure all tests pass**.

### Project Structure

```text
fun-003-data-structures/
├── data_structures.py              # <-- This is where you write your solutions
├── answers.txt                     # <-- This is where you write your answers to the long questions
├── tests/
│   └── test_data_structures.py     # <-- These are the tests you must make pass
└── README.md                       # <-- Assessment instructions (this file) 
```

---

### Question 1 - `split_coords(coordinates)`

A team of eco-adventurers is mapping out a new hiking trail along the Wild Coast in the *Eastern Cape*. Their GPS device records the path as a series of coordinates, stored as pairs of (latitude, longitude); or in our case, **$(x, y)$** values.The navigation team at the base camp in *Chintsa* needs these coordinates separated. They need one list containing only the *$x$ values* (to calculate horizontal distance) and another list containing only the *$y$ values* (to track the vertical path). Instead of looking at them as pairs, they need two distinct "tracks" of data.

Apply your logic to the `split_coords()` function. You will receive a list of tuples, where each tuple contains two numbers. Your goal is to "unzip" or split these pairs into two separate lists.

- **Input:**

```python
[(12, 45), (15, 48), (18, 51)]
```

- **Output:**

```python
([12, 15, 18], [45, 48, 51])
```

---

### Question 2 - create_id_lookup(user_data)

It’s registration day for the *Comrades Marathon* in Durban! Thousands of runners are arriving to collect their race numbers. The volunteers at the desk have a list of runner names in the order they signed up (their "index" in the system).

To speed up the process, the organisers want a quick "lookup" system. Instead of scrolling through a long list every time a runner arrives, they want a digital folder (a dictionary) where they can type in a runner's name and immediately get their ID/Index number.

Apply your logic to the `create_id_lookup()` function. The function takes a list of names and should return a dictionary where each runner's name acts as the key and their position in the list (index) is the value.

- **Input:**

```python
["Sipho", "Lerato", "Thandi", "Kobane"]
```

- **Output:**

```python
{"Sipho": 0, "Lerato": 1, "Thandi": 2, "Kobane": 3}
```

---

### Question 3 - extract_unique_tags(posts)

You are working for a high-growth tech scale-up in the *Silicon Cape* (Cape Town’s tech hub). Your platform handles millions of micro-service events per hour. Every time a developer pushes code, the CI/CD pipeline generates "Tags" like Python, Java, Go, and Rust, based on the coding language. You need to process these tags so that the system only sees unique, lowercase identifiers.

Apply your logic to the `extract_unique_tags()` function. You must transform the list of raw tags into a set of unique, lowercase strings.

- **Input:**

```python
['Python', 'python', 'JAVA', 'Data', 'data', 'DATA', 'Code']
```

- **Output:**

```python
{'python', 'java', 'data', 'code'}
```

---

### Question 4 - group_by_category(items)

A major South African supermarket chain in Johannesburg is preparing for the *"Braai Day"* rush. Their online shopping app receives a messy list of items from a customer’s trolley, but the personal shoppers at the store need the list organised by Aisle Category so they can pick the items quickly without walking back and forth across the shop.

Apply your logic to the `group_by_category()` function. You will take a list of dictionaries, each containing a `name` and a `type`, and transform them into a single dictionary where each `type` is a key, and its value is a list of all item `names` belonging to that category.

- **Input:**

```python
[{"name": "Boerewors", "type": "Meat"}, {"name": "Charcoal", "type": "Hardware"}, {"name": "Lamb Chops", "type": "Meat"}, {"name": "Chakalaka", "type": "Canned Goods"}]
```

- **Output:**

```python
{"Meat": ["Boerewors", "Lamb Chops"], "Hardware": ["Charcoal"], "Canned Goods": ["Chakalaka"]}
```

---

### Question 5 - `batch_api_dispatcher(user_ids)`

The South African Social Security Agency (SASSA) needs to send out SMS notifications to citizens regarding their grant statuses. To keep the government servers running smoothly and avoid "crashing" the system, the SMS gateway has a strict limit: *it can only process a maximum of 5 users at a time in a single "batch" request*.

You have a list of `user_ids` that need their notifications sent. Your job is to help the IT team at the department in *Pretoria* organise these IDs into smaller groups (sublists) so the system can process them without any errors.

Apply your logic to the `batch_api_dispatcher()` function. The function should take the full list of IDs and break them down into a nested list where each internal "batch" contains a maximum of 5 IDs. If the total number of users isn't a perfect multiple of 5, the final batch will simply contain the remaining IDs.

- **Input:**

```python
['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7']
```

- **Output:**

```python
[['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7']]
```

Constraint: No sublist should ever exceed 5 items.

---

### Question 6 - `social_graph_inverter(following_list)`

A new South African social networking app, *Molo*, is gaining huge traction in Soweto and Mamelodi. The backend currently stores data based on who each user is following (e.g., "Sipho follows Lerato").

However, the marketing team needs to know the opposite: they want to see a list of followers for every user to identify the biggest local influencers.

Apply your solution to the `social_graph_inverter()` function. You are given a dictionary where the keys are users and the values are lists of people they follow. You must return a new dictionary where the keys are the people being followed and the values are lists of their followers.

- **Input:**

```python
{"Alice": ["Bob", "Charlie"], "Bob": ["Charlie"]}
```

- **Output:**

```python
{"Bob": ["Alice"], "Charlie": ["Alice", "Bob"]}
```

*Clarity: Because Alice follows Bob, Bob now has Alice in his followers list. Because both Alice and Bob follow Charlie, Charlie has both of them in his list.*

---

### Question 7 - `fibonacci_generator(n)`

Scientists at the Kirstenbosch National Botanical Garden in Cape Town are studying the growth patterns of various indigenous succulents and flowers, like the Protea. In nature, many plants follow a mathematical sequence where each new stage of growth is the sum of the two previous stages, this is known as the Fibonacci Sequence. The research team needs a tool to predict the number of petals or seed spirals a plant might develop over $n$ generations. To help them, you need to provide a list of the sequence up to the $n^{th}$ number.

Apply your solution to the `fibonacci_generator(n)` function. The function should take an integer $n$ and return a list containing the first $n$ numbers of the Fibonacci sequence.

- **Input:**

```python
n = 7
```

- **Output:**

```python
[0, 1, 1, 2, 3, 5, 8]
```

---

## Long-Format Questions

Please answer these in the `answers.txt` file (**DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT**)

### Question 1

Explain the difference between mutable and immutable data structures in Python.
Give two examples of each, and explain one practical situation where immutability would be beneficial

### Question 2

Explain when you would use a list versus a set versus a dictionary in Python, describing what each data structure is best suited for and why its characteristics make it appropriate for that use.

### Question 3

You are developing a live class-list application for a lecturer. Students can be added when they enroll, removed when they drop out, and updated when their information changes. This happens many times a day. Explain what characteristics the data structure managing the student list must have, and why certain data structures are more appropriate than others for handling this constantly changing data.

---

Good luck — and remember to think carefully about your solutions!
