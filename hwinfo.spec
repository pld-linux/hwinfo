Summary:	hwinfo - the hardware detection tool used in SuSE Linux
Summary(pl.UTF-8):	hwinfo - narzędzie do wykrywania sprzętu używane w SuSE Linuksie
Name:		hwinfo
Version:	21.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/h/hwinfo/%{name}_%{version}.orig.tar.gz
# Source0-md5:	594f879cf646131057f7e8e296ec6cf9
Patch0:		%{name}-kbd.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-x86_64.patch
URL:		http://packages.qa.debian.org/h/hwinfo.html
BuildRequires:	dbus-devel >= 0.35
BuildRequires:	flex
BuildRequires:	hal-devel
%ifarch %{ix86} %{x8664}
BuildRequires:	libx86emu-devel >= 1
%endif
BuildRequires:	linux-libc-headers >= 7:2.6.20
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwinfo is the hardware detection tool used in SuSE Linux.

%description -l pl.UTF-8
hwinfo to narzędzie do wykrywania sprzętu używane w SuSE Linuksie.

%package devel
Summary:	Header files for hwinfo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hwinfo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for hwinfo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hwinfo.

%prep
%setup -q -c
%patch0 -p0
%patch1 -p1
%if "%{_lib}" == "lib64"
%patch2 -p1
%endif

%build
%{__make} -j1 \
	ARCH=%{_target_base_arch} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc MAINTAINER README changelog
%attr(755,root,root) %{_sbindir}/check_hd
%attr(755,root,root) %{_sbindir}/convert_hd
%attr(755,root,root) %{_sbindir}/getsysinfo
%attr(755,root,root) %{_sbindir}/hwinfo
%attr(755,root,root) %{_sbindir}/mk_isdnhwdb
%attr(755,root,root) %{_libdir}/libhd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libhd.so.21
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhd.so
%{_includedir}/hd.h
%{_pkgconfigdir}/hwinfo.pc
