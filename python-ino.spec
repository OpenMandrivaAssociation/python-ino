%global module ino
%define mod %(m=%{module}; echo ${m:0:1})

Summary:	A command line toolkit for working with Arduino hardware
Name:		python-%{module}
Version:	0.3.6
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://inotool.org
Source0: 	https://files.pythonhosted.org/packages/source/%{mod}/ino/%{module}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Ino is a command line toolkit for working with Arduino hardware

It allows you to:

  *  Quickly create new projects
  *  Build a firmware from multiple source files and libraries
  *  Upload the firmware to a device
  *  Perform serial communication with a device (aka serial monitor)

Ino may replace Arduino IDE UI if you prefer to work with command line and
an editor of your choice or if you want to integrate Arduino build process
to 3-rd party IDE.

Ino is based on make to perform builds. However Makefiles are generated
automatically and you'll never see them if you don't want to.

%files
%license MIT-LICENSE.txt
%doc README.rst
%{_bindir}/%{module}
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

