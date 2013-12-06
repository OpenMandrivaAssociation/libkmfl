%define major	0
%define libname %mklibname kmfl %{major}
%define devname %mklibname kmfl -d

Summary:	Keystroke interpreter for Tavultesoft Keyman files
Name:		libkmfl
Version:	0.9.9
Release:	2
Group:		System/Internationalization
License:	GPLv2+
Url:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
Patch0:		libkmfl-0.9.8-fix-linkage.patch
BuildRequires:	kmflcomp-devel >= %{version}

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

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%setup -q
%patch0 -p0

%build
%define _disable_ld_no_undefined 1
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%files -n %{libname}
%{_libdir}/libkmfl.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog
%{_includedir}/kmfl/libkmfl.h
%{_libdir}/libkmfl.so

