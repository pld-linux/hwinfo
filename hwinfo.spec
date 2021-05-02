#
# Conditional build:
%bcond_with	hal	# HAL support

Summary:	hwinfo - the hardware detection tool used in SuSE Linux
Summary(pl.UTF-8):	hwinfo - narzędzie do wykrywania sprzętu używane w SuSE Linuksie
Name:		hwinfo
Version:	21.72
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://ftp.debian.org/debian/pool/main/h/hwinfo/%{name}_%{version}.orig.tar.gz
# Source0-md5:	d33995be010185840f99c4eff4f699f0
Patch0:		%{name}-kbd.patch
URL:		http://packages.qa.debian.org/h/hwinfo.html
BuildRequires:	flex
%{?with_hal:BuildRequires:	hal-devel}
%ifarch %{ix86} %{x8664} x32
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
%setup -q
%patch0 -p0

# these should be in tarball, but aren't (21.6)
test -e VERSION || echo %{version} > VERSION
test -e changelog || touch changelog

%build
%{__make} -j1 \
	VERSION=%{version} \
	ARCH=%{_target_base_arch} \
	CC="%{__cc}" \
	LIBDIR=%{_libdir} \
	RPM_OPT_FLAGS="%{rpmcflags} %{?with_hal:-DWITH_HAL}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc MAINTAINER README.md changelog
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
