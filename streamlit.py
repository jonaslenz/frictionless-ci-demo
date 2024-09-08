import streamlit as st
from frictionless import portals, Package, zenodo

if st.button("loading from zenodo"):
  package = Package("https://zenodo.org/record/7078760")
  report = catalog.packages[0].validate()
  st.write(report)
  st.write(catalog.packages[0].resources[0].to_pandas())

if st.button("loading local"):
  package = Package("data/data.yaml")
  report = package.validate()
  st.write(report)
  st.write(package.resources[0].to_pandas())
