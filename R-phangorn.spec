#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-phangorn
Version  : 2.7.0
Release  : 26
URL      : https://cran.r-project.org/src/contrib/phangorn_2.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/phangorn_2.7.0.tar.gz
Summary  : Phylogenetic Reconstruction and Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-phangorn-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-ape
Requires: R-fastmatch
Requires: R-igraph
Requires: R-magrittr
Requires: R-quadprog
BuildRequires : R-Rcpp
BuildRequires : R-ape
BuildRequires : R-fastmatch
BuildRequires : R-igraph
BuildRequires : R-magrittr
BuildRequires : R-quadprog
BuildRequires : buildreq-R

%description
using Maximum Likelihood, Maximum Parsimony, distance methods and
    Hadamard conjugation. Offers methods for tree comparison, model
    selection and visualization of phylogenetic networks as described in

%package lib
Summary: lib components for the R-phangorn package.
Group: Libraries

%description lib
lib components for the R-phangorn package.


%prep
%setup -q -c -n phangorn
cd %{_builddir}/phangorn

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620065676

%install
export SOURCE_DATE_EPOCH=1620065676
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phangorn
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phangorn
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library phangorn
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/phangorn/CITATION
/usr/lib64/R/library/phangorn/DESCRIPTION
/usr/lib64/R/library/phangorn/INDEX
/usr/lib64/R/library/phangorn/Meta/Rd.rds
/usr/lib64/R/library/phangorn/Meta/data.rds
/usr/lib64/R/library/phangorn/Meta/features.rds
/usr/lib64/R/library/phangorn/Meta/hsearch.rds
/usr/lib64/R/library/phangorn/Meta/links.rds
/usr/lib64/R/library/phangorn/Meta/nsInfo.rds
/usr/lib64/R/library/phangorn/Meta/package.rds
/usr/lib64/R/library/phangorn/Meta/vignette.rds
/usr/lib64/R/library/phangorn/NAMESPACE
/usr/lib64/R/library/phangorn/NEWS
/usr/lib64/R/library/phangorn/R/phangorn
/usr/lib64/R/library/phangorn/R/phangorn.rdb
/usr/lib64/R/library/phangorn/R/phangorn.rdx
/usr/lib64/R/library/phangorn/R/sysdata.rdb
/usr/lib64/R/library/phangorn/R/sysdata.rdx
/usr/lib64/R/library/phangorn/README
/usr/lib64/R/library/phangorn/data/Laurasiatherian.RData
/usr/lib64/R/library/phangorn/data/chloroplast.RData
/usr/lib64/R/library/phangorn/data/yeast.RData
/usr/lib64/R/library/phangorn/doc/AdvancedFeatures.R
/usr/lib64/R/library/phangorn/doc/AdvancedFeatures.Rmd
/usr/lib64/R/library/phangorn/doc/AdvancedFeatures.html
/usr/lib64/R/library/phangorn/doc/Ancestral.R
/usr/lib64/R/library/phangorn/doc/Ancestral.Rmd
/usr/lib64/R/library/phangorn/doc/Ancestral.html
/usr/lib64/R/library/phangorn/doc/IntertwiningTreesAndNetworks.R
/usr/lib64/R/library/phangorn/doc/IntertwiningTreesAndNetworks.Rmd
/usr/lib64/R/library/phangorn/doc/IntertwiningTreesAndNetworks.html
/usr/lib64/R/library/phangorn/doc/Networx.R
/usr/lib64/R/library/phangorn/doc/Networx.Rmd
/usr/lib64/R/library/phangorn/doc/Networx.html
/usr/lib64/R/library/phangorn/doc/Trees.R
/usr/lib64/R/library/phangorn/doc/Trees.Rmd
/usr/lib64/R/library/phangorn/doc/Trees.html
/usr/lib64/R/library/phangorn/doc/index.html
/usr/lib64/R/library/phangorn/extdata/Blosum62.dat
/usr/lib64/R/library/phangorn/extdata/Dayhoff.dat
/usr/lib64/R/library/phangorn/extdata/FLU.dat
/usr/lib64/R/library/phangorn/extdata/HIVb.dat
/usr/lib64/R/library/phangorn/extdata/HIVw.dat
/usr/lib64/R/library/phangorn/extdata/JTT.dat
/usr/lib64/R/library/phangorn/extdata/MtZoa.dat
/usr/lib64/R/library/phangorn/extdata/RtREV.dat
/usr/lib64/R/library/phangorn/extdata/VT.dat
/usr/lib64/R/library/phangorn/extdata/cpREV.dat
/usr/lib64/R/library/phangorn/extdata/dayhoff-dcmut.dat
/usr/lib64/R/library/phangorn/extdata/jtt-dcmut.dat
/usr/lib64/R/library/phangorn/extdata/lg.dat
/usr/lib64/R/library/phangorn/extdata/mtArt.dat
/usr/lib64/R/library/phangorn/extdata/mtREV24.dat
/usr/lib64/R/library/phangorn/extdata/mtmam.dat
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bestTree.3moles
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bestTree.AIs
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bestTree.Wang.out
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bestTree.YCh
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bestTree.mtG
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitions.3moles
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitions.AIs
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitions.YCh
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitions.mtG
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitions.woodmouse
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitionsBranchLabels.3moles
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitionsBranchLabels.AIs
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitionsBranchLabels.YCh
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bipartitionsBranchLabels.mtG
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bootstrap.3moles
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bootstrap.AIs
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bootstrap.Wang.out
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bootstrap.YCh
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bootstrap.mtG
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_bootstrap.woodmouse
/usr/lib64/R/library/phangorn/extdata/trees/RAxML_distances.Wang.nxs
/usr/lib64/R/library/phangorn/extdata/trees/Splits.txt
/usr/lib64/R/library/phangorn/extdata/trees/primates.dna
/usr/lib64/R/library/phangorn/extdata/trees/woodmouse.fasta
/usr/lib64/R/library/phangorn/extdata/trees/woodmouse.mrbayes.nex.con
/usr/lib64/R/library/phangorn/extdata/trees/woodmouse.mrbayes.nex.run1.t
/usr/lib64/R/library/phangorn/extdata/trees/woodmouse.mrbayes.nex.run2.t
/usr/lib64/R/library/phangorn/extdata/trees/woodmouse.nxs
/usr/lib64/R/library/phangorn/extdata/wag.dat
/usr/lib64/R/library/phangorn/help/AnIndex
/usr/lib64/R/library/phangorn/help/aliases.rds
/usr/lib64/R/library/phangorn/help/paths.rds
/usr/lib64/R/library/phangorn/help/phangorn.rdb
/usr/lib64/R/library/phangorn/help/phangorn.rdx
/usr/lib64/R/library/phangorn/html/00Index.html
/usr/lib64/R/library/phangorn/html/R.css
/usr/lib64/R/library/phangorn/phangorn_sticker.png
/usr/lib64/R/library/phangorn/tests/tinytest.R
/usr/lib64/R/library/phangorn/tinytest/test_Clanistics.R
/usr/lib64/R/library/phangorn/tinytest/test_SH.R
/usr/lib64/R/library/phangorn/tinytest/test_ancestral.R
/usr/lib64/R/library/phangorn/tinytest/test_bootstrap.R
/usr/lib64/R/library/phangorn/tinytest/test_codon.R
/usr/lib64/R/library/phangorn/tinytest/test_dist_tree.R
/usr/lib64/R/library/phangorn/tinytest/test_distances.R
/usr/lib64/R/library/phangorn/tinytest/test_hadamard.R
/usr/lib64/R/library/phangorn/tinytest/test_mast.R
/usr/lib64/R/library/phangorn/tinytest/test_modelTest.R
/usr/lib64/R/library/phangorn/tinytest/test_parsimony.R
/usr/lib64/R/library/phangorn/tinytest/test_phyDat.R
/usr/lib64/R/library/phangorn/tinytest/test_pml.R
/usr/lib64/R/library/phangorn/tinytest/test_pmlCluster.R
/usr/lib64/R/library/phangorn/tinytest/test_pmlMix.R
/usr/lib64/R/library/phangorn/tinytest/test_pmlPart.R
/usr/lib64/R/library/phangorn/tinytest/test_pmlPen.R
/usr/lib64/R/library/phangorn/tinytest/test_speciesTree.R
/usr/lib64/R/library/phangorn/tinytest/test_splits.R
/usr/lib64/R/library/phangorn/tinytest/test_superTree.R
/usr/lib64/R/library/phangorn/tinytest/test_treeManipulation.R
/usr/lib64/R/library/phangorn/tinytest/test_treeRearrangement.R
/usr/lib64/R/library/phangorn/tinytest/test_treedist.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/phangorn/libs/phangorn.so
/usr/lib64/R/library/phangorn/libs/phangorn.so.avx2
/usr/lib64/R/library/phangorn/libs/phangorn.so.avx512
