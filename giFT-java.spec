Summary:	The generic interface to FastTrack
Name:		giFT-java
Version:	0.1.1
Release:	1
License:	GPL
Group:		Applications/Java
Group(de):	Applikationen/Java
Group(pl):	Aplikacje/Java
Source0:	%{name}.%{version}.tar.gz
URL:		http://giFT.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
The generic interface to FastTrack

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp *.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf README LICENSE *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar
