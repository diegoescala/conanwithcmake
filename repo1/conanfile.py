from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools.files import copy
import os

class Repo1Recipe(ConanFile):
    name = "repo1"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    options = {"arch": ["armv8", "x86"]}
    default_options = {"arch": "armv8"}
    platform = "armv8"
    
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "Config.cmake.in"

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = "build"
        self.cpp.package.libs = ["repo1"]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # Copy headers preserving the repo1/ subdirectory
        copy(self, "*.h", src=os.path.join(self.source_folder, "include"), 
             dst=os.path.join(self.package_folder, "include"),
             keep_path=True)  # Changed to True to preserve directory structure
        
        # The build_folder is already pointing to the build directory
        lib_src = self.build_folder  # Remove the extra "build" from the path
        lib_dst = os.path.join(self.package_folder, "lib")
        
        self.output.info(f"Copying library from {lib_src} to {lib_dst}")
        copy(self, "librepo1.a", src=lib_src, dst=lib_dst, keep_path=False)
        
        # Verify the copy
        if os.path.exists(os.path.join(lib_dst, "librepo1.a")):
            self.output.info("Library successfully copied!")
        else:
            self.output.error("Library not copied to destination!")
            # Add more debug info
            self.output.info(f"Contents of {lib_src}:")
            for root, dirs, files in os.walk(lib_src):
                for file in files:
                    if file.endswith('.a'):
                        self.output.info(f"Found .a file: {os.path.join(root, file)}")

    def package_info(self):
        self.cpp_info.libs = ["repo1"]  # Name of your library
        self.cpp_info.includedirs = ["include"]  # Specify include directory
