%define root	crack

%define _enable_libtoolize 1

%define major		2
%define libname		%mklibname %root %major
%define develname	%mklibname %root -d

Summary:	A password-checking library
Name:		cracklib
Version:	2.8.13
Release:	%mkrel 4
Group:		System/Libraries
License:	Artistic
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
Patch:      cracklib-2.8.13-fix-python-path.patch
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
%patch -p 1
autoreconf

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
%doc AUTHORS COPYING ChangeLog NEWS README*
/%{_lib}/*.so.%{major}*


%files -n %{libname}-python
%defattr(-,root,root)
%{py_platsitedir}/cracklib*
%{py_platsitedir}/_cracklib*

%files -f %{name}.lang
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
