#
# TODO:
# - polish description
# group sys/apps
Summary:	hwinfo is the hardware detection tool used in SuSE Linux.
Name:		hwinfo
Version:	13.11
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.debian.org/debian/pool/main/h/hwinfo/%{name}_%{version}.orig.tar.gz
# Source0-md5:	afc560ebe9404fcb1553bc9ebda69700
Patch0:		%{name}-kbd.patch
URL:		http://packages.qa.debian.org/h/hwinfo.html
BuildRequires:	hal-devel
BuildRequires:	dbus-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwinfo is the hardware detection tool used in SuSE Linux.

%prep
%setup -q
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libhd.so*
/usr/sbin
%attr(644,root,root) %{_includedir}
%attr(644,root,root) %{_libdir}/pkgconfig/hwinfo.pc
%attr(644,root,root) %{_datadir}/%{name}
