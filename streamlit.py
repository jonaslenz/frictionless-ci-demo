import streamlit as st
from frictionless import portals, Package

package = Package("https://zenodo.org/record/7078760")
report = catalog.packages[0].validate()
st.write(report)

