#include <pybind11/pybind11.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <cmath>

namespace py = pybind11;
class FUNCT {
public:
    std::string output(const std::string& input) {
        return "Processed: " + input;
    }
    
    void input(){
        double Val1;
        std::cin >> Val1;
    }

    double getInput(double text_input){
        return text_input;
    }

    
};

PYBIND11_MODULE(CPPCLASS, m) {
    py::class_<FUNCT>(m, "FUNCT")
        .def(py::init<>())
        .def("output", &FUNCT::output)
        .def("input", &FUNCT::input);
}
int main(){

    return 0;
}