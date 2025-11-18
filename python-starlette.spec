%define module starlette

Name:		python-%{module}
Version:	0.50.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
Summary:	The little ASGI library that shines
URL:		https://pypi.org/project/starlette/
License:	BSD-3-Clause
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python-build
BuildRequires:	python-hatchling
Requires:	python-anyio >= 3.6.0
Requires:	python-typing-extensions

%description
Starlette is a lightweight ASGI framework/toolkit, which is ideal for building
async web services in Python.

It is production-ready, and gives you the following:

  A lightweight, low-complexity HTTP web framework.
  WebSocket support.
  In-process background tasks.
  Startup and shutdown events.
  Test client built on httpx.
  CORS, GZip, Static Files, Streaming responses.
  Session and Cookie support.
  100%% test coverage.
  100%% type annotated codebase.
  Few hard dependencies.
  Compatible with asyncio and trio backends.
  Great overall performance against independent benchmarks.


%prep
%autosetup -p1 -n starlette-%{version}

%build
%py_build

%install
%py3_install

%files
%{python3_sitelib}/%{module}-%{version}.dist-info
%{python3_sitelib}/%{module}/*.py
%{python3_sitelib}/%{module}/*.typed
%{python3_sitelib}/%{module}/__pycache__/*.cpython-3*.pyc
%{python3_sitelib}/%{module}/middleware/*.py
%{python3_sitelib}/%{module}/middleware/__pycache__/*.cpython-3*.pyc
%doc README.md
%license LICENSE.md
