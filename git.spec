Summary:	A set of GNU Interactive Tools.
Name:		git
Version:	4.3.17
Release:	6
Copyright:	GNU
Group:		Applications/File
Source:		ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		git-4.3.17-path.patch
Patch1:		git-FHS.patch
Buildroot:	/tmp/%{name}-%{version}-root
Prereq:		/sbin/install-info

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
/sbin/install-info /usr/info/git.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/git.info.gz /usr/info/dir
fi

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
