# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class JediFv3MinEnv(BundlePackage):
    """Development environment for fv3-bundle"""

    homepage = "https://github.com/JCSDA/fv3-bundle"
    git = "https://github.com/JCSDA/fv3-bundle.git"

    maintainers("")

    version("1.0.0")

    # Variants defining packages that we cannot distribute publicly
    # Need to find a free fftw provider for fftw-api ...
    variant("fftw", default=True, description="Build fftw")
    variant("hdf4", default=True, description="Build hdf4 library and python hdf module")

    depends_on("base-env", type="run")
    depends_on("bison", type="run")
    depends_on("blas", type="run")
    depends_on("boost", type="run")
    depends_on("bufr", type="run")
    # Force users to load manually
    # depends_on("crtm@v2.4.1-jedi", type="run")
    depends_on("ecbuild", type="run")
#    depends_on("eccodes", type="run")   ygyu
    depends_on("eckit", type="run")
    depends_on("ecmwf-atlas", type="run")
    depends_on("eigen", type="run")
    depends_on("fckit", type="run")
    depends_on("fftw-api", when="+fftw", type="run")
#    depends_on("flex", type="run")
#    depends_on("gsibec", type="run")
    depends_on("gsl-lite", type="run")
    depends_on("hdf", when="+hdf4", type="run")
    depends_on("jedi-cmake", type="run")
    depends_on("netcdf-cxx4", type="run")
#    depends_on("ncview", type="run")               # later
    depends_on("nlohmann-json", type="run")
    depends_on("nlohmann-json-schema-validator", type="run")
#    depends_on("odc", type="run")
    depends_on("sp", type="run", when="^ip@:4")
    depends_on("udunits", type="run")

    depends_on("fms", type="run")      # for FV3

    # There is no need for install() since there is no code.

    conflicts(
        "%gcc platform=darwin",
        msg="jedi-base-env does not build with gcc on macOS, use apple-clang",
    )

    # There is no need for install() since there is no code.
