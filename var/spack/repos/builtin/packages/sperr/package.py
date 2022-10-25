# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Sperr(CMakePackage):
    """SPERR is a lossy scientific (floating-point) data compressor that can
    perform either error-bounded or size-bounded data compression"""

    homepage = "https://github.com/NCAR/SPERR"
    git = homepage

    version("2022.07.18", commit="640305d049db9e9651ebdd773e6936e2c028ff3a")
    version("2022.05.26", commit="7894a5fe1b5ca5a4aaa952d1779dfc31fd741243")

    depends_on("git", type="build")
    depends_on("zstd", type=("build", "link"), when="+zstd")
    depends_on("pkgconf", type=("build"), when="+zstd")

    variant("shared", description="build shared libaries", default=True)
    variant("zstd", description="use Zstd for more compression", default=True)
    variant("openmp", description="use openmp for acceleration", default=True)

    maintainers = ["shaomeng", "robertu94"]

    def cmake_args(self):
        # ensure the compiler supports OpenMP if it is used
        if "+openmp" in self.spec:
            self.compiler.openmp_flag

        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("USE_ZSTD", "zstd"),
            self.define_from_variant("USE_OMP", "openmp"),
            "-DSPERR_PREFER_RPATH=OFF",
            "-DUSE_BUNDLED_ZSTD=OFF",
            "-DBUILD_CLI_UTILITIES=OFF",
            "-DBUILD_UNIT_TESTS=OFF",
        ]
        return args
