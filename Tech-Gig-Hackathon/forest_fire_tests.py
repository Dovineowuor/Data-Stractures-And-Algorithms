import subprocess
import sys
import os

# Test case 1
N = 5
X = 4
energy_levels = [1, 3, 2, 4, 5]
expected_output = "2\n"
input_str = f"{N} {X}\n{' '.join(map(str, energy_levels))}\n"
output_str = subprocess.check_output(['python', 'forest_fire.py'], input=input_str, universal_newlines=True)
assert output_str == expected_output, f"Expected {expected_output}, but got {output_str}"

# Test case 2
N = 6
X = 3
energy_levels = [10, 5, 8, 12, 6, 9]
expected_output = "8\n"
input_str = f"{N} {X}\n{' '.join(map(str, energy_levels))}\n"
output_str = subprocess.check_output(['python', 'forest_fire.py'], input=input_str, universal_newlines=True)
assert output_str == expected_output, f"Expected {expected_output}, but got {output_str}"

# Test case 3
N = 3
X = 2
energy_levels = [1, 1, 1]
expected_output = "-1\n"
input_str = f"{N} {X}\n{' '.join(map(str, energy_levels))}\n"
output_str = subprocess.check_output(['python', 'forest_fire.py'], input=input_str, universal_newlines=True)
assert output_str == expected_output, f"Expected {expected_output}, but got {output_str}"

# Test case 4
N = 1
X = 1
energy_levels = [100]
expected_output = "100\n"
input_str = f"{N} {X}\n{' '.join(map(str, energy_levels))}\n"
output_str = subprocess.check_output(['python', 'forest_fire.py'], input=input_str, universal_newlines=True)
assert output_str == expected_output, f"Expected {expected_output}, but got {output_str}"

# Test case 5
N = 7
X = 5
energy_levels = [6, 8, 4, 3, 9, 2, 7]
expected_output = "4\n"
input_str = f"{N} {X}\n{' '.join(map(str, energy_levels))}\n"
output_str = subprocess.check_output(['python', 'forest_fire.py'], input=input_str, universal_newlines=True)
assert output_str == expected_output, f"Expected {expected_output}, but got {output_str}"

print("All test cases passed!")

