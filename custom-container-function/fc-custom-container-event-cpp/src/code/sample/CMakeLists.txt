cmake_minimum_required(VERSION 3.7)

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_GLIBCXX_USE_CXX11_ABI=0")

find_package(OpenCV REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/../include)
include_directories(${CMAKE_SOURCE_DIR}/../third-party/rapidjson/include)
include_directories(${CMAKE_SOURCE_DIR}/include)
include_directories( ${OpenCV_INCLUDE_DIRS} )
link_directories(${CMAKE_SOURCE_DIR}/../bin)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_definitions(-D_GLIBCXX_USE_CXX11_ABI=1)

project(bootstrap)

set(RUNTIME_SOURCE_FILES ${CMAKE_SOURCE_DIR}/src/register_handler.cpp ${CMAKE_SOURCE_DIR}/src/handlers/echo_handler.cpp)

add_executable(bootstrap ${RUNTIME_SOURCE_FILES})
set_target_properties(bootstrap PROPERTIES
                      RUNTIME_OUTPUT_DIRECTORY ../../bin/)
target_link_libraries(bootstrap pthread cppruntime ${OpenCV_LIBS})