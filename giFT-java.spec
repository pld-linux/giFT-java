Summary:	The generic interface to FastTrack
Summary(pl.UTF-8):	Zwykły interfejs do FastTracka
Name:		giFT-java
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/gift/%{name}.%{version}.tar.gz
# Source0-md5:	839d53641dae29cdaeddb31a1a65e79c
URL:		http://giFT.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The generic interface to FastTrack.

%description -l pl.UTF-8
Zwykły interfejs do FastTracka.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install *.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.html
%{_javalibdir}/*.jar
