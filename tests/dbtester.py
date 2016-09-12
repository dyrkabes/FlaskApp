from models import calc

calc.Resource.set_cost(calc.Resource.get(calc.Resource.name=="Test_3"), 123)
calc.Resource.get(calc.Resource.name=="Test_3").set_cost(128)