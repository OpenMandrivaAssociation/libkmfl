%define major 0
%define libname %mklibname kmfl %{major}
%define develname %mklibname kmfl -d

Name:		libkmfl
Summary:	Keystroke interpreter for Tavultesoft Keyman files
Version:	0.9.9
Release:	1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
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
%makeinstall_std

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libkmfl.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_includedir}/kmfl/libkmfl.h
%{_libdir}/libkmfl.a
%{_libdir}/libkmfl.so


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-3mdv2011.0
+ Revision: 661479
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-2mdv2011.0
+ Revision: 602565
- rebuild

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 0.9.8-1mdv2010.1
+ Revision: 466216
- New version 0.9.8

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.7-2mdv2010.0
+ Revision: 425586
- rebuild

* Wed Dec 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 315037
- protect major in file list
- new release 0.9.7

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-6mdv2009.1
+ Revision: 301524
- rebuilt against new libxcb

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-5mdv2009.0
+ Revision: 232146
- use _disable_ld_no_undefined to make it build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-3mdv2008.1
+ Revision: 178961
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.6-1mdv2008.0
+ Revision: 80751
- correct license to GPLv2+
- new release 0.9.6

* Fri Aug 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.5-1mdv2008.0
+ Revision: 58436
- rebuild for 2008
- package correct doc files
- remove unneeded complexity in build
- clean buildrequires
- improve description
- use Fedora licensing policy
- new devel policy
- clean spec
- new release 0.9.5


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.8-3mdk
- Rebuild

* Wed Aug 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8-2mdk
- fix BuildRequires

* Mon Aug 08 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.8-1mdk
- new release

* Wed May 11 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.5-1mdk
- first spec for Mandriva Linux

