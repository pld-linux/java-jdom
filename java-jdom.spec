#
# Conditional build:
%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif
#
%define		srcname	jdom
#
%include	/usr/lib/rpm/macros.java

Summary:	A Java representation of an XML document
Name:		java-%{srcname}
Version:	1.1
Release:	0.1
License:	BSD-Like
Group:		Libraries/Java
Source0:	http://www.jdom.org/dist/binary/%{srcname}-%{version}.tar.gz
# Source0-md5:	22745cbaaddb12884ed8ee09083d8fe2
URL:		http://www.jdom.org/
BuildRequires:	ant
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JDOM is, quite simply, a Java representation of an XML document. JDOM
provides a way to represent that document for easy and efficient
reading, manipulation, and writing. It has a straightforward API, is a
lightweight and fast, and is optimized for the Java programmer. It's
an alternative to DOM and SAX, although it integrates well with both
DOM and SAX.

%description -l pl.UTF-8
JDOM jest biblioteką napisaną w Javie służącą do obróbki dokumentów
XML. JDOM jest reprezentacją danych pozwalającą w łatwy i efektywny
sposób odczytywać, przekształcać i zapisywać dokumenty XML. JDOM
posiada przejrzyste, lekkie i szyckie API, jest zoptymalizowane z
myślą o programiście Javy. Biblioteka JDOM jest alternatywą dla DOM i
SAX, jednak może być łatwo zintegrowana zarówno z DOM jak i SAX.

%package demo
Summary:	Demo for %{srcname}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{srcname}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

%build
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sax
cp -a samples/sax/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sax
cp -a samples/*.* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt COMMITTERS.txt LICENSE.txt README.txt TODO.txt
%{_javadir}/*.jar

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
