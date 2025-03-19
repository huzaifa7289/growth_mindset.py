import streamlit as st

# Title
st.title("Unit Converter")

# Select the conversion type
conversion_type = st.selectbox(
    "Choose a conversion type:",
    ["Length", "Weight", "Temperature"]
)

# Conversion logic
def convert_length(value, from_unit, to_unit):
    length_units = {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084}
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return None

# Get user input
value = st.number_input("Enter value:", min_value=0.0, format="%.5f")

# Select units based on conversion type
if conversion_type == "Length":
    units = ["meters", "kilometers", "miles", "feet"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")

elif conversion_type == "Weight":
    units = ["grams", "kilograms", "pounds", "ounces"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
