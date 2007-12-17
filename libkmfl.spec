%define name	libkmfl
%define version	0.9.6
%define release	%mkrel 1

%define major		0
%define libname		%mklibname kmfl %{major}
%define develname	%mklibname kmfl -d

Name:		%{name}
Summary:	Keystroke interpreter for Tavultesoft Keyman files
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
BuildRequires:	libkmflcomp-devel 

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

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libkmfl.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_includedir}/kmfl/libkmfl.h
%{_libdir}/libkmfl.la
%{_libdir}/libkmfl.a
%{_libdir}/libkmfl.so
