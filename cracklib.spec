%define root	crack

%define _enable_libtoolize 1

%define major		2
%define libname		%mklibname %root %major
%define develname	%mklibname %root -d

Summary:	A password-checking library
Name:		cracklib
Version:	2.8.18
Release:	%mkrel 2
Group:		System/Libraries
License:	LGPLv2
URL:		http://sourceforge.net/projects/cracklib/
Source0:	http://prdownloads.sourceforge.net/cracklib/cracklib-%{version}.tar.gz
Source1:        http://prdownloads.sourceforge.net/cracklib/cracklib-words.bz2
Source10:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Domains.bz2
Source11:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Dosref.bz2
Source12:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Ftpsites.bz2
Source13:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Jargon.bz2
Source14:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/common-passwords.txt.bz2
Source15:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/etc-hosts.bz2
Source16:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Movies.bz2
Source17:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Python.bz2
Source18:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Trek.bz2
Source19:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/LCarrol.bz2
Source20:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/Paradise.Lost.bz2
Source21:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/cartoon.bz2
Source22:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/myths-legends.bz2
Source23:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/sf.bz2
Source24:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/shakespeare.bz2
Source25:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/ASSurnames.bz2
Source26:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Congress.bz2
Source27:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Family-Names.bz2
Source28:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Given-Names.bz2
Source29:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/famous.bz2
Source30:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/fast-names.bz2
Source31:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/female-names.bz2
Source32:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/male-names.bz2
Source33:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/names.french.bz2
Source34:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/names.hp.bz2
Source35:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/other-names.bz2
Source36:	ftp://ftp.cerias.purdue.edu/pub/dict/wordlists/names/surnames.finnish.bz2
Patch0:		cracklib-2.8.15-fix-python-path.patch
Patch1:		cracklib-2.8.15-inttypes.patch
Patch2:		cracklib-2.8.12-gettext.patch
Conflicts:	libcrack2 < 2.8.15
Conflicts:	lib64crack2 < 2.8.15
BuildRequires:	gettext-devel
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop
users from choosing passwords which would be easy to guess. CrackLib
performs certain tests: 

* It tries to generate words from a username and gecos entry and 
  checks those words against the password;
* It checks for simplistic patterns in passwords;
* It checks for the password in a dictionary.

CrackLib is actually a library containing a particular
C function which is used to check the password, as well as
other C functions. CrackLib is not a replacement for a passwd
program; it must be used in conjunction with an existing passwd
program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you
install CrackLib, you'll also want to install the cracklib-dicts
package.

%package -n	%{libname}
Summary:	A password-checking library
Group:		System/Libraries
Obsoletes:	cracklib < %{version}-%{release}

%description -n %{libname}
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics.

%package -n	%{libname}-python
Summary:	A password-checking library
Group:		System/Libraries
Obsoletes:	cracklib-python < %{version}-%{release}
%py_requires -d

%description -n %{libname}-python
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics.

%package	dicts
Summary:	The standard CrackLib dictionaries
Group:		System/Libraries

%description	dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words.  Cracklib-dicts also contains
the utilities necessary for the creation of new dictionaries.

If you are installing CrackLib, you should also install cracklib-dicts.

%package -n	%{develname}
Summary:	Cracklib link library & header file
Group:		Development/C
Provides:	lib%{root}-devel = %{version}-%{release}
Provides:	%{root}lib-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	cracklib-devel < %{version}-%{release}
Obsoletes:	%{mklibname crack 2 -d} < %{version}-%{release}

%description -n	%{develname}
The cracklib devel package include the needed library link and
header files for development.

%prep
%setup -q
%patch0 -p0
cp -p lib/packer.h lib/packer.h.in
%patch1 -p1 -b .inttypes
%patch2 -p1 -b .gettext

autoreconf -fi

for dict in %{SOURCE1} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} \
    %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} \
    %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} \
    %{SOURCE29} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} \
    %{SOURCE36} %{SOURCE1}; do
    cp ${dict} dicts/
