# KINEMATICS #

# Kinematics is the physics of motion

# Here is an explanation on the "big 4 equations", all of which were used to make this
# algorithm: https://www.physicsclassroom.com/class/1dkin/Lesson-6/Kinematic-Equations

# r = rounding place

# Output will always be a float, so if you need to round, set r to whatever place you 
# are rounding to

# NOTE: Not all of these equations will give you an exactly same answer, but will be 
# very close. Typically you would only show sig 
# figs when you calculate with these equations.

# Doctests are all tested with initial_velocity=0, final_velocity=104.96, initial_position=0,
# final_position=1720, acceleration=3.2, time_elapsed=32.8, r=2

# These were calculated by hand so the output for distance is different, but the outputs 
# are more accurate than the one used for the example.

# In all cases distance is final_position-initial_position
# TOTAL distance is final_position+initial_position
# If you want to find distance from one point to another assume initial_position=0

# Typing hints
from typing import Union

# FINDING DISTANCE #

class NotEnoughInfo(Exception):
    pass

# r is rounding place
def distance(initial_velocity: Union[int,float] = None, final_velocity: Union[int,float] = None, 
             initial_position: Union[int,float] = None, acceleration: Union[int,float] = None, 
             time_elapsed: Union[int,float] = None, r: int = None) -> float:
    """
    Find distance for given initial_position, initial_velocity, final_velocity, acceleration* or t.
    
    :param initial_velocity: int, float
    :param initial_position: int, float
    :param final_velocity: int, float
    :param acceleration: int, float
    :param time_elapsed: int, float
    :param r: int
    :return: float
    
    >>> distance(initial_velocity=0, initial_position=0, acceleration=3.2, time_elapsed=32.8, r=2)
    1721.34
    >>> distance(initial_velocity=0, final_velocity=104.96, initial_position=0, time_elapsed=32.8, r=2)
    1721.34
    
    The variable 'r' can only be an integer.
    >>> distance(initial_velocity=0, final_velocity=104.96, initial_position=0, time_elapsed=32.8, r='2')
    Traceback (most recent call last):
        ...
    ValueError: r cannot be type 'str'
    
    When not given enough information, you will get an error.
    Ex. Trying to find distance without time
    >>> distance(initial_velocity=0, final_velocity=104.96, initial_position=0, r=2)
    Traceback (most recent call last):
        ...
    NotEnoughInfo: Not enough information to complete calculation.
    """
    if not acceleration:
        if None in (initial_position,initial_velocity,final_velocity,time_elapsed):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float(initial_position+((final_velocity+initial_velocity)/2)*time_elapsed), r)
            else:
                return float(initial_position+((final_velocity+initial_velocity)/2)*time_elapsed)
    else:
        if None in (initial_velocity,initial_position,acceleration*time_elapsed):
            raise NotEnoughInfo("Not enough information to complete calculation.")
        else:
            if r is not None:
                if type(r) != int:
                    raise ValueError(f"r cannot be type '{type(r).__name__}'")
                else:
                    return round(float(initial_position+(initial_velocity*time_elapsed)+((acceleration*(time_elapsed**2))*0.5)), r)
            else:
                return float(initial_position+(initial_velocity*time_elapsed)+((acceleration*(time_elapsed**2))*0.5))
