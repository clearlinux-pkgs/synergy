#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : synergy
Version  : 1.14.6.19
Release  : 15
URL      : https://github.com/symless/synergy-core/archive/1.14.6.19-stable/synergy-core-1.14.6.19.tar.gz
Source0  : https://github.com/symless/synergy-core/archive/1.14.6.19-stable/synergy-core-1.14.6.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: synergy-bin = %{version}-%{release}
Requires: synergy-data = %{version}-%{release}
Requires: synergy-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : libX11-dev
BuildRequires : libXtst-dev
BuildRequires : libxkbfile-dev
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pugixml-dev
BuildRequires : qtbase-dev
BuildRequires : qttools-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-target_link_libraries-instead-of-qt5_use_modules.patch

%description
# Synergy Core
This is the open source core component of Synergy, a keyboard and mouse sharing tool.

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
%setup -q -n synergy-core-1.14.6.19-stable
cd %{_builddir}/synergy-core-1.14.6.19-stable
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683915452
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. $(grep -v '^#' ../Build.properties | while read variable; do echo "-D${variable// /}"; done) \
-DBUILD_TESTS=OFF \
-DSYSTEM_PUGIXML=ON
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1683915452
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/synergy
cp %{_builddir}/synergy-core-%{version}-stable/LICENSE %{buildroot}/usr/share/package-licenses/synergy/395b7e59bf458e5fc394dfda946d656126941f64 || :
cp %{_builddir}/synergy-core-%{version}-stable/res/License.rtf %{buildroot}/usr/share/package-licenses/synergy/f801798afe701ce87c20062a6a514d1ab7bf5185 || :
cp %{_builddir}/synergy-core-%{version}-stable/res/License.tex %{buildroot}/usr/share/package-licenses/synergy/28c8b9f7de43754bf7dfa7ddef3dabd54d257cd2 || :
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/share/package-licenses/synergy/src_gui_src_LicenseManager.h

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/synergy
/usr/bin/synergy-core
/usr/bin/synergyc
/usr/bin/synergys
/usr/bin/syntool

%files data
%defattr(-,root,root,-)
/usr/share/applications/synergy.desktop
/usr/share/icons/hicolor/scalable/apps/synergy.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/synergy/28c8b9f7de43754bf7dfa7ddef3dabd54d257cd2
/usr/share/package-licenses/synergy/395b7e59bf458e5fc394dfda946d656126941f64
/usr/share/package-licenses/synergy/f801798afe701ce87c20062a6a514d1ab7bf5185
