#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-spatstat.utils
Version  : 3.1.1
Release  : 70
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/spatstat.utils_3.1-1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/spatstat.utils_3.1-1.tar.gz
Summary  : Utility Functions for 'spatstat'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.utils-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
which may also be useful for other purposes.

%package lib
Summary: lib components for the R-spatstat.utils package.
Group: Libraries

%description lib
lib components for the R-spatstat.utils package.


%prep
%setup -q -n spatstat.utils
pushd ..
cp -a spatstat.utils buildavx2
popd
pushd ..
cp -a spatstat.utils buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731651776

%install
export SOURCE_DATE_EPOCH=1731651776
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/spatstat.utils/NEWS
/usr/lib64/R/library/spatstat.utils/R/spatstat.utils
/usr/lib64/R/library/spatstat.utils/R/spatstat.utils.rdb
/usr/lib64/R/library/spatstat.utils/R/spatstat.utils.rdx
/usr/lib64/R/library/spatstat.utils/R/sysdata.rdb
/usr/lib64/R/library/spatstat.utils/R/sysdata.rdx
/usr/lib64/R/library/spatstat.utils/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.utils/help/AnIndex
/usr/lib64/R/library/spatstat.utils/help/aliases.rds
/usr/lib64/R/library/spatstat.utils/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.utils/help/paths.rds
/usr/lib64/R/library/spatstat.utils/help/spatstat.utils.rdb
/usr/lib64/R/library/spatstat.utils/help/spatstat.utils.rdx
/usr/lib64/R/library/spatstat.utils/html/00Index.html
/usr/lib64/R/library/spatstat.utils/html/R.css
/usr/lib64/R/library/spatstat.utils/info/packagesizes.txt
/usr/lib64/R/library/spatstat.utils/tests/circleseg.R
/usr/lib64/R/library/spatstat.utils/tests/fmla.R
/usr/lib64/R/library/spatstat.utils/tests/indices.R
/usr/lib64/R/library/spatstat.utils/tests/numerical.R
/usr/lib64/R/library/spatstat.utils/tests/segments.R
/usr/lib64/R/library/spatstat.utils/tests/tekst.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/spatstat.utils/libs/spatstat.utils.so
/V4/usr/lib64/R/library/spatstat.utils/libs/spatstat.utils.so
/usr/lib64/R/library/spatstat.utils/libs/spatstat.utils.so
