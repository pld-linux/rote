Summary:	ROTE Our Own Terminal Emulation Library
Summary(pl):	Biblioteka emulacji powtórzeñ terminali
Name:		rote
Version:	0.2.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/rote/%{name}-%{version}.tar.gz
# Source0-md5:	a80074dc2fbabd6e204bc07a61e57120
# Source0-size:	61440
Patch0:		%{name}-DESTDIR.patch
URL:		http://rote.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROTE is a simple C library for VT102 terminal emulation. It allows the
programmer to set up virtual 'screens' and send them data. They will
emulate the behavior of a VT102 terminal, interpreting escape
sequences, control characters and such.

%description -l pl
ROTE jest prost± bibliotek± C do emulacji terminala VT102. Pozwala
programi¶cie na ustawienie wirtualnych ekranów i wysy³anie do nich
danych. Mo¿e emulowaæ zachowanie terminala VT102, interpretowaæ kody
esc, kontrolowaæ znaki itepe.

%package devel
Summary:	Header files for ROTE library
Summary(pl):	Pliki nag³ówkowe biblioteki ROTE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel

%description devel
Header files for ROTE library.

%description devel -l pl
Pliki nag³ówkowe biblioteki ROTE.

%package static
Summary:	Static ROTE library
Summary(pl):	Statyczna biblioteka ROTE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ROTE library.

%description static -l pl
Statyczna biblioteka ROTE.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
