#
%define		srcname	jdom
#
%include	/usr/lib/rpm/macros.java

Summary:	A Java representation of an XML document
Name:		java-%{srcname}
Version:	1.1
Release:	2
License:	BSD-Like
Group:		Libraries/Java
Source0:	http://www.jdom.org/dist/binary/%{srcname}-%{version}.tar.gz
# Source0-md5:	22745cbaaddb12884ed8ee09083d8fe2
URL:		http://www.jdom.org/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre
Provides:	jdom
Obsoletes:	jdom
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
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{srcname}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	jdom-demo

%description demo
Demonstrations and samples for %{srcname}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%package javadoc
Summary:	%{srcname} documentation
Summary(pl.UTF-8):	Dokumentacja do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
%{srcname} documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

find -name '*.jar' | xargs rm
find -name '*.class' | xargs rm

%build
%ant package %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -R build/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc CHANGES.txt COMMITTERS.txt LICENSE.txt README.txt TODO.txt
%{_javadir}/*.jar

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
