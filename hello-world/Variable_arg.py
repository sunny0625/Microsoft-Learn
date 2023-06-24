def variable_length(*args):
    print(args)

variable_length()
()
variable_length("one", "two")
('one', 'two')
variable_length(None)
(None,)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
sequence_time(4, 14, 18)

sequence_time(4, 14, 48)

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
3 astronauts assigned for this mission:
captain: Neil Armstrong
pilot: Buzz Aldrin
command_pilot: Michael Collins

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")
  File "<stdin>", line 1
SyntaxError: keyword argument repeated: pilot