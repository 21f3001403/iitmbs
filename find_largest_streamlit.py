import streamlit as st

def largest_number(a, b, c):
    """
    This function finds the largest among the 3 given numbers.
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def main():
    st.title("GA-8, 21f3001403")
    st.title("Find the largest among 3 numbers")
    st.write("Enter 3 numbers below:")
    a = st.number_input("First number", min_value=0, step=1)
    b = st.number_input("Second number", min_value=0, step=1)
    c = st.number_input("Third number", min_value=0, step=1)
    if st.button("Find largest number"):
        result = largest_number(a, b, c)
        st.write("The largest number is:", result)

if __name__ == "__main__":
    main()
