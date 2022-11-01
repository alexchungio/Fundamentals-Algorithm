cmake_minimum_required(VERSION VERSION 2.6)
project(linked_list)

file(GLOB_RECURSE SRC_LIST "${CMAKE_CURRENT_LIST_DIR}/*.cpp")
file(GLOB_RECURSE HEAD_LIST "${CMAKE_CURRENT_LIST_DIR}/*.hpp")

add_library(linked_list ${SRC_LIST} ${HEAD_LIST})
