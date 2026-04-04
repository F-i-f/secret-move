%global _pypi_project_name     secret-move
%global _pypi_project_name_esc secret_move
%global _description %{expand:
Tool to list, copy and move libsecret secrets between keyrings.}

Name:		python-%{_pypi_project_name}
Version:	0.5
Release:	1%{?dist}
Summary:	List, copy and move libsecret secrets between keyrings

License:	GPLv3
URL:		https://github.com/F-i-f/%_pypi_project_name
Source0:	%{pypi_source %_pypi_project_name_esc}

BuildArch:	noarch

%description %_description

%package -n python3-%_pypi_project_name
Summary:	%{summary}

%description -n python3-%_pypi_project_name %_description

%prep
%autosetup -n %_pypi_project_name_esc-%version

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %_pypi_project_name_esc

%files -n python3-%_pypi_project_name -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/secret-move

%changelog
* Fri Apr 03 2026 Philippe Troin <phil@fifi.org>
- Created.
