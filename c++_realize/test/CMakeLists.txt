cmake_minimum_required(VERSION VERSION 2.6)
project(test)

find_package(OpenCV REQUIRED)

# config variable
set(TEST_DIR "${CMAKE_CURRENT_LIST_DIR}")

# generate macro execute 
macro(add_eval name sources)
    # execute project
    add_executable(${name}  ${sources})
    # Specify libraries when linking target
    target_link_libraries(${name} ${OpenCV_LIBS})
    target_link_libraries(${name} class)
    target_link_libraries(${name} template)
    
endmacro(add_eval)

# generate share|static library
# add_library(common STATIC util.cpp) 
# add_library(common SHARED util.cpp)

# add include file
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR} 
    ${CMAKE_CURRENT_LIST_DIR}
    ${OpenCV_INCLUDE_DIR}
)

include_directories(
    "${CMAKE_CURRENT_LIST_DIR}/class"
    "${CMAKE_CURRENT_LIST_DIR}/template"
)
# add execute source file
add_eval(start start.cpp)
add_eval(testStock ../class/test_stock.cpp)
add_eval(functionTemplateDemo ../template/function_template_demo.cpp)
add_eval(classTemplateDemo ../template/class_template_demo.cpp) 
add_eval(structDemo ../struct/struct_demo.cpp)
