add_library(index SHARED ${GEN_DIR}/index.cpp)

add_custom_command(
    OUTPUT ${GEN_DIR}/index.h ${GEN_DIR}/index.cpp
    COMMAND python3 ${GEN_DIR}/preparing.py ${GEN_DIR}/index.h ${GEN_DIR}/index.cpp
    COMMENT "RUNNING PY"
    WORKING_DIRECTORY ${GEN_DIR}
)


target_compile_features(index PUBLIC cxx_std_17)

target_include_directories(index PRIVATE ${CMAKE_BINARY_DIR})
