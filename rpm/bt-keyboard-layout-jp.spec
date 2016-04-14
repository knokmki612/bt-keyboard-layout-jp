Name: bt-keyboard-layout-jp
Version: 1.0.0
Release: 2
Summary: Addittional layout of bluetooth keyboard for Japanese
URL: https://github.com/knokmki612/bt-keyboard-layout-jp
License: MIT
Source: %{name}-%{version}.tar.gz
Buildarch: noarch
Requires: patchmanager
Requires: jolla-settings
Requires: sailfish-version >= 2.0.0

%description
Can be able to use Japanese layout via bluetooth keyboard on Sailfish OS.

%define debug_package %{nil}

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
