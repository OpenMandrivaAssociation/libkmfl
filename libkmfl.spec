%define version	0.8
%define release	%mkrel 3

%define major 0
%define libname %mklibname kmfl %{major}


Name:		libkmfl
Summary:	Keystroke interpreter for Tavultesoft Keyman files
Version:		%{version}
Release:		%{release}
Requires:	libkmflcomp-devel
Group:		System/Internationalization
License:		GPL
URL:			http://kmfl.sourceforge.net/
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		automake1.8
BuildRequires:          libkmflcomp-devel 

%description
libkmfl is a keystroke interpreter for Tavultesoft Keyman files.

KMFL means "Keyboard Mapping For Linux", but it is not for 
general purposes. It is for Tavultesoft Keyman.
KMFL is being jointly developed by SIL International and Tavultesoft.

Keyman is a proprietary software for keyboard mapping.
It runs on MS Windows.
See the screenshot:
http://www.tavultesoft.com/keymandev/screenshot.php

Some Keyman users provide the binary Keyman files,
http://www.tavultesoft.com/keyman/downloads/keyboards/
but they don't work with libkmfl.

You need the source Keyman files.
For example, get "IPAUni_Src105.zip".
http://208.145.80.131/cms/scripts/page.php?site_id=nrsi&item_id=UniIPAKeyboard
It includes "IPAUni10.kmn". That is a source Keyman file.

Compile "IPAUni10.kmn" by kmflcomp.
Kmflcomp is a compiler for source Keyman files.
It is a free software (GPL) running on Linux.

$ kmflcomp IPAUni10.kmn
It will generate "IPAUni10.kmfl".

SCIM supports libkmfl. Install scim-kmfl-imengine then
run scim-setup. Click "KMFL" and install "IPAUni10.kmfl".

Restart SCIM and choose "Other" -> "IPA Unicode 1.0.5" on
scim-toolbar.


%package -n	%{libname}
Summary:	KMFL library
Group:		System/Internationalization
Provides:		%{name} = %{version}-%{release}

%description -n %{libname}
KMFL library.

%package -n	%{libname}-devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:		%{libname} = %{version}
Provides:		%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers of %{name} for development.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./autoge.sh
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
%doc COPYING
%{_libdir}/libkmfl.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING 
%{_includedir}/kmfl/libkmfl.h
%{_libdir}/libkmfl.la
%{_libdir}/libkmfl.a
%{_libdir}/libkmfl.so


