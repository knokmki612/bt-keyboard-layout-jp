Name: bt-keyboard-layout-jp
Version: 1.0.0
Release: 2
%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary: Addittional layout of bluetooth keyboard for Japanese
URL: https://github.com/knokmki612/bt-keyboard-layout-jp
License: MIT
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
BuildRequires: qt5-qttools-kmap2qmap
Requires: patchmanager
Requires: jolla-settings
Requires: sailfish-version >= 2.0.0

%description
Can be able to use Japanese layout via bluetooth keyboard on Sailfish OS.

%define debug_package %{nil}

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 SPECVERSION=%{version}
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}
%qmake5_install

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
	/usr/sbin/patchmanager -u %{name} || true
fi

%post
cd /usr/share/qt5/keymaps
if [ -f boston.qmap ]; then
	mv boston.qmap boston.qmap.orig
	mv jp.qmap boston.qmap
fi
if [ -f droid.qmap ]; then
	mv droid.qmap droid.qmap.orig
	mv jp.qmap droid.qmap
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
	/usr/sbin/patchmanager -u %{name} || true
fi
cd /usr/share/qt5/keymaps
if [ -f boston.qmap ]; then
	cd /usr/share/qt5/keymaps
	mv boston.qmap jp.qmap
	mv boston.qmap.orig boston.qmap
fi
if [ -f droid.qmap ]; then
	cd /usr/share/qt5/keymaps
	mv droid.qmap jp.qmap
	mv droid.qmap.orig droid.qmap
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
%{_datadir}/qt5/keymaps/
