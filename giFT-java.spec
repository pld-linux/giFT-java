Summary:	The generic interface to FastTrack
Summary(pl):	Zwyk�y interfejs do FastTracka
Name:		giFT-java
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gift/%{name}.%{version}.tar.gz
URL:		http://giFT.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
The generic interface to FastTrack.

%description -l pl
Zwyk�y interfejs do FastTracka.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install *.jar $RPM_BUILD_ROOT%{_javalibdir}

gzip -9nf README LICENSE *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar