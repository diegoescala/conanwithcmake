from conan import ConanFile
from conan.tools.cmake import CMake

class Repo1Recipe(ConanFile):
    name = "repo1"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
