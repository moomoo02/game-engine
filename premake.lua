workspace "game-engine"
    startproject "engine"
    architecture "x64"

    configurations
    {
        "Debug",
        "Release"
    }

project "engine"
    location "engine"
    kind "ConsoleApp"
    language "C++"
    cppdialect "C++17"

    files
    {
        "%{prj.name}/src/**.h",
        "%{prj.name}/src/**.cpp",
    }

    flags
    {
        "FatalWarnings"
    }