%global pypi_name sphinx-removed-in

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        3%{?dist}
Summary:        versionremoved and removed-in directives for Sphinx
License:        BSD
URL:            https://github.com/MrSenko/sphinx-removed-in
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# https://github.com/MrSenko/sphinx-removed-in/pull/6
Patch1:         %{pypi_name}-sphinx2.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-testing

%description
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a Sphinx extension which recognizes the versionremoved and removed-in
directives.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinx_removed_in/
%{python3_sitelib}/sphinx_removed_in-%{version}-py%{python3_version}.egg-info/

%changelog
* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-1
- Initial package
