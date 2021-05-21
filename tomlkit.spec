#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tomlkit
Version  : 0.7.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/65/ed/7b7216101bc48627b630693b03392f33827901b81d4e1360a76515e3abc4/tomlkit-0.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/ed/7b7216101bc48627b630693b03392f33827901b81d4e1360a76515e3abc4/tomlkit-0.7.2.tar.gz
Summary  : Style preserving TOML library
Group    : Development/Tools
License  : ISC MIT
Requires: tomlkit-license = %{version}-%{release}
Requires: tomlkit-python = %{version}-%{release}
Requires: tomlkit-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang

%description
[github_release]: https://img.shields.io/github/release/sdispater/tomlkit.svg?logo=github&logoColor=white
[pypi_version]: https://img.shields.io/pypi/v/tomlkit.svg?logo=python&logoColor=white
[python_versions]: https://img.shields.io/pypi/pyversions/tomlkit.svg?logo=python&logoColor=white
[github_license]: https://img.shields.io/github/license/sdispater/tomlkit.svg?logo=github&logoColor=white
[travisci]: https://img.shields.io/travis/com/sdispater/tomlkit/master.svg?logo=travis&logoColor=white&label=Travis%20CI
[appveyor]: https://img.shields.io/appveyor/ci/sdispater/tomlkit/master.svg?logo=appveyor&logoColor=white&label=AppVeyor
<!--Codecov logo not offered by shields.io or simpleicons.org, this is Codecov's SVG image modified to be white-->
[codecov]: https://img.shields.io/codecov/c/github/sdispater/tomlkit/master.svg?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CgogPGc+CiAgPHRpdGxlPmJhY2tncm91bmQ8L3RpdGxlPgogIDxyZWN0IGZpbGw9Im5vbmUiIGlkPSJjYW52YXNfYmFja2dyb3VuZCIgaGVpZ2h0PSI0MDIiIHdpZHRoPSI1ODIiIHk9Ii0xIiB4PSItMSIvPgogPC9nPgogPGc+CiAgPHRpdGxlPkxheWVyIDE8L3RpdGxlPgogIDxwYXRoIGlkPSJzdmdfMSIgZmlsbC1ydWxlPSJldmVub2RkIiBmaWxsPSIjZmZmZmZmIiBkPSJtMjUuMDE0LDBjLTEzLjc4NCwwLjAxIC0yNS4wMDQsMTEuMTQ5IC0yNS4wMTQsMjQuODMybDAsMC4wNjJsNC4yNTQsMi40ODJsMC4wNTgsLTAuMDM5YTEyLjIzOCwxMi4yMzggMCAwIDEgOS4wNzgsLTEuOTI4YTExLjg0NCwxMS44NDQgMCAwIDEgNS45OCwyLjk3NWwwLjczLDAuNjhsMC40MTMsLTAuOTA0YzAuNCwtMC44NzQgMC44NjIsLTEuNjk2IDEuMzc0LC0yLjQ0M2MwLjIwNiwtMC4zIDAuNDMzLC0wLjYwNCAwLjY5MiwtMC45MjlsMC40MjcsLTAuNTM1bC0wLjUyNiwtMC40NGExNy40NSwxNy40NSAwIDAgMCAtOC4xLC0zLjc4MWExNy44NTMsMTcuODUzIDAgMCAwIC04LjM3NSwwLjQ5YzIuMDIzLC04Ljg2OCA5LjgyLC0xNS4wNSAxOS4wMjcsLTE1LjA1N2M1LjE5NSwwIDEwLjA3OCwyLjAwNyAxMy43NTIsNS42NTJjMi42MTksMi41OTggNC40MjIsNS44MzUgNS4yMjQsOS4zNzJhMTcuOTA4LDE3LjkwOCAwIDAgMCAtNS4yMDgsLTAuNzlsLTAuMzE4LC0wLjAwMWExOC4wOTYsMTguMDk2IDAgMCAwIC0yLjA2NywwLjE1M2wtMC4wODcsMC4wMTJjLTAuMzAzLDAuMDQgLTAuNTcsMC4wODEgLTAuODEzLDAuMTI2Yy0wLjExOSwwLjAyIC0wLjIzNywwLjA0NSAtMC4zNTUsMC4wNjhjLTAuMjgsMC4wNTcgLTAuNTU0LDAuMTE5IC0wLjgxNiwwLjE4NWwtMC4yODgsMC4wNzNjLTAuMzM2LDAuMDkgLTAuNjc1LDAuMTkxIC0xLjAwNiwwLjNsLTAuMDYxLDAuMDJjLTAuNzQsMC4yNTEgLTEuNDc4LDAuNTU4IC0yLjE5LDAuOTE0bC0wLjA1NywwLjAyOWMtMC4zMTYsMC4xNTggLTAuNjM2LDAuMzMzIC0wLjk3OCwwLjUzNGwtMC4wNzUsMC4wNDVhMTYuOTcsMTYuOTcgMCAwIDAgLTQuNDE0LDMuNzhsLTAuMTU3LDAuMTkxYy0wLjMxNywwLjM5NCAtMC41NjcsMC43MjcgLTAuNzg3LDEuMDQ4Yy0wLjE4NCwwLjI3IC0wLjM2OSwwLjU2IC0wLjYsMC45NDJsLTAuMTI2LDAuMjE3Yy0wLjE4NCwwLjMxOCAtMC4zNDgsMC42MjIgLTAuNDg3LDAuOWwtMC4wMzMsMC4wNjFjLTAuMzU0LDAuNzExIC0wLjY2MSwxLjQ1NSAtMC45MTcsMi4yMTRsLTAuMDM2LDAuMTExYTE3LjEzLDE3LjEzIDAgMCAwIC0wLjg1NSw1LjY0NGwwLjAwMywwLjIzNGEyMy41NjUsMjMuNTY1IDAgMCAwIDAuMDQzLDAuODIyYzAuMDEsMC4xMyAwLjAyMywwLjI1OSAwLjAzNiwwLjM4OGMwLjAxNSwwLjE1OCAwLjAzNCwwLjMxNiAwLjA1MywwLjQ3MWwwLjAxMSwwLjA4OGwwLjAyOCwwLjIxNGMwLjAzNywwLjI2NCAwLjA4LDAuNTI1IDAuMTMsMC43ODdjMC41MDMsMi42MzcgMS43Niw1LjI3NCAzLjYzNSw3LjYyNWwwLjA4NSwwLjEwNmwwLjA4NywtMC4xMDRjMC43NDgsLTAuODg0IDIuNjAzLC0zLjY4NyAyLjc2LC01LjM2OWwwLjAwMywtMC4wMzFsLTAuMDE1LC0wLjAyOGExMS43MzYsMTEuNzM2IDAgMCAxIC0xLjMzMywtNS40MDdjMCwtNi4yODQgNC45NCwtMTEuNTAyIDExLjI0MywtMTEuODhsMC40MTQsLTAuMDE1YzIuNTYxLC0wLjA1OCA1LjA2NCwwLjY3MyA3LjIzLDIuMTM2bDAuMDU4LDAuMDM5bDQuMTk3LC0yLjQ0bDAuMDU1LC0wLjAzM2wwLC0wLjA2MmMwLjAwNiwtNi42MzIgLTIuNTkyLC0xMi44NjUgLTcuMzE0LC0xNy41NTFjLTQuNzE2LC00LjY3OSAtMTAuOTkxLC03LjI1NSAtMTcuNjcyLC03LjI1NSIvPgogPC9nPgo8L3N2Zz4=&label=Codecov

