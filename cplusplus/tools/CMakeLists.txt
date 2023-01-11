cmake_minimum_required(VERSION VERSION 3.0)
project(tools)

file(GLOB_RECURSE SRC_LIST "${CMAKE_CURRENT_LIST_DIR}/*.cpp")

# add libarary to project
add_library(template ${SRC_LIST} )