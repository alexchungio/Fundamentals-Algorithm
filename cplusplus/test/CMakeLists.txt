cmake_minimum_required(VERSION VERSION 2.6)
project(test)

# config variable
# set(TEST_DIR "${CMAKE_CURRENT_LIST_DIR}")

# generate macro execute 
macro(add_eval name sources)
    # execute project
    add_executable(${name}  ${sources})
    target_link_libraries(${name} ${OpenCV_LIBS})
    target_link_libraries(${name} class)
    target_link_libraries(${name} template)
    
endmacro(add_eval)


# add execute source file
add_eval(cvDemo cv_demo.cpp)
add_eval(testStock test_stock.cpp)
add_eval(functionTemplateDemo function_template_demo.cpp)
add_eval(classTemplateDemo class_template_demo.cpp) 
add_eval(lambdaDemo lambda_demo.cpp)
add_eval(structDemo ../struct/struct_demo.cpp)
add_eval(vectorDemo vector_demo.cpp)
add_eval(stringDemo string_demo.cpp)
add_eval(mapDemo map_demo.cpp)
add_eval(setDemo set_demo.cpp)
add_eval(tupleDemo tuple_demo.cpp)
add_eval(bag01 bag_01.cpp)
add_eval(linkedDemo ../linked_list/linked_demo.cpp)
add_eval(getNext ../kmp/get_next.cpp)
add_eval(findSubSequence ../leetcode/find_sub_sequences.cpp)
add_eval(candy ../leetcode/candy.cpp)
add_eval(eigenDemo ../eigen_example/eigen_demo.cpp)