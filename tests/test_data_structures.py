import pytest
from data_structures import *
from unittest.mock import patch

# Question 1

@pytest.mark.parametrize("input_coords, expected_x, expected_y", [
    ([(1, 2), (3, 4), (5, 6)], [1, 3, 5], [2, 4, 6]),    
    ([(10, 20)], [10], [20]),    
    ([], [], []),    
    ([(-1.5, 0), (0, 2.2)], [-1.5, 0], [0, 2.2]),    
    ([(1, 1), (1, 1)], [1, 1], [1, 1])
])
def test_split_coords_logic(input_coords, expected_x, expected_y):
    x_res, y_res = split_coords(input_coords)
    assert x_res == expected_x
    assert y_res == expected_y

def test_split_coords_integrity():
    input_data = [(i, i+1) for i in range(100)]
    x_coords, y_coords = split_coords(input_data)
    
    assert len(x_coords) == len(input_data)
    assert len(y_coords) == len(input_data)

    assert x_coords[50] == 50
    assert y_coords[50] == 51

def test_split_coords_invalid_tuple_size():
    bad_input = [(1, 2), (3, 4, 5)]
    with pytest.raises(ValueError):
        split_coords(bad_input)

def test_split_coords_non_iterable_element():
    bad_input = [(1, 2), 3]
    with pytest.raises(TypeError):
        split_coords(bad_input)

def test_split_coords_large_dataset():
    large_input = [(i, i) for i in range(100000)]
    x, y = split_coords(large_input)
    assert len(x) == 100000
    assert x[99999] == 99999

def test_split_coords_single_coord():
    assert split_coords([(1, 2)]) == ([1], [2])

def test_split_coords_multiple_coords():
    assert split_coords([(1, 2), (3, 4), (5, 6)]) == ([1, 3, 5], [2, 4, 6])

def test_split_coords_multiple_coords_2():
    assert split_coords([(10, 20), (30, 40), (50, 60), (70, 80)]) == ([10, 30, 50, 70], [20, 40, 60, 80])

def test_split_coords_negative_coords():
    assert split_coords([(-1, -2), (-3, -4), (-5, -6)]) == ([-1, -3, -5], [-2, -4, -6])

def test_split_coords_mixed_coords():
    assert split_coords([(0, 0), (1, -1), (-1, 1)]) == ([0, 1, -1], [0, -1, 1])

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 2
    
@pytest.mark.parametrize("user_data, expected_dict", [  
    (["Peter", "Busang", "Mpho"], {"Peter": 0, "Busang": 1, "Mpho": 2}),    
    ([], {}),    
    (["Solo"], {"Solo": 0}),    
    (["alice", "Alice"], {"alice": 0, "Alice": 1}),
])
def test_create_id_lookup_logic(user_data, expected_dict):
    assert create_id_lookup(user_data) == expected_dict

def test_create_id_lookup_duplicates():
    names = ["Alice", "Bob", "Alice"]
    result = create_id_lookup(names)
    
    assert result["Alice"] == 2
    assert len(result) == 2

def test_create_id_lookup_large_scale():
    large_names = [f"User_{i}" for i in range(100000)]
    result = create_id_lookup(large_names)
    
    assert len(result) == 100000
    assert result["User_99999"] == 99999

def test_create_id_lookup_unhashable_type():
    bad_data = ["Alice", ["I", "am", "unhashable"]]
    with pytest.raises(TypeError):
        create_id_lookup(bad_data)

def test_create_id_lookup_single_name():
    assert create_id_lookup(['Zoe']) == {'Zoe': 0}

def test_create_id_lookup_duplicate_names():
    assert create_id_lookup(['Anna', 'Bob', 'Anna']) == {'Anna': 2, 'Bob': 1}

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 3
    
@pytest.mark.parametrize("input_tags, expected_set", [
    (["Python", "python", "PyThOn"], {"python"}),
    (["Go", "Rust", "Java"], {"go", "rust", "java"}),
    ([], set()),
    (["Web3", "dot-net"], {"web3", "dot-net"}),
])
def test_extract_unique_tags_logic(input_tags, expected_set):
    assert extract_unique_tags(input_tags) == expected_set

def test_extract_unique_tags_large_dataset():
    large_input = (["TagA"] * 50000) + (["taga"] * 50000)
    result = extract_unique_tags(large_input)
    assert len(result) == 1
    assert "taga" in result

def test_extract_unique_tags_logic():
    input_tags = ['Python', 'python', 'Data', 'data', 'DATA', 'Code']
    expected_output = {'python', 'data', 'code'}
    assert extract_unique_tags(input_tags) == expected_output

def test_extract_unique_tags_no_duplicates():
    input_tags = ['Java', 'C++', 'Ruby']
    expected_output = {'java', 'c++', 'ruby'}
    assert extract_unique_tags(input_tags) == expected_output

def test_extract_unique_tags_all_duplicates():
    input_tags = ['Tag', 'tag', 'TAG', 'tAg']
    expected_output = {'tag'}
    assert extract_unique_tags(input_tags) == expected_output

