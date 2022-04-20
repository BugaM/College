cmake_minimum_required(VERSION 3.10)

cmake_policy(SET CMP0048 NEW)
project(labSort VERSION 0.0.1 LANGUAGES CXX)

include(CMakePrintHelpers)
cmake_print_variables(CMAKE_VERSION)

if(CMAKE_VERSION VERSION_LESS 3.14) 

    # Here is the old cmake magic, for Ubuntu 2018
    #https://crascit.com/2015/07/25/cmake-gtest/

    # Download and unpack googletest at configure time
    configure_file(CMakeLists.txt.in googletest-download/CMakeLists.txt)
    execute_process(COMMAND "${CMAKE_COMMAND}" -G "${CMAKE_GENERATOR}" .
        WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/googletest-download" )
    execute_process(COMMAND "${CMAKE_COMMAND}" --build .
        WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/googletest-download" )

    # Prevent GoogleTest from overriding our compiler/linker options
    # when building with Visual Studio
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

    # Add googletest directly to our build. This adds
    # the following targets: gtest, gtest_main, gmock
    # and gmock_main
    add_subdirectory("${CMAKE_BINARY_DIR}/googletest-src"
                    "${CMAKE_BINARY_DIR}/googletest-build")

    # The gtest/gmock targets carry header search path
    # dependencies automatically when using CMake 2.8.11 or
    # later. Otherwise we have to add them here ourselves.
    if(CMAKE_VERSION VERSION_LESS 2.8.11)
        include_directories("${gtest_SOURCE_DIR}/include"
                            "${gmock_SOURCE_DIR}/include")
    endif()
    
else() # version 3.14 needed for new cmake magic
    # new cmake magic, from gtest docs
    # https://google.github.io/googletest/quickstart-cmake.html
    
    # GoogleTest requires at least C++11
    set(CMAKE_CXX_STANDARD 11)

    include(FetchContent)
        FetchContent_Declare(
        googletest
        # commit e2239 = release 1.11.0 210611
        URL https://github.com/google/googletest/archive/e2239ee6043f73722e7aa812a459f54a28552929.zip
        )
    # For Windows: Prevent overriding the parent project's compiler/linker settings
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)
endif()

# Now simply link your own targets against gtest, gmock,
# etc. as appropriate

include(GoogleTest)

SET(CES12_SRC "src" CACHE FILEPATH "Directory with student sources")

include_directories( ${CES12_SRC} include lib )

FILE(GLOB libLabSortSrc lib/*.cpp)
add_library(libLabSort ${libLabSortSrc})

FILE(GLOB LabSources ${CES12_SRC}/*.cpp)
add_executable(labSorttests test/testSort.cpp ${LabSources})

target_link_libraries(labSorttests gtest gtest_main libLabSort)
 
gtest_discover_tests(labSorttests)




