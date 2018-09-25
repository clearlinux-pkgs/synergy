#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : synergy
Version  : 1.10.1.stable
Release  : 2
URL      : https://github.com/symless/synergy-core/archive/v1.10.1-stable.tar.gz
Source0  : https://github.com/symless/synergy-core/archive/v1.10.1-stable.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 OpenSSL
Requires: synergy-bin
Requires: synergy-data
Requires: synergy-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : glibc-dev
BuildRequires : libX11-dev
BuildRequires : libXtst-dev
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : python3
Patch1: 0001-Use-target_link_libraries-instead-of-qt5_use_modules.patch
Patch2: 0002-Add-missing-header-includes-to-build-against-Qt-5.11.patch
Patch3: 0003-disable-zeroconf-and-dns_sd.patch

%description
Google C++ Testing Framework
============================
http://code.google.com/p/googletest/

%package bin
Summary: bin components for the synergy package.
Group: Binaries
Requires: synergy-data = %{version}-%{release}
Requires: synergy-license = %{version}-%{release}

%description bin
bin components for the synergy package.


%package data
Summary: data components for the synergy package.
Group: Data

%description data
data components for the synergy package.


%package license
Summary: license components for the synergy package.
Group: Default

%description license
license components for the synergy package.


%prep
%setup -q -n synergy-core-1.10.1-stable
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537901910
mkdir -p clr-build
pushd clr-build
%cmake .. $(grep -v '^#' ../Build.properties | while read variable; do echo "-D${variable// /}"; done)
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1537901910
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/synergy
cp LICENSE %{buildroot}/usr/share/package-licenses/synergy/LICENSE
cp ext/gmock/COPYING %{buildroot}/usr/share/package-licenses/synergy/ext_gmock_COPYING
cp ext/gmock/scripts/generator/COPYING %{buildroot}/usr/share/package-licenses/synergy/ext_gmock_scripts_generator_COPYING
cp ext/gtest/COPYING %{buildroot}/usr/share/package-licenses/synergy/ext_gtest_COPYING
cp ext/openssl/LICENSE %{buildroot}/usr/share/package-licenses/synergy/ext_openssl_LICENSE
cp res/License.rtf %{buildroot}/usr/share/package-licenses/synergy/res_License.rtf
cp res/License.tex %{buildroot}/usr/share/package-licenses/synergy/res_License.tex
cp src/gui/src/LicenseManager.h %{buildroot}/usr/share/package-licenses/synergy/src_gui_src_LicenseManager.h
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/synergy
/usr/bin/synergyc
/usr/bin/synergys
/usr/bin/syntool

%files data
%defattr(-,root,root,-)
%exclude /usr/share/package-licenses/synergy/src_gui_src_LicenseManager.h
/usr/share/applications/synergy.desktop
/usr/share/icons/hicolor/scalable/apps/synergy.svg
/usr/share/package-licenses/synergy/res_License.rtf
/usr/share/package-licenses/synergy/res_License.tex

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/synergy/LICENSE
/usr/share/package-licenses/synergy/ext_gmock_COPYING
/usr/share/package-licenses/synergy/ext_gmock_scripts_generator_COPYING
/usr/share/package-licenses/synergy/ext_gtest_COPYING
/usr/share/package-licenses/synergy/ext_openssl_LICENSE
