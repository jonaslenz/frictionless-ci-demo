import streamlit as st
from frictionless import portals, Package, Catalog

if st.button("loading catalog from zenodo"):
  control = portals.ZenodoControl(apikey=st.secrets["apikey"])
  package = Package("https://zenodo.org/record/7078768", control=control)
  st.write(package)
if st.button("loading catalog from zenodo"):
  control = portals.ZenodoControl(search='notes:"TDWD"')
  catalog = Catalog(control=control)
  catalog.infer()
  st.write("Total packages", len(catalog.packages))
  st.write(catalog.packages)

if st.button("loading from zenodo"):
  package = Package("https://zenodo.org/record/7078760")
  report = catalog.packages[0].validate()
  st.write(report)
  st.write(catalog.packages[0].resources[0].to_pandas())

if st.button("loading local"):
  package = Package("data/data.yaml")
  report = package.validate()
  st.write(report)
  st.write(package.resources[1].to_pandas())
