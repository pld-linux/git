Summary: A set of GNU Interactive Tools.
Name: git
Version: 4.3.17
Release: 5
Copyright: GNU
Group: Applications/File
Source: ftp://prep.ai.mit.edu:/pub/gnu/git-4.3.17.tar.gz
Patch0: git-4.3.17-path.patch
Buildroot: /var/tmp/git-root
Prereq: /sbin/install-info

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

%setup
%patch0 -p1 -b .path

%build
CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS" LDFLAGS='-s' ./configure --prefix=/usr \
	--with-terminfo
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/ install-strip
gzip -9nf $RPM_BUILD_ROOT/usr/info/git.info*

%files
%doc COPYING ChangeLog LSM NEWS PLATFORMS PROBLEMS README INSTALL
/usr/bin/*
/usr/bin/.gitaction
/usr/man/man1/*
/usr/info/*
/usr/lib/git/.gitrc*
%docdir /usr/lib/git/html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/git.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/git.info.gz /usr/info/dir
fi
