#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.utils
Version  : 1.9.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/spatstat.utils_1.9-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.utils_1.9-0.tar.gz
Summary  : Utility Functions for 'spatstat'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.utils-lib
BuildRequires : clr-R-helpers

%description
which may also be useful for other purposes.

%package lib
Summary: lib components for the R-spatstat.utils package.
Group: Libraries

%description lib
lib components for the R-spatstat.utils package.


%prep
%setup -q -c -n spatstat.utils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532874896

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532874896
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.utils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.utils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.utils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library spatstat.utils|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.utils/DESCRIPTION
/usr/lib64/R/library/spatstat.utils/INDEX
/usr/lib64/R/library/spatstat.utils/Meta/Rd.rds
/usr/lib64/R/library/spatstat.utils/Meta/features.rds
/usr/lib64/R/library/spatstat.utils/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.utils/Meta/links.rds
/usr/lib64/R/library/spatstat.utils/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.utils/Meta/package.rds
/usr/lib64/R/library/spatstat.utils/NAMESPACE
/usr/lib64/R/library/spatstat.utils/R/spatstat.utils
/usr/lib64/R/library/spatstat.utils/R/spatstat.utils.rdb
/usr/lib64/R/library/spatstat.utils/R/spatstat.utils.rdx
/usr/lib64/R/library/spatstat.utils/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.utils/help/AnIndex
/usr/lib64/R/library/spatstat.utils/help/aliases.rds
/usr/lib64/R/library/spatstat.utils/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.utils/help/paths.rds
/usr/lib64/R/library/spatstat.utils/help/spatstat.utils.rdb
/usr/lib64/R/library/spatstat.utils/help/spatstat.utils.rdx
/usr/lib64/R/library/spatstat.utils/html/00Index.html
/usr/lib64/R/library/spatstat.utils/html/R.css
/usr/lib64/R/library/spatstat.utils/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.utils/libs/spatstat.utils.so
/usr/lib64/R/library/spatstat.utils/libs/spatstat.utils.so.avx2
/usr/lib64/R/library/spatstat.utils/libs/spatstat.utils.so.avx512
