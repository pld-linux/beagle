# TODO:
#	Add proper BR's
#	separate epiphany plugin
#	maybe more :)

Summary:	Beagle - An indexing subsystem
Summary(pl):	Beagle - podsystem indeksuj±cy
Name:		beagle
Version:	0.0.1
Release:	0.2
License:	Various
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	9505a0d8aad8f0d80f9f18aab77dac08
URL:		http://www.gnome.com/
BuildRequires:	dotnet-evolution-sharp >= 0.3
BuildRequires:	epiphany-devel
BuildRequires:	mono
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
Gecko# development files.

%description devel -l pl
Pliki programistyczne Gecko#.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Kill useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/extensions/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root)%{_bindir}/*
%attr(755,root,root)%{_libdir}/epiphany/extensions/libbeagleextension.so*
%{_libdir}/%{name}


%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