done
bunzip2 dicts/*.bz2

%build
%configure2_5x --libdir=/%{_lib}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

chmod 0755 ./util/cracklib-format ./util/cracklib-packer
./util/cracklib-format dicts/* | ./util/cracklib-packer %{buildroot}%{_datadir}/cracklib/pw_dict

ln -s cracklib-format %{buildroot}%{_sbindir}/mkdict
ln -s cracklib-packer %{buildroot}%{_sbindir}/packer

ln -s %{_datadir}/cracklib/pw_dict.hwm %{buildroot}%{_libdir}/cracklib_dict.hwm
ln -s %{_datadir}/cracklib/pw_dict.pwd %{buildroot}%{_libdir}/cracklib_dict.pwd
ln -s %{_datadir}/cracklib/pw_dict.pwi %{buildroot}%{_libdir}/cracklib_dict.pwi

install -m644 lib/packer.h %{buildroot}%{_includedir}/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
/%{_lib}/*.so.%{major}*

%files -n %{libname}-python
%defattr(-,root,root)
%{py_platsitedir}/cracklib*
%{py_platsitedir}/_cracklib*

%files -f %{name}.lang
%doc AUTHORS NEWS README*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
/%{_lib}/*.so
/%{_lib}/*.*a

%files dicts
%defattr(-,root,root)
%{_sbindir}/*
%{_datadir}/%{name}
%{_libdir}/cracklib_dict.*


%changelog
* Wed Feb 22 2012 abf
- The release updated by ABF

* Tue May 03 2011 Funda Wang <fwang@mandriva.org> 2.8.18-1mdv2011.0
+ Revision: 663999
- br gettext-devel

  + Oden Eriksson <oeriksson@mandriva.com>
    - 2.8.18
    - rediffed P0
    - added fixes from fedora (P1+P2)
    - mass rebuild

* Sat Oct 30 2010 Shlomi Fish <shlomif@mandriva.org> 2.8.16-2mdv2011.0
+ Revision: 590592
- Bump to new release for python-2.7

* Wed Mar 03 2010 Frederik Himpe <fhimpe@mandriva.org> 2.8.16-1mdv2010.1
+ Revision: 514005
- update to new version 2.8.16

* Fri Nov 20 2009 Frederik Himpe <fhimpe@mandriva.org> 2.8.15-1mdv2010.1
+ Revision: 467688
- Update to new version 2.8.15
- Rediff Python path patch
- Fix libification by moving docs out of library package

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.8.13-4mdv2010.0
+ Revision: 413276
- rebuild

  + Arnaud Patard <apatard@mandriva.com>
    - Fix ftbfs with newer libtool by defining _enable_libtoolize

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 2.8.13-3mdv2009.1
+ Revision: 319812
- rebuild for new python

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.8.13-2mdv2009.1
+ Revision: 316518
- rebuild

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.13-1mdv2009.1
+ Revision: 297783
- patch: fix python modules installation path
- new version

* Thu Jun 19 2008 Adam Williamson <awilliamson@mandriva.org> 2.8.12-1mdv2009.0
+ Revision: 226736
- docs/LICENCE doesn't exist any more..
- new release 2.8.12
- move shared library to /lib (fix #40626, impossible to login without /usr)
- clean file lists
- drop bogus and/or useless devel provides in lib and python packages
- fix python package description
- version obsoletes
- new devel policy
- simplify and clean spec

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.8.10-6mdv2009.0
+ Revision: 220517
- rebuild
- fix spacing at top of description

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - fix library description (broken for 5 years)

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 2.8.10-5mdv2008.1
+ Revision: 149140
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild for optflags
    - make format and packer executable prior to running them in %%install (#31210)

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

* Sat Jun 02 2007 Adam Williamson <awilliamson@mandriva.org> 2.8.10-1mdv2008.0
+ Revision: 34743
- new release 2.8.10, remove pre-2007 workaround


* Thu Dec 14 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.8.9-2mdv2007.0
+ Revision: 96899
- BuildRequires: python-devel
- BuildRequires: python
- fix build
- Import cracklib

* Sat Jun 24 2006 Emmanuel Andry <eandry@mandriva.org> 2.8.9-1mdv2007.0
- 2.8.9
- %%mkrel
- add cracklib-python package

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 2.8.3-3mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.8.3-2mdk
- Rebuild

* Wed Apr 27 2005 Oden Eriksson <oeriksson@mandriva.com> 2.8.3-1mdk
- 2.8.3, new url, drop upstream implemented patches
- sync some with fedora
- fix summary-ended-with-dot

* Thu May 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.7-18mdk
- add one missing header file
- misc spec file fixes

