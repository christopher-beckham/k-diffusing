import inspect
from k_diffusion import sampling

# Inspect k_diffusion/sampling.py and pull out all samplers with a certain function signature
def get_valid_samplers():
    functions = inspect.getmembers(sampling, inspect.isfunction)
    valid_fn_names = []
    for name, func in functions:
        print(f"Function: {name}")
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        if params[0].name=='model' and params[1].name=='x' and params[2].name == 'sigmas':
            print("  ...pass")
            valid_fn_names.append(name)
    return valid_fn_names