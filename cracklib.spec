%define sname crack
%define major 2
%define libname %mklibname %{sname} %{major}
%define devname %mklibname %{sname} -d

Summary:	A password-checking library
Name:		cracklib
Version:	2.9.7
Release:	1
Group:		System/Libraries
License:	LGPLv2
Url:		https://github.com/cracklib/cracklib
Source0:	http://prdownloads.sourceforge.net/cracklib/%{version}/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/cracklib/%{version}/cracklib-words-%{version}.bz2
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
Patch0:		cracklib-2.8.15-fix-python-path.patch
Patch1:		cracklib-2.9.1-inttypes.patch
Patch5:		cracklib-2.9.6-coverity.patch
Patch6:		cracklib-2.9.6-lookup.patch
BuildRequires:	gettext-devel
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

%description -n	%{devname}
The cracklib devel package include the needed library link and
header files for development.

%package dicts
Summary:	The standard CrackLib dictionaries
Group:		System/Libraries

%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words.  Cracklib-dicts also contains
the utilities necessary for the creation of new dictionaries.

If you are installing CrackLib, you should also install cracklib-dicts.

%package -n python2-%{name}
Summary:	A password-checking library
Group:		System/Libraries
%rename		%{_lib}crack2-python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2

%description -n python2-%{name}
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics.

%prep
%autosetup -p1
cp -p lib/packer.h lib/packer.h.in
autoreconf -fi

for dict in %{SOURCE1} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} \
	%{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} \
	%{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} %{SOURCE28} \
	%{SOURCE29} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} \
	%{SOURCE36} %{SOURCE1}; do
	cp ${dict} dicts/
done
gunzip dicts/*.gz
bunzip2 dicts/*.bz2
mv dicts/cracklib-words-%{version} dicts/cracklib-words

%build
export PYTHON=%{__python2}
%configure --libdir=/%{_lib} --enable-static
%make_build

%install
%make_install

# MD remove static python lib
rm -f %{buildroot}%{py2_platsitedir}/_cracklib.a

chmod 0755 ./util/cracklib-format ./util/cracklib-packer
./util/cracklib-format dicts/* | ./util/cracklib-packer %{buildroot}%{_datadir}/cracklib/pw_dict

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

%files -n %{libname}
/%{_lib}/libcrack.so.%{major}*

%files -n %{devname}
%{_includedir}/*
/%{_lib}/*.so
/%{_lib}/*.*a

%files dicts
%{_sbindir}/*
%{_datadir}/%{name}
%{_libdir}/cracklib_dict.*

%files -n python2-%{name}
%{py2_platsitedir}/cracklib*
%{py2_platsitedir}/_cracklib.so
