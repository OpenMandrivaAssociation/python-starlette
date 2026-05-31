%define module starlette

Name:		python-starlette
Version:	1.2.1
Release:	1
Summary:	The little ASGI library that shines
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://starlette.dev/
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

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

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
