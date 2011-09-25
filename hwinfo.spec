Summary:	hwinfo - the hardware detection tool used in SuSE Linux
Summary(pl.UTF-8):	hwinfo - narzędzie do wykrywania sprzętu używane w SuSE Linuksie
Name:		hwinfo
Version:	16.0
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/h/hwinfo/%{name}_%{version}.orig.tar.gz
# Source0-md5:	b7e5cae47a373b75abd5a4a5f7584b98
Patch0:		%{name}-kbd.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-x86_64.patch
Patch3:		%{name}-update-vm86.patch
URL:		http://packages.qa.debian.org/h/hwinfo.html
BuildRequires:	dbus-devel >= 0.35
BuildRequires:	flex
BuildRequires:	hal-devel
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
%setup -q
%patch0 -p0
%patch1 -p1
%if "%{_lib}" == "lib64"
%patch2 -p1
%endif
%patch3 -p1

%build
%{__make} -j1 \
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
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libhd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libhd.so.??
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhd.so
%{_includedir}/hd.h
%{_pkgconfigdir}/hwinfo.pc
