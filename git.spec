Summary:	A set of GNU Interactive Tools
Summary(de.UTF-8):	GIT - GNU Interactive Tools
Summary(fr.UTF-8):	GIT - Outils interactifs de GNU
Summary(pl.UTF-8):	GIT - interaktywne narzędzia GNU
Summary(tr.UTF-8):	GNU görsel kabuğu
Name:		git
Version:	4.3.20
Release:	10
License:	GPL v2+
Group:		Applications/File
Source0:	http://ftp.gnu.org/gnu/git/%{name}-%{version}.tar.gz
# Source0-md5:	72b01d5f9905951137ac1bb87d7e431c
Patch0:		%{name}-info.pach
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-ac.patch
URL:		http://www.gnu.org/software/git/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIT (GNU Interactive Tools) provides an extensible file system
browser, an ASCII/hexadecimal file viewer, a process viewer/killer and
other related utilities and shell scripts. GIT can be used to increase
the speed and efficiency of copying and moving files and directories,
invoking editors, compressing and uncompressing files, creating and
expanding archives, compiling programs, sending mail and more. GIT
uses standard ANSI color sequences, if they are available.

%description -l de.UTF-8
GIT ist ein Dateisystem-Browser für UNIX-Systeme. Ein interaktiver
Prozeß-Viewer/Killer, ein Hex/ASCII-Datei-Viewer, ein
Auto-Mount-Shell-Skript und ein dateiformatbezogenes Aktions-Skript
sind ebenfalls erhältlich.

%description -l fr.UTF-8
GIT est un navigateur de systèmes de fichiers pour les systèmes UNIX.
Un visualisateur/destructeur interactif de processus, un visualisateur
de fichiers en hexa/ascii, un script shell d'automontage et un script
d'actions par type de fichier sont aussi disponibles.

Les séquences standard ANSI pour les couleurs sont utilisées
lorsqu'elles sont disponibles. Les pages du manuel et la doc info sont
aussi fournies.

%description -l pl.UTF-8
GIT (GNU Interactive Tools, interaktywne narzędzia GNU) to elastyczna
przeglądarka plików, narzędzie do przeglądania zawartości plików w
formacie ASCII i szesnanstkowym, przeglądarka i eliminator procesów
oraz inne, pokrewne narzędzia i skrypty powłoki. Dzięki interaktywnym
narzędziom GNU można zwiększyć szybkość i efektywność takich czynności
jak kopiowanie i przenoszenie plików i katalogów, wywoływania
edytorów, pakowanie i rozpakowywanie plików, tworzenie i ekstrakcja
archiwów, kompilacja programów, wysyłanie poczty itd. GIT używa
standardowych sekwencji koloryzujących ANSI, jeśli system je
obsługuje.

%description -l tr.UTF-8
GIT, UNIX sistemler için bir dosya sistemi arayüzüdür. Etkileşimli bir
süreç görüntüleyici/sonlandırıcı, bir hex/ascii dosya görüntüleyici,
bir otomatik bağlayıcı (auto-mount) kabuk betiği ve dosya tipine göre
betik çalıştırma yetenekleri vardır.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

touch doc/git.html

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-terminfo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# rename the binary to avoid collision with git-core 
# OTOH, Debian renamed git-core. 
mv -f $RPM_BUILD_ROOT%{_bindir}/git{,.gnu}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog LSM NEWS PLATFORMS PROBLEMS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_bindir}/.gitaction
%{_mandir}/man1/*
%{_infodir}/git.info*
%dir %{_datadir}/git
%{_datadir}/git/.gitrc*
