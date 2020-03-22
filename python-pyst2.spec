# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	asterisk
%define         egg_name        pyst2
Summary:	A Python Interface to Asterisk
Name:		python-pyst2
Version:	0.5.0
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	https://github.com/rdegges/pyst2/archive/%{version}.tar.gz
# Source0-md5:	c1e882331d2d3f7fe8da85b3a1e11b10
URL:		https://pypi.python.org/pypi/pyst2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyst2 consists of a set of interfaces and libraries to allow
programming of Asterisk from python. The library currently supports
AGI, AMI, and the parsing of Asterisk configuration files. The library
also includes debugging facilities for AGI.

%package -n python3-%{egg_name}
Summary:	A Python Interface to Asterisk
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{egg_name}
pyst2 consists of a set of interfaces and libraries to allow
programming of Asterisk from python. The library currently supports
AGI, AMI, and the parsing of Asterisk configuration files. The library
also includes debugging facilities for AGI.

%prep
%setup -q -n pyst2-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{egg_name}
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
