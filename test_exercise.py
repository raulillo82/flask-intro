import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

def speed_calc_decorator(function):
  def wrapper_function():
      start_time = time.time()
      function()
      end_time = time.time()
      print (f"{function.__name__} run speed: {end_time - start_time}")
  return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

#Without the @ syntactic sugar
#If using this approach, the lines beginning with @ can be removed
#speed_calc_decorator(fast_function)()
#speed_calc_decorator(slow_function)()

#With the @ syntactic sugar
fast_function()
slow_function()
