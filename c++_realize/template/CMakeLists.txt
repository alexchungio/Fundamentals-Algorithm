cmake_minimum_required(VERSION VERSION 2.6)
project(template)


set(HEAD_LIST class_template.h)

# set(SRC_FILE class_template.cpp)
# list(APPEND SRC_FILE )
# list(APPEND SRC_FILE function_template.cpp)
# search file
file(GLOB_RECURSE SRC_LIST "${CMAKE_CURRENT_LIST_DIR}/*.cpp")

# add libarary to project
add_library(template ${SRC_LIST} ${HEAD_LIST})
