import streamlit as st
st.title("Google unit converter")
st.write("Easily convert between different unit of length, weight, and area.")

# user input
conversion_type = st.selectbox("choose conversion type",["length","weight", "area"])
value = st.number_input("Enter your value", value= 0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)


# conditions
if conversion_type == "length":
    with col1:
        from_unit = st.selectbox("from",["meter","inch","foot","cm","km"])
    with col2:
        to_unit = st.selectbox("to",["meter","inch","foot","cm","km"])
elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox("from",["kilogram","pound","gram","ounce"])
    with col2:
        to_unit = st.selectbox("to",["kilogram","pound","grams","ounce"])
elif conversion_type == "area":
    with col1:
        from_unit = st.selectbox("from",["square meter","acre","square yard","square kilometer"])
    with col2:
        to_unit = st.selectbox("to",["square meter","acre","square yard","square kilometer"])

# function for conversion
def length_converter(value, from_unit, to_unit):
    length_unit = {
        'meter': 1, 'inch':39.37, 'foot': 3.28, 'cm':100 , 'km':0.001 
    }
    return(value / length_unit[from_unit])*length_unit[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_unit = {
        'kilogram': 1 , 'pound':2.20462 , 'grams':1000 , 'ounce':35.274 ,
    }
    return(value / weight_unit[from_unit])* weight_unit[to_unit]

def area_converter(value, from_unit, to_unit):
    area_unit={
        'square meter': 1 , 'acre':4046.86 , 'square yard':0.836127, 'square kilometer':1e-6 ,
    }
    return(value / area_unit[from_unit])*area_unit[to_unit]


# button for convert
if st.button("convert"):
   if conversion_type == "length" :
      result = length_converter(value, from_unit, to_unit)
   elif conversion_type == "weight":
      result = weight_converter(value, from_unit, to_unit)
   elif conversion_type == "area":
      result = area_converter(value, from_unit, to_unit)
   st.write(f"result>>, {value}{from_unit} = {result:4f}{to_unit}")
