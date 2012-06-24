Summary:	A set of GNU Interactive Tools
Summary(de):	GIT - GNU Interactive Tools
Summary(fr):	GIT - Outils interactifs de GNU
Summary(pl):	GIT - interaktywne narz�dzia GNU
Summary(tr):	GNU g�rsel kabu�u
Name:		git
Version:	4.3.20
Release:	7
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnu.org/pub/gnu/git/%{name}-%{version}.tar.gz
# Source0-md5:	72b01d5f9905951137ac1bb87d7e431c
Patch0:		%{name}-info.pach
Patch1:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIT (GNU Interactive Tools) provides an extensible file system
browser, an ASCII/hexadecimal file viewer, a process viewer/killer and
other related utilities and shell scripts. GIT can be used to increase
the speed and efficiency of copying and moving files and directories,
invoking editors, compressing and uncompressing files, creating and
expanding archives, compiling programs, sending mail and more. GIT
uses standard ANSI color sequences, if they are available.

%description -l de
GIT ist ein Dateisystem-Browser f�r UNIX-Systeme. Ein interaktiver
Proze�-Viewer/Killer, ein Hex/ASCII-Datei-Viewer, ein
Auto-Mount-Shell-Skript und ein dateiformatbezogenes Aktions-Skript
sind ebenfalls erh�ltlich.

%description -l fr
GIT est un navigateur de syst�mes de fichiers pour les syst�mes UNIX.
Un visualisateur/destructeur interactif de processus, un visualisateur
de fichiers en hexa/ascii, un script shell d'automontage et un script
d'actions par type de fichier sont aussi disponibles.

Les s�quences standard ANSI pour les couleurs sont utilis�es
lorsqu'elles sont disponibles. Les pages du manuel et la doc info sont
aussi fournies.

%description -l pl
GIT (GNU Interactive Tools, interaktywne narz�dzia GNU) to elastyczna
przgl�darka plik�w, narz�dzie do przegl�dania zawarto�ci plik�w w
formacie ASCII i szesnanstkowym, przegladarka i eliminator proces�w
oraz inne, pokrewne narz�dzia i skrypty pow�oki. Dzi�ki interaktywnym
narz�dziom GNU mo�na zwi�kszy� szybko�� i efektywno�� takich czynnosci
jak kopiowanie i przenoszenie plik�w i katalog�w, wywo�ywania
edytor�w, pakowanie i rozpakowywanie plik�w, tworzenie i ekstrakcja
archiw�w, kompilacja program�w, wysy�anie poczty itd. GIT uzywa
standardowych sekwencji koloryzuj�cych ANSI, je�li system je
obs�uguje.

%description -l tr
GIT, UNIX sistemler i�in bir dosya sistemi aray�z�d�r. Etkile�imli bir
s�re� g�r�nt�leyici/sonland�r�c�, bir hex/ascii dosya g�r�nt�leyici,
bir otomatik ba�lay�c� (auto-mount) kabuk beti�i ve dosya tipine g�re
betik �al��t�rma yetenekleri vard�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-terminfo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog LSM NEWS PLATFORMS PROBLEMS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_bindir}/.gitaction
%{_mandir}/man1/*
%{_infodir}/git.info*
%dir %{_datadir}/git
%{_datadir}/git/.gitrc*
