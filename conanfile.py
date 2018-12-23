from conans import ConanFile, CMake, tools


class PcgcppConan(ConanFile):
    name = "pcg-cpp"
    version = "0.1"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        self.run("git clone https://github.com/imneme/pcg-cpp")
        self.run("cd pcg-cpp")
