%define major 0
%define libname %mklibname kmfl %{major}
%define develname %mklibname kmfl -d

Name:		libkmfl
Summary:	Keystroke interpreter for Tavultesoft Keyman files
Version:	0.9.8
Release:	%mkrel 2
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
Patch0:		libkmfl-0.9.8-fix-linkage.patch
BuildRequires:	kmflcomp-devel >= %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

libkmfl is one of three parts of the KMFL project. It provides an 
engine to interpret compiled KMFL keyboard tables. The other two parts
are kmflcomp and libscim-kmfl-imengine.

%package -n	%{libname}
Summary:	KMFL library
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

libkmfl is one of three parts of the KMFL project. It provides an 
engine to interpret compiled KMFL keyboard tables. The other two parts
are kmflcomp and libscim-kmfl-imengine.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname kmfl 0 -d}

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q
%patch0 -p0

%build
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libkmfl.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_includedir}/kmfl/libkmfl.h
%{_libdir}/libkmfl.la
%{_libdir}/libkmfl.a
%{_libdir}/libkmfl.so
