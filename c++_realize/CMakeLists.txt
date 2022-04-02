cmake_minimum_required(VERSION VERSION 2.6)
project(cplusplus_experiment)

# config variable
set(TEST_DIR "${CMAKE_CURRENT_LIST_DIR}")

# generate macro
macro(add_eval name sources)
    add_executable(${name} ${sources})
endmacro(add_eval)

# add liabrary

include_directories(
    ${CMAKE_CURRENT_BINARY_DIR} # base.hpp
    ${CMAKE_CURRENT_LIST_DIR}
    ${OpenCV_INCLUDE_DIR}
)

include_directories(
    "${CMAKE_CURRENT_LIST_DIR}/class"
    "${CMAKE_CURRENT_LIST_DIR}/template"
    # target_link_libraries(${name} eval ${OpenCV_LIBS} ${libManis_LIBS})
)

# add executable
add_eval(start start.cpp)
# add_eval(testStock class/test_stock.cpp)