def test_extract_unique_tags_mixed_case():
    input_tags = ['Hello', 'WORLD', 'hello', 'world', 'HeLLo']
    expected_output = {'hello', 'world'}
    assert extract_unique_tags(input_tags) == expected_output

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 4
    
@pytest.mark.parametrize("items, expected", [
    (
        [ 
            {"name": "Boerewors", "type": "Meat"}, 
            {"name": "Charcoal", "type": "Hardware"}, 
            {"name": "Lamb Chops", "type": "Meat"}, 
            {"name": "Chakalaka", "type": "Canned Goods"} 
        ],
        { "Meat": ["Boerewors", "Lamb Chops"], "Hardware": ["Charcoal"], "Canned Goods": ["Chakalaka"] }
    ),
    (
        [
            {"name": "Hammer", "type": "Tools"},
            {"name": "Drill", "type": "Power Tools"},
            {"name": "Wrench", "type": "Tools"}
        ],
        {"Tools": ["Hammer", "Wrench"], "Power Tools": ["Drill"]}
    ),
    (
        [
            {"name": "Python", "type": "Software"},
            {"name": "VS Code", "type": "IDE"},
            {"name": "Docker", "type": "Software"}
        ],
        {"Software": ["Python", "Docker"], "IDE": ["VS Code"]}
    ),
    ([], {}),
    (
        [{"name": "Sedan", "type": "Vehicle"}],
        {"Vehicle": ["Sedan"]}
    ),
    (
        [        
            {'name': 'Apple', 'type': 'Fruit'},        
            {'name': 'Carrot', 'type': 'Vegetable'},        
            {'name': 'Banana', 'type': 'Fruit'},        
            {'name': 'Broccoli', 'type': 'Vegetable'},        
            {'name': 'Chicken', 'type': 'Meat'}    
        ],
        {'Fruit': ['Apple', 'Banana'], 'Vegetable': ['Carrot', 'Broccoli'], 'Meat': ['Chicken']}
    )
])
def test_group_by_category_logic(items, expected):
    assert group_by_category(items) == expected

def test_group_by_category_missing_keys():
    with pytest.raises(KeyError):
        group_by_category([{"name": "Laptop"}])

def test_group_by_category_non_dict_elements():
    with pytest.raises(TypeError):
        group_by_category([None])

def test_group_by_category_integrity():
    items = [{"name": "Pliers", "type": "Tools"}]
    result = group_by_category(items)
    assert isinstance(result["Tools"], list)
    assert len(result["Tools"]) == 1

def test_group_by_category_large_input():
    items = [{"name": f"Sensor_{i}", "type": "Hardware"} for i in range(5000)]
    result = group_by_category(items)
    assert len(result["Hardware"]) == 5000
    assert result["Hardware"][0] == "Sensor_0"

def test_group_by_category_alternative():
    items = [        
        {'name': 'Salmon', 'type': 'Fish'},        
        {'name': 'Tuna', 'type': 'Fish'},        
        {'name': 'Lettuce', 'type': 'Vegetable'}    
    ]
    expected_output = {        
        'Fish': ['Salmon', 'Tuna'],        
        'Vegetable': ['Lettuce']    
    }
    assert group_by_category(items) == expected_output

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 5
    
