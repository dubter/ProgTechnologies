cmake_minimum_required(VERSION 3.20.0)
project(task2)

set(CMAKE_CXX_STANDARD 14)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set(GEN_DIR "${PROJECT_SOURCE_DIR}/A")
set(LIB_DIR "${PROJECT_SOURCE_DIR}/B")
set(SRC_DIR "${PROJECT_SOURCE_DIR}/C")
add_subdirectory(A)
add_subdirectory(B)
add_subdirectory(C)
