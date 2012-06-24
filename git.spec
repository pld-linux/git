Summary:	A set of GNU Interactive Tools.
Name:		git
Version:	4.3.17
Release:	7
Copyright:	GNU
Group:		Applications/File
Source:		ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		git-4.3.17-path.patch
Patch1:		git-FHS.patch
Buildroot:	/tmp/%{name}-%{version}-root
Prereq:		/usr/sbin/fix-info-dir

%description
GIT (GNU Interactive Tools) provides an extensible file system browser,
an ASCII/hexadecimal file viewer, a process viewer/killer and other
related utilities and shell scripts.  GIT can be used to increase the
speed and efficiency of copying and moving files and directories, invoking
editors, compressing and uncompressing files, creating and expanding
archives, compiling programs, sending mail and more.  GIT uses standard
ANSI color sequences, if they are available.  

You should install the git package if you are interested in using its file
management capabilities.

%description -l pl
GIT (GNU Interactive Tools, interaktywne narz�dzia GNU) to elastyczna
przgl�darka plik�w, narz�dzie do przegl�dania zawarto�ci plik�w w formacie
ASCII i szesnanstkowym, przegladarka i eliminator proces�w oraz inne, pokrewne
narz�dzia i skrypty pow�oki. Dzi�ki interaktywnym narz�dziom GNU mo�na 
zwi�kszy� szybko�� i efektywno�� takich czynnosci jak kopiowanie i przenoszenie
plik�w i katalog�w, wywo�ywania edytor�w, pakowanie i rozpakowywanie plik�w,
tworzenie i ekstrakcja archiw�w, kompilacja program�w, wysy�anie poczty itd.
GIT uzywa standardowych sekwencji koloryzuj�cych ANSI, je�li system je obs�uguje.

Nale�y zainstalowac pakiet git je�li che si� wykorzystac jego mo�liwo�ci
w zarz�dzaniu plikami.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --with-terminfo
make

%install
rm -rf $RPM_BUILD_ROOT
make install-strip prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/git.info* \
	ChangeLog LSM NEWS PLATFORMS PROBLEMS README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc {ChangeLog,LSM,NEWS,PLATFORMS,PROBLEMS,README}.gz
%doc %dir %{_datadir}/git/html
%doc %{_datadir}/git/html/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_bindir}/.gitaction
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/git/.gitrc*
