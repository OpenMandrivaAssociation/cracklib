%define sname crack
%define major 2
%define libname %mklibname %{sname} %{major}
%define devname %mklibname %{sname} -d

%bcond_without python

%if %{with python}
# For the python module
%define _disable_ld_no_undefined 1
%endif

Summary:	A password-checking library
Name:		cracklib
Version:	2.9.11
Release:	1
Group:		System/Libraries
License:	LGPLv2
Url:		https://github.com/cracklib/cracklib
Source0:	https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-%{version}.tar.xz
Source1:	https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-words-%{version}.xz
Source10:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Domains.gz
Source11:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Dosref.gz
Source12:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Ftpsites.gz
Source13:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/Jargon.gz
Source14:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/common-passwords.txt.gz
Source15:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/computer/etc-hosts.gz
Source16:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Movies.gz
Source17:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Python.gz
Source18:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/movieTV/Trek.gz
Source19:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/LCarrol.gz
Source20:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/Paradise.Lost.gz
Source21:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/cartoon.gz
Source22:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/myths-legends.gz
Source23:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/sf.gz
Source24:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/literature/shakespeare.gz
Source25:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/ASSurnames.gz
Source26:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Congress.gz
Source27:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Family-Names.gz
Source28:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/Given-Names.gz
Source29:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/famous.gz
Source30:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/fast-names.gz
Source31:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/female-names.gz
Source32:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/male-names.gz
Source33:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/names.french.gz
Source34:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/names.hp.gz
Source35:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/other-names.gz
Source36:	http://ftp.cerias.purdue.edu/pub/dict/wordlists/names/surnames.finnish.gz
Source37:	http://downloads.skullsecurity.org/passwords/john.txt.bz2
Source38:	http://downloads.skullsecurity.org/passwords/cain.txt.bz2
Source39:	http://downloads.skullsecurity.org/passwords/twitter-banned.txt.bz2
Source40:	http://downloads.skullsecurity.org/passwords/500-worst-passwords.txt.bz2
BuildRequires:	gettext-devel
BuildRequires:	slibtool
Suggests:	%{name}-dicts = %{version}-%{release}

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

%package -n %{libname}
Summary:	A password-checking library
Group:		System/Libraries
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics.

%package -n %{devname}
Summary:	Cracklib link library & header file
Group:		Development/C
Provides:	lib%{sname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{devname}
The cracklib devel package include the needed library link and
header files for development.

%package dicts
Summary:	The standard CrackLib dictionaries
Group:		System/Libraries
Requires(meta):	cracklib >= %{EVRD}

%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words.  Cracklib-dicts also contains
the utilities necessary for the creation of new dictionaries.

If you are installing CrackLib, you should also install cracklib-dicts.

%if %{with python}
%package -n python-%{name}
Summary:	A password-checking library
Group:		System/Libraries
%rename		%{_lib}crack2-python
BuildRequires:	pkgconfig(python)

%description -n python-%{name}
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics.
%endif

%prep
%autosetup -p1

cp -p lib/packer.h lib/packer.h.in
AUTOPOINT=true autoreconf -fi

for dict in %{SOURCE1} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} \
	%{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} \
	%{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} \
	%{SOURCE29} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} \
	%{SOURCE36} %{SOURCE37} %{SOURCE38} %{SOURCE39} %{SOURCE40}; do
	cp ${dict} dicts/
done
gzip -d dicts/*.gz
bzip2 -d dicts/*.bz2
unxz dicts/*.xz
mv dicts/cracklib-words-%{version} dicts/cracklib-words

export CONFIGURE_TOP=$(pwd)
mkdir build
cd build
%configure \
%if %{without python}
	--without-python --disable-python \
%endif
	--enable-static
cd ..
%if %{cross_compiling}
mkdir build-native
cd build-native
unset CC || :
unset LDFLAGS || :
CFLAGS="-O2" ../configure --enable-static --disable-shared
%endif

%build
%make_build -C build LIBTOOL=slibtool

%if %{cross_compiling}
%make_build -C build-native LIBTOOL=slibtool
%endif

%install
%make_install -C build LIBTOOL=slibtool

# MD remove static python lib
rm -f %{buildroot}%{py_platsitedir}/_cracklib.a

%if %{cross_compiling}
B=build-native
%else
B=build
%endif

chmod 0755 ./util/cracklib-format ./$B/util/cracklib-packer
./util/cracklib-format dicts/* | ./$B/util/cracklib-packer %{buildroot}%{_datadir}/cracklib/pw_dict

ln -s cracklib-format %{buildroot}%{_sbindir}/mkdict
ln -s cracklib-packer %{buildroot}%{_sbindir}/packer

mkdir -p %{buildroot}%{_libdir}
ln -s %{_datadir}/cracklib/pw_dict.hwm %{buildroot}%{_libdir}/cracklib_dict.hwm
ln -s %{_datadir}/cracklib/pw_dict.pwd %{buildroot}%{_libdir}/cracklib_dict.pwd
ln -s %{_datadir}/cracklib/pw_dict.pwi %{buildroot}%{_libdir}/cracklib_dict.pwi

install -m644 lib/packer.h %{buildroot}%{_includedir}/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README*
%{_sbindir}/*
%doc %{_mandir}/man3/*.3*
%doc %{_mandir}/man8/cracklib*.8*

%files -n %{libname}
%{_libdir}/libcrack.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.*a

%files dicts
%{_datadir}/%{name}
%{_libdir}/cracklib_dict.*

%if %{with python}
%files -n python-%{name}
%{python_sitearch}/*.so
%{python_sitelib}/*cracklib*
%{python_sitelib}/__pycache__/*
%endif
