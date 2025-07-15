Summary:	ROTE Our Own Terminal Emulation Library
Summary(pl.UTF-8):	Biblioteka emulacji powtórzeń terminali
Name:		rote
Version:	0.2.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/rote/%{name}-%{version}.tar.gz
# Source0-md5:	9e5901267d9ed239343f55a54d76e48e
Patch0:		%{name}-ncurses.patch
URL:		http://rote.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROTE is a simple C library for VT102 terminal emulation. It allows the
programmer to set up virtual 'screens' and send them data. They will
emulate the behavior of a VT102 terminal, interpreting escape
sequences, control characters and such.

%description -l pl.UTF-8
ROTE jest prostą biblioteką C do emulacji terminala VT102. Pozwala
programiście na ustawienie wirtualnych ekranów i wysyłanie do nich
danych. Może emulować zachowanie terminala VT102, interpretować kody
esc, kontrolować znaki itepe.

%package devel
Summary:	Header files for ROTE library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ROTE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel

%description devel
Header files for ROTE library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ROTE.

%package static
Summary:	Static ROTE library
Summary(pl.UTF-8):	Statyczna biblioteka ROTE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ROTE library.

%description static -l pl.UTF-8
Statyczna biblioteka ROTE.

%prep
%setup -q
%patch -P0 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
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
%attr(755,root,root) %{_libdir}/librote.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librote.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/librote.so
%{_includedir}/%{name}
