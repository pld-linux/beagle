#
# Conditional build:
%bcond_with	epiphany	# build epiphany extension (it requires
				# epiphany-1.2.x)
#%define	snap 20041214
#Release:	0.%{snap}.1

Summary:	Beagle - An indexing subsystem
Summary(pl):	Beagle - podsystem indeksuj±cy
Name:		beagle
Version:	0.0.4
Release:	0.2
License:	Various
Group:		Libraries
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	db81d4d1bd0f841f0ae77829623d2a59
Patch0:		%{name}-Filters-dir.patch
Patch1:		%{name}-pc.patch
Patch2:		%{name}-bash.patch
URL:		http://www.gnome.com
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dotnet-evolution-sharp-devel >= 0.3
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	dotnet-dbus-sharp-devel >= 0.23
BuildRequires:	dotnet-gmime-sharp-devel
BuildRequires:	dotnet-gecko-sharp-devel
BuildRequires:	dotnet-gsf-sharp-devel
%if %{with epiphany}
BuildRequires:	epiphany-devel >= 1.2.1
BuildRequires:	epiphany-devel < 1.3.0
%endif
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	mono-csharp
BuildRequires:	wv-devel
BuildRequires:	pkgconfig
Requires:	dotnet-evolution-sharp >= 0.3
Requires:	dotnet-gtk-sharp
Requires:	dotnet-dbus-sharp >= 0.23
Requires:	dotnet-gsf-sharp
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beagle is an indexing sub-system and search aggregator built on top of
Lucene.Net.

%description -l pl
Beagle jest podsystemem indeksuj±cym i wyszukuj±cym zbudowanym na
bazie Lucene.Net.

%package devel
Summary:	Beagle development files
Summary(pl):	Pliki programistyczne Beagle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Beagle development files.

%description devel -l pl
Pliki programistyczne Beagle.

%package -n epiphany-extension-beagle
Summary:	Epiphany extension - beagle
Summary(pl):	Rozszerzenie dla Epiphany - beagle
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany >= 1.2.1
Requires:	epiphany < 1.3.0

%description -n epiphany-extension-beagle
Epiphany extension that allows Beagle to index every page the user
views.

%description -n epiphany-extension-beagle -l pl
Rozszerzenie dla Epiphany sprawiaj±ce, ¿e Beagle indeksuje ka¿d±
odwiedzan± stronê.

%prep
%setup -q
#%patch0 -p0
#%patch1 -p0
%patch2 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if %{with epiphany}
	--enable-epiphany-extension
%else
	--disable-epiphany-extension
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Kill useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/extensions/*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/filesystems/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root)%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/gtk-2.0/2.4.0/filesystems/libbeaglechooserhack.so*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*

%if %{with epiphany}
%files -n epiphany-extension-beagle
%defattr(644,root,root,755)
%doc epiphany-extension/README
%attr(755,root,root) %{_libdir}/epiphany/extensions/libbeagleextension.so*
%endif
