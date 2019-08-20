# Copyright 2019 Nokia

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Name:           hw-detector
Version:        %{_version}
Release:        2%{?dist}
Summary:        Hardware detector
Group:          Nokia
License:        %{_platform_licence}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Vendor:         %{_platform_vendor}

Requires: python 
BuildRequires: python
BuildRequires: python-setuptools

%description
Hardware detector for different hardware types

%prep
%autosetup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_python_site_packages_path}/hw_detector

cd src && python setup.py install --root %{buildroot} --no-compile --install-purelib %{_python_site_packages_path} --install-scripts /usr/local/bin && cd -

%files
%defattr(0755,root,root)
%{_python_site_packages_path}/hw_detector*

%pre

%post

%postun
