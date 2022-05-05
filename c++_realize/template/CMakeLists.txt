cmake_minimum_required(VERSION VERSION 2.6)
project(template)


# list(APPEND SRC_FILE )
# list(APPEND SRC_FILE function_template.cpp)
# search file
file(GLOB_RECURSE HEAD_LIST "${CMAKE_CURRENT_LIST_DIR}/*.hpp")
file(GLOB_RECURSE SRC_LIST "${CMAKE_CURRENT_LIST_DIR}/*.cpp")

# add libarary to project
add_library(template ${SRC_LIST} ${HEAD_LIST})
