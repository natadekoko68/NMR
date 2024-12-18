import sympy as sp
from IPython.display import display
from IPython.display import Math

data = {
    ("Ix", "Ix"): "0", ("Ix", "Iy"): "-Iz", ("Ix", "Iz"): "Iy", ("Ix", "Sx"): "0", ("Ix", "Sy"): "0", ("Ix", "Sz"): "0", ("Ix", "2IzSz"): "2IySz",
    ("Iy", "Ix"): "Iz", ("Iy", "Iy"): "0", ("Iy", "Iz"): "-Ix", ("Iy", "Sx"): "0", ("Iy", "Sy"): "0", ("Iy", "Sz"): "0", ("Iy", "2IzSz"): "-2IxSz",
    ("Iz", "Ix"): "-Iy", ("Iz", "Iy"): "Ix", ("Iz", "Iz"): "0", ("Iz", "Sx"): "0", ("Iz", "Sy"): "0", ("Iz", "Sz"): "0", ("Iz", "2IzSz"): "0",
    ("Sx", "Ix"): "0", ("Sx", "Iy"): "0", ("Sx", "Iz"): "0", ("Sx", "Sx"): "0", ("Sx", "Sy"): "-Sz", ("Sx", "Sz"): "Sy", ("Sx", "2IzSz"): "2IzSy",
    ("Sy", "Ix"): "0", ("Sy", "Iy"): "0", ("Sy", "Iz"): "0", ("Sy", "Sx"): "Sz", ("Sy", "Sy"): "0", ("Sy", "Sz"): "-Sx", ("Sy", "2IzSz"): "-2IzSx",
    ("Sz", "Ix"): "0", ("Sz", "Iy"): "0", ("Sz", "Iz"): "0", ("Sz", "Sx"): "-Sy", ("Sz", "Sy"): "Sx", ("Sz", "Sz"): "0", ("Sz", "2IzSz"): "0",
    ("2IzSx", "Ix"): "-2IySx", ("2IzSx", "Iy"): "2IxSx", ("2IzSx", "Iz"): "0", ("2IzSx", "Sx"): "0", ("2IzSx", "Sy"): "-2IzSz", ("2IzSx", "Sz"): "2IzSy", ("2IzSx", "2IzSz"): "Sy",
    ("2IzSy", "Ix"): "-2IySy", ("2IzSy", "Iy"): "2IxSy", ("2IzSy", "Iz"): "0", ("2IzSy", "Sx"): "2IzSz", ("2IzSy", "Sy"): "0", ("2IzSy", "Sz"): "-2IzSx", ("2IzSy", "2IzSz"): "-Sx",
    ("2IzSz", "Ix"): "-2IySz", ("2IzSz", "Iy"): "2IxSz", ("2IzSz", "Iz"): "0", ("2IzSz", "Sx"): "-2IzSy", ("2IzSz", "Sy"): "2IzSx", ("2IzSz", "Sz"): "0", ("2IzSz", "2IzSz"): "0",
    ("2IxSz", "Ix"): "0", ("2IxSz", "Iy"): "-2IzSz", ("2IxSz", "Iz"): "2IySz", ("2IxSz", "Sx"): "-2IxSy", ("2IxSz", "Sy"): "2IxSx", ("2IxSz", "Sz"): "0", ("2IxSz", "2IzSz"): "Iy",
    ("2IySz", "Ix"): "2IzSz", ("2IySz", "Iy"): "0", ("2IySz", "Iz"): "-2IxSz", ("2IySz", "Sx"): "-2IySy", ("2IySz", "Sy"): "2IySx", ("2IySz", "Sz"): "0", ("2IySz", "2IzSz"): "-Ix",
    ('2IxSx', 'Ix'): '0', ('2IxSx', 'Iy'): '-2IzSx', ('2IxSx', 'Iz'): '2IySx', ('2IxSx', 'Sx'): '0', ('2IxSx', 'Sy'): '-2IxSz', ('2IxSx', 'Sz'): '2IxSy', ('2IxSx', '2IzSz'): '0',
    ('2IxSy', 'Ix'): '0', ('2IxSy', 'Iy'): '-2IzSy', ('2IxSy', 'Iz'): '2IySy', ('2IxSy', 'Sx'): '2IxSz', ('2IxSy', 'Sy'): '0', ('2IxSy', 'Sz'): '-2IxSx', ('2IxSy', '2IzSz'): '0',
    ('2IySy', 'Ix'): '2IzSy', ('2IySy', 'Iy'): '0', ('2IySy', 'Iz'): '-2IxSy', ('2IySy', 'Sx'): '2IySz', ('2IySy', 'Sy'): '0', ('2IySy', 'Sz'): '-2IySx', ('2IySy', '2IzSz'): '0',
}

def get_transformation(initial_state, transformation):
    sign = 0
    key = (initial_state.replace("-", ""), transformation.replace("-", ""))
    result = data.get(key, "0")

    if initial_state.startswith("-"):
        sign += 1
    if transformation.startswith("-"):
        sign += 1
    if result.startswith("-"):
        sign += 1
    result = result.replace("-", "")

    return f"-{result}" if sign % 2 == 1 else result

def pulse(magnet_charge_dict, transform, time):
    """Applies a pulse transformation to the input magnetization states."""
    ret = {key: [] for key in [
        "E", "Ix", "Iy", "Iz", "Sx", "Sy", "Sz",
        "2IxSx", "2IxSy", "2IxSz", "2IySx", "2IySy", "2IySz",
        "2IzSx", "2IzSy", "2IzSz",
        "2SxSx", "2SxSy", "2SxSz", "2SySx", "2SySy", "2SySz",
        "2SzSx", "2SzSy", "2SzSz"
    ]}

    if time == "90°":
        cos_value, sin_value = 0, 1
    elif time == "π/2":
        cos_value, sin_value = 0, 1
    elif time == "pi/2":
        cos_value, sin_value = 0, 1
    elif time == "180°":
        cos_value, sin_value = -1, 0
    elif time == "π":
        cos_value, sin_value = -1, 0
    elif time == "pi":
        cos_value, sin_value = -1, 0
    else:
        cos_value = f"cos({time})"
        sin_value = f"sin({time})"

    for magnet_charge, coefficients in magnet_charge_dict.items():
        transformed_state = get_transformation(magnet_charge, transform)
        if transformed_state.startswith("-"):
            transformed_state = transformed_state[1:]
            for coeff in coefficients:
                if transformed_state == "0":
                    ret[magnet_charge].append(coeff)
                else:
                    ret[magnet_charge].append(f"{coeff}*{cos_value}")
                    ret[transformed_state].append(f"-{coeff}*{sin_value}")
        else:
            for coeff in coefficients:
                if transformed_state == "0":
                    ret[magnet_charge].append(coeff)
                    # print(magnet_charge,transform)
                else:
                    ret[magnet_charge].append(f"{coeff}*{cos_value}")
                    ret[transformed_state].append(f"{coeff}*{sin_value}")
    ret = {key: value for key, value in ret.items() if value}
    return ret

def display_dict(magnet_charge_dict):
    ret = []
    for key, terms in magnet_charge_dict.items():
        if terms:
            simplified = sp.simplify(" + ".join(terms))
            if simplified != 0:
                latex_key = key
                ret.append("{"+f"{simplified}"+"} * "f"{latex_key}")
    return " + ".join(ret).replace(" + -", " - ").replace("1 ", "")


def display_dict_only_observables(magnet_charge_dict):
    ret = []
    observables = ["Ix","Iy","Sx","Sy","2IxSz","2IySz","2IzSx","2IzSy"]
    for key, terms in magnet_charge_dict.items():
        if key in observables:
            if terms:
                simplified = sp.simplify(" + ".join(terms))
                if simplified != 0:
                    latex_key = key
                    ret.append("{"+f"{simplified}"+"} * "f"{latex_key}")
    return " + ".join(ret).replace(" + -", " - ").replace("1 ", "")

if __name__ == "__main__":
    result = pulse({"Iz":["1"]},"Ix","pi/2")
    result = pulse(result, "2IzSz", "πJτ")
    result = pulse(result, "Sx", "pi/2")
    result = pulse(result, "Ix", "pi")
    result = pulse(result, "Sz", "Ωt")
    result = pulse(result, "Sx", "pi/2")
    result = pulse(result, "2IzSz", "πJτ")
    latex_result = display_dict(result)
    display(Math(sp.latex(latex_result)))