%package license
Summary: license components for the tomlkit package.
Group: Default

%description license
license components for the tomlkit package.


%package python
Summary: python components for the tomlkit package.
Group: Default
Requires: tomlkit-python3 = %{version}-%{release}

%description python
python components for the tomlkit package.


%package python3
Summary: python3 components for the tomlkit package.
Group: Default
Requires: python3-core
Provides: pypi(tomlkit)

%description python3
python3 components for the tomlkit package.


%prep
%setup -q -n tomlkit-0.7.2
cd %{_builddir}/tomlkit-0.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621560972
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tomlkit
cp %{_builddir}/tomlkit-0.7.2/LICENSE %{buildroot}/usr/share/package-licenses/tomlkit/84661790a5df00ab944c2d37978d6ce5ac88e554
cp %{_builddir}/tomlkit-0.7.2/tests/toml-spec-tests/LICENSE %{buildroot}/usr/share/package-licenses/tomlkit/7ad2173ba59937a324cdfe33686e42e2f29ee6ae
cp %{_builddir}/tomlkit-0.7.2/tests/toml-test/COPYING %{buildroot}/usr/share/package-licenses/tomlkit/7a82386b25eb7b8b4fbfd8427349ad9cdddf026d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
rm -rf %{buildroot}/usr/lib/python3*/site-packages/tests
## install_append end

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tomlkit/7a82386b25eb7b8b4fbfd8427349ad9cdddf026d
/usr/share/package-licenses/tomlkit/7ad2173ba59937a324cdfe33686e42e2f29ee6ae
/usr/share/package-licenses/tomlkit/84661790a5df00ab944c2d37978d6ce5ac88e554

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
