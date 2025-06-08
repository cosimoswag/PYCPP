
//Compilare
g++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) CPPCLASS.cpp -o CPPCLASS$(python3-config --extension-suffix)
//avviare file py
streamlit PYUI.py