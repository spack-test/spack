# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdoDb(RPackage):
    """A set of annotation maps describing the entire Human Disease Ontology.

    A set of annotation maps describing the entire Human Disease Ontology
    assembled using data from DO.  Its annotation data comes from
    https://github.com/DiseaseOntology/HumanDiseaseOntology/tree/main/src/ontology."""

    url = "https://bioconductor.org/packages/release/data/annotation/src/contrib/HDO.db_0.99.1.tar.gz"
    bioc = "HDO.db"

    version("0.99.1", sha256="c17cf28d06621d91148a64d47fdeaa906d8621aba7a688715fb9571a55f7cf92")

    depends_on("r@4.2.0:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