@pytest.mark.parametrize("input_ids, expected_output", [   
    (['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7'], [['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7']]),    
    (['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], [['ID1', 'ID2', 'ID3', 'ID4', 'ID5']]),    
    ([], []),    
    (['ID1', 'ID2'], [['ID1', 'ID2']]),    
    (['1', '2', '3', '4', '5', '6'], [['1', '2', '3', '4', '5'], ['6']]),
])
def test_batch_api_dispatcher_logic(input_ids, expected_output):
    assert batch_api_dispatcher(input_ids) == expected_output

def test_batch_api_dispatcher_immutability():
    original = ['A', 'B', 'C', 'D', 'E', 'F']
    original_copy = original.copy()
    
    batch_api_dispatcher(original)
    
    assert original == original_copy, "The input list was mutated during batching!"

def test_batch_api_dispatcher_large_scale():
    large_input = [f"ID{i}" for i in range(10000)]
    result = batch_api_dispatcher(large_input)
    
    assert len(result) == 2000
    assert len(result[0]) == 5
    assert result[-1][-1] == "ID9999"

def test_batch_api_dispatcher_non_list_iterable():
    input_tuple = ('ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6')
    expected = [['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6']]
    
    assert batch_api_dispatcher(input_tuple) == expected

def test_batch_api_dispatcher_single_request():
    assert batch_api_dispatcher(['ID1']) == [['ID1']]

def test_batch_api_dispatcher_multiple_requests():
    assert batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7']) == [['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7']]

def test_batch_api_dispatcher_exact_multiple():
    assert batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7', 'ID8', 'ID9', 'ID10']) == [['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7', 'ID8', 'ID9', 'ID10']]

def test_batch_api_dispatcher_mixed_ids():
    assert batch_api_dispatcher(['ID10', 'ID5', 'ID3', 'ID8', 'ID1', 'ID7']) == [['ID10', 'ID5', 'ID3', 'ID8', 'ID1'], ['ID7']]

def test_batch_api_dispatcher_large_number_of_requests():
    user_ids = [f'ID{i}' for i in range(1, 21)]
    expected_output = [
        ['ID1', 'ID2', 'ID3', 'ID4', 'ID5'],
        ['ID6', 'ID7', 'ID8', 'ID9', 'ID10'],
        ['ID11', 'ID12', 'ID13', 'ID14', 'ID15'],
        ['ID16', 'ID17', 'ID18', 'ID19', 'ID20']
    ]
    assert batch_api_dispatcher(user_ids) == expected_output

def test_batch_api_dispatcher_fewer_than_batch_size():
    assert batch_api_dispatcher(['ID1', 'ID2', 'ID3']) == [['ID1', 'ID2', 'ID3']]

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 6
    
@pytest.mark.parametrize("following_list, expected_followers", [
    (
        {"Alice": ["Bob", "Charlie"], "Bob": ["Charlie"]},
        {"Bob": ["Alice"], "Charlie": ["Alice", "Bob"]}
    ),
    (
        {"UserA": ["UserB"], "UserB": ["UserA"]},
        {"UserB": ["UserA"], "UserA": ["UserB"]}
    ),
    ({}, {}),
    (
        {"Alice": [], "Bob": ["Alice"]},
        {"Alice": ["Bob"]}
    ),
    (
        {"A": ["X"], "B": ["X"], "C": ["X"]},
        {"X": ["A", "B", "C"]}
    )
])
def test_social_graph_inverter_logic(following_list, expected_followers):
    assert social_graph_inverter(following_list) == expected_followers

def test_social_graph_inverter_immutability():
    original = {"Alice": ["Bob"]}
    original_copy = {"Alice": ["Bob"]}
    social_graph_inverter(original)
    assert original == original_copy

def test_social_graph_inverter_non_iterable_value():
    with pytest.raises(TypeError):
        social_graph_inverter({"Alice": None})

def test_social_graph_inverter_large_star_graph():
    star_graph = {f"User{i}": ["Celebrity"] for i in range(10000)}
    result = social_graph_inverter(star_graph)
    
    assert len(result["Celebrity"]) == 10000
    assert "User9999" in result["Celebrity"]

def test_social_graph_inverter_self_follow():
    self_follow = {"Alice": ["Alice"]}
    result = social_graph_inverter(self_follow)

    assert result == {"Alice": ["Alice"]}

def test_social_graph_inverter_referential_integrity():
    data = {"Alice": ["Bob"]}
    result = social_graph_inverter(data)
    result["Bob"].append("Charlie")

    assert "Charlie" not in social_graph_inverter(data)["Bob"]

# ------------------------------------------------------------------------------------------ # ------------------------------------------------------------------------------------------ #

# Question 7
    
@pytest.mark.parametrize("n, expected_output", [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (5, [0, 1, 1, 2, 3]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
])

def test_fibonacci_generator_logic(n, expected_output):
    assert fibonacci_generator(n) == expected_output

def test_fibonacci_generator_large_n():
    result = fibonacci_generator(30)
    assert len(result) == 30
    assert result[-1] == 514229

def test_fibonacci_generator_zero_and_one():
    assert fibonacci_generator(0) == []
    assert fibonacci_generator(1) == [0]

def test_fibonacci_generator_negative_n():
    with pytest.raises(ValueError):
        fibonacci_generator(-5)

def test_fibonacci_generator_non_integer_n():
    with pytest.raises(ValueError):
        fibonacci_generator(5.5)

def test_fibonacci_generator_integrity():
    result = fibonacci_generator(20)
    assert result[0] == 0
    assert result[1] == 1
    assert result[2] == 1
    assert result[3] == 2
    assert result[4] == 3

def test_fibonacci_generator_edge_cases():
    assert fibonacci_generator(2) == [0, 1]
    assert fibonacci_generator(3) == [0, 1, 1]
    assert fibonacci_generator(4) == [0, 1, 1, 2]

def test_is_recursion_implemented():

    with patch("data_structures.fibonacci_generator", wraps=fibonacci_generator) as mocked_function:
        mocked_function(10)
        
        assert mocked_function.call_count > 1, f"Recursion not detected. Count: {mocked_function.call_count}"

def test_recursion_depth():
    depth = 2000
    with pytest.raises(RecursionError):
        fibonacci_generator(depth)

def test_recursion_parameters():
    with patch("data_structures.fibonacci_generator", wraps=fibonacci_generator) as mocked_function:
        mocked_function(5)
        
        for call in mocked_function.call_args_list:
            args, _ = call
            assert len(args) == 1, "Recursive calls should have exactly one argument."
            assert isinstance(args[0], int), "Recursive call argument should be an integer